$(document).ready(function(){
    if (sessionStorage.getItem('color') != 'null') {
      $("body").css('color', sessionStorage.getItem('color'));
    }

    if (sessionStorage.getItem('background-color-color') != 'null') {
      $("body").css('background-color', sessionStorage.getItem('background-color'));
    }

    // alert("" + sessionStorage.getItem('size') + "")

    if (sessionStorage.getItem('size') != 'null'){
      $("body").css('fontSize', sessionStorage.getItem('size') + "px")
    }
});