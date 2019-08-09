// Login Open Scripts
$(document).ready(function () {
  $(document).on("click", "#showLoginModal", function () {
    $(".modal").addClass("is-active");
  });

  $(document).on("click", ".closeLoginModal", function () {
    $(".modal").removeClass("is-active");
  });
});

// Login Endpoint
var login = function () {
  $.post({
    type: "POST",
    url: "/login",
    data: {
      "username": $("#login-user").val(),
      "email": $("#login-email").val(),
      "password": $("#login-pass").val()
    },
    success(response) {
      var status = JSON.parse(response)["status"];
      if (status === "Login successful") { location.reload(); }
      else { error("login-input"); }
    }
  });
};

// Sign Up Endpoint
var signup = function() {
  $.post({
    type: "POST",
    url: "/signup",
    data: {
      "username": $("#signup-user").val(),
      "email": $("#signup-email").val(),
      "password": $("#singup-pass").val()
    },
    success(response) {
      var status = JSON.parse(response)["status"];
      if (status === "Signup Sucessful") { location.reload(); }
      else {
        error("signup-input");
      }
    }
  });
};


// Comment Endpoint
var commentPost = function() {
  $.post({
    type: "POST",
    url: "/comments",
    data: {
      "username": $("#comment-user").val(),
      "email": $("#comment-email").val(),
      "comment": $("#comment-section").val()
    },
    success(response) {
      var status = JSON.parse(response)["status"];
      if (status == "Comment Sucessful") {
        location.reload();
      } else {
        error("comment-error");
      }
    }
  });
}

// Comment Delete
var commentDelete = function (event) {
  var comment_id = event.currentTarget.value;
  console.log(comment_id);
  $.post({
    type: "POST",
    url: "/comments/delete",
    data: {
      "comment_id": comment_id
    },
    success(response) {
      var status = JSON.parse(response)["status"];
      if (status == "Comment Deleted") {
        location.reload();
      } else {
        error("comment-delete-error");
      }
    }
  });

  // $.post({
  //   type: "POST",
  //   url: "/comments/delete",
  //   data: {
  //     "id": comment_id,
  //   },
  //   success(response) {
  //     var status = JSON.parse(response)["status"];
  //     if (status == "Comment Deleted") {
  //       location.reload();
  //     } else {
  //       error("comment-delete-error");
  //     }
  //   }
  // });
}


// Register Volunteer Post
var register = function() {
  $.post({
    type: "POST",
    url: "/register",
    data: {
      "organization": $("#register-org").val(),
      "email": $("#register-email").val(),
      "description": $("#register-description").val()},
    success(response) {
      var status = JSON.parse(response)["status"];
      if (status == "Registered Sucessful") {
        location.reload();
      } else {
        error("register-error");
      }
    }
  });
};



function error(type) {
  $("."+type).css("border-color", "#E14448");
}

// var btnClassClick = function (e) {
//   alert("Button clicked from class: " + e.currentTarget.id);
// }





$(document).ready(function() {
    
  $(document).on("click", "#comment-button", commentPost);
  $(document).on("click", "#signup-button", signup);
  $(document).on("click", "#register-button", register);
  $(document).on("click", "#login-button", login);
  $(document).on("click", "#signup-button", signup);
  $

  $(document).keypress(function(e) {if(e.which === 13) {login();}});
  


  $(document).on("click", "#save", function() {
    $.post({
      type: "POST",
      url: "/settings",
      data: {"username": $("#settings-user").val(), 
             "password": $("#settings-pass").val(), 
             "email": $("#settings-mail").val()},
      success(response){
        message(JSON.parse(response)["status"]);
      }
    });
  });
});

$(document).ready(function () {
  var carousels = bulmaCarousel.attach(); // carousels now contains an array of all Carousel instances
});

// Open or Close mobile & tablet menu
// https://github.com/jgthms/bulma/issues/856
$("#navbar-burger-id").click(function () {
  if($("#navbar-burger-id").hasClass("is-active")){
    $("#navbar-burger-id").removeClass("is-active");
    $("#navbar-menu-id").removeClass("is-active");
  }else {
    $("#navbar-burger-id").addClass("is-active");
    $("#navbar-menu-id").addClass("is-active");
  }
});



function message(status, shake = false, id = "") {
  if (shake) {
    $("#" + id).effect("shake", { direction: "right", times: 2, distance: 8 }, 250);
  }
  document.getElementById("feedback").innerHTML = status;
  $("#feedback").show().delay(2000).fadeOut();
}

function error(type) {
  $("." + type).css("border-color", "#E14448");
}