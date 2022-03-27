
  $(document).ready(function() {
    var deg = 180;
    $(".wrapper-login").fadeIn(1000);
    $(".right-sign").fadeIn(1000);
  });
  function myFunction1() {
    var x = document.getElementById("myDIV");
    var y = document.getElementById("myDIV1");
    var p = document.getElementById("r1");
    var q = document.getElementById("r2");
    
    x.style.display = "none";
    $(".wrapper-signIn").fadeIn(1000);
    p.style.display = "none";
    $(".right-log").fadeIn(1000);
    q.style.display = "block";

    
  }
  function myFunction2() {
    var a = document.getElementById("myDIV1");
    var b = document.getElementById("myDIV1");
    var c = document.getElementById("r2");
    var d = document.getElementById("r1");
    
    a.style.display = "none";
    $(".wrapper-login").fadeIn(1000);
    c.style.display = "none";
    $(".right-sign").fadeIn(1000);

  }

  function myFunction3() {
    var v = document.getElementById("myInput");
    // console.log("hello world");
    if (v.type === "password") {
      v.type = "text";
    } else {
      v.type = "password";
    }
  }
  function myFunction4() {
    var m = document.getElementById("id_password1");
    var n = document.getElementById("id_password2");
    // console.log("hello world");
    if (m.type === "password") {
      m.type = "text";
      n.type = "text";
    } else {
      m.type = "password";
      n.type = "password";
    }
  }