# -*- coding: utf-8 -*-

# from scripts import tabledef
from scripts import forms
from scripts import helpers
from flask import Flask, redirect, url_for, render_template, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
import flask_excel as excel
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
excel.init_excel(app)

# from scripts import models
class Composition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    composition_name = db.Column(db.String(80), nullable=False)
    composer = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(5000), nullable=False)
    video_link = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return 'Composition ' + self.composition_name + '>'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)


class CommentPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    comment = db.Column(db.String(5000), nullable=False)

    def __repr__(self):
        return 'Comment ' + self.username + '>'

db.create_all()



# ======== Routing =========================================================== #
# -------- Login ------------------------------------------------------------- #
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/import', methods=['GET', 'POST'])
def do_import():
    # Clean Database and recreate database
    Composition.query.delete()
    
    if request.method == "POST":
        def init_func(row):
            composition = Composition(
                                row['composition_name'],
                                row['composer'],
                                row['description'],
                                row['video_link']
                                )
            composition.id = row['id']
            return composition
        request.save_to_database(
            field_name='file', session=db.session, table=Composition, initializers=[init_func])
    return '''
        <!doctype html>
        <title>Upload an excel file</title>
        <a href="javascript:history.back()">Go Back</a>
        <h1>Excel file upload (xls, xlsx, ods please)</h1>
        <form action="" method=post enctype=multipart/form-data><p>
        <input type=file name=file><input type=submit value=Upload>
        </form>
        '''


@app.route('/compositions')
def compositionsEndpoint():
    # Convert SQL_achlemy object to dictionary
    dict_compositions = []
    for composition in Composition.query.all():
        dict_compositions.append(composition.__dict__)

    return render_template('compositions.html', compositions=dict_compositions)

@app.route("/comments", methods=["GET"])
def getComments():
    dict_comments = []
    for comment in CommentPost.query.all():
        dict_comments.append(comment.__dict__)
    return render_template('comments.html', comments=dict_comments)


@app.route("/comments", methods=["POST"])
def postComments():
    username = request.form['username']
    email = request.form['email']
    comment = request.form['comment']
    if forms.CommentForm(request.form).validate():
        new_comment = CommentPost(username=username, email=email, comment=comment)
        db.session.add(new_comment)
        db.session.commit()
        return json.dumps({'status': 'Comment Sucessful'})
    else:
        return json.dumps({'status': 'All Fields are required'})

        
@app.route("/comments/delete", methods=["POST"])
def deleteComment():
    comment_id = request.form['comment_id']
    print(comment_id)
    delete_comment = CommentPost.query.filter_by(id=comment_id).first();
    db.session.delete(delete_comment)
    db.session.commit()
    return json.dumps({'status': 'Comment Deleted'})

@app.route("/biography/<string:life_stage>", methods=["GET"])
def biography(life_stage):
    # if life_stage == "early":
    #     return render_template('biography/early.html')
    # elif life_stage == "mid":
    #     return render_template('biography/mid.html')
    # elif life_stage == "late":
    #     return render_template('biography/late.html')


    if life_stage == "early":
        return render_template('biography/early.html')
    elif life_stage == "early_mid":
        return render_template('biography/early-mid.html')
    elif life_stage == "late_mid":
        return render_template('biography/late-mid.html')
    elif life_stage == "late":
        return render_template('biography/late.html')
    else:
        return json.dumps("Incorrect route")













@app.route("/login", methods=['GET', 'POST'])
def login():
    if not session.get('logged_in'):
        if request.method == 'POST':
            username = request.form['username'].lower()
            password = request.form['password']
            if forms.LoginForm(request.form).validate():

                if helpers.credentials_valid(username, password):
                    session['logged_in'] = True
                    session['username'] = username
                    session['email'] = email
                    return jsonify({'status': 'Login successful'})
                else:
                    return jsonify({'status': 'Invalid username/password'})

            else:
                return jsonify({'status': 'Both fields required'})
    else:
        return render_template('home.html')
    

@app.route("/logout")
def logout():
    return_template('home.html');



# -------- Signup ---------------------------------------------------------- #
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # Get Method Handler
    if request.method == 'GET':
        if not session.get('logged_in'):
            return render_template('signup.html')
        else:
            return render_template('home.html')
    elif request.method == 'POST':
        if session.get('logged_in'):
            return jsonify({'status': 'You are already logged in'})
        else:
            username = request.form('username').lower
            email = request.form('email').lower
            password = request.form('password')
            if not helper.username_taken(username):
                helper.add_user(username, email, password)
                return render_template('home.html')
            else:
                return jsonify({'status': 'Username Taken'})
    
            
        # Check if I have an account in the Database


@app.route('/register', methods=['GET', 'POST'])
def register():
    # Registering a new opporunity
    if request.method == 'POST':
        print(request.form['organization'])
        print(request.form['email'])
        print(request.form['description'])
        return json.dumps({'status': 'Registered successful'})
    else:
        return render_template('register.html');

@app.route('/listings', methods=['GET', 'POST'])
def listings():
    return render_template('listings.html');


# ======== Main ============================================================== #
if __name__ == "__main__":
    app.secret_key = os.urandom(12)  # Generic key for dev purposes only
    app.run(debug=True, use_reloader=True)






