$(document).ready(function(){
    if (sessionStorage.getItem('color') != 'null') {
        $(".container").css('color', sessionStorage.getItem('color'));
    }

    if (sessionStorage.getItem('background-color') != 'null') {
        $(".container").css('background-color', sessionStorage.getItem('background-color'));
    }

    //if (sessionStorage.getItem('size') != 'null') {
    //    $("#ballot-container *").css('font-size', sessionStorage.getItem('size') + "px")
    ''}

    if (sessionStorage.getItem('boldness') != 'null') {
        $("#ballot-container *").css('fontWeight', sessionStorage.getItem('boldness'))
    }

    $("#ballot-container *").css('line-height', "2.0em");
    $("#ballot-container *").css('list-style', "none");

});