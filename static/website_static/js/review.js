$(document).ready(function(){
    if (sessionStorage.getItem('color') == null) {
        sessionStorage.setItem('color', 'black');
    } else {
        $(".container").css('color', sessionStorage.getItem('color'));
    }

    if (sessionStorage.getItem('background-color') == null) {
        sessionStorage.setItem('background-color', 'white');
    } else {
        if (sessionStorage.getItem('background-color') == 'white') {
            $(".container").css('background-color', 'white');
            $(".hero-unit").css('background-color', '#eeeeee');
            //$("label[class=radio]").css('background-color', 'black')
        } else {
            $(".container").css('background-color', 'black');
            $(".hero-unit").css('background-color', '#111111');
        }
    }

    if (sessionStorage.getItem('size') != 'null'){
      $(".container").css('fontSize', sessionStorage.getItem('size') + "px")
      $("span").css('fontSize', sessionStorage.getItem('size') + "px")
    }

    $("#ballot-container *").css('line-height', "2.0em");
});