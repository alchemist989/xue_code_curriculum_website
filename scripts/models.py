# from __main__ import db


# class Composition(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     composition_name = db.Column(db.String(80), nullable=False)
#     composer = db.Column(db.String(80), nullable=False)
#     description = db.Column(db.String(5000), nullable=False)
#     video_link = db.Column(db.String(80), nullable=False)

#     def __repr__(self):
#         return 'Composition ' + self.composition_name + '>'

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(80), nullable=False)
#     password = db.Column(db.String(80), nullable=False)


# class CommentPost(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(80), nullable=False)
#     description = db.Column(db.String(5000), nullable=False)