$(document).ready(function() {

    var pathArray = window.location.pathname.split('/');
    var id = pathArray[2];
    if (id == "options") {
        id = 0;
    } else {
        id = parseInt(id);
    }

    sessionStorage.setItem('returnId', id)

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
        } else {
            $(".container").css('background-color', 'black');
            $(".hero-unit").css('background-color', '#111111');
        }
    }

    if (sessionStorage.getItem("boldness") != null) {
        if (sessionStorage.getItem("boldness") == 400) {
            $("input[id=normal]").prop("checked", true);
        } else {
            $("input[id=bold]").prop("checked", true);
            $("txt[name=sample]").css("font-weight", 700);
        }
    }

    if (sessionStorage.getItem("size") != null) {
        $("txt[name=sample]").css("font-size", sessionStorage.getItem("size"));
        sizeValue = sessionStorage.getItem("size");
    } else {
        sizeValue = "72";
    }

    $("#size").val(sizeValue);

    $("#sizeSlider").slider({
        min: 18,
        max: 72,
        value: sizeValue,
        formatter: function(value) {
            return 'Current value: ' + value;
        }
    });
    $("#sizeSlider").on("slide", function(slideEvt) {
        $("#size").val(slideEvt.value);
    });

    $("#applySize").click(function(event) {
        event.preventDefault();
        sessionStorage.setItem('size', $("#size").val());
        $("txt[name=sample]").animate({
            "font-size": $("#size").val() + "px"
        });
    });

    $("#applyBold").click(function(event) {
        if ($("input[id='normal']:checked").val()) {
            sessionStorage.setItem("boldness", 400)
            $("txt[name=sample]").animate({
                "font-weight": 400
            });
        }
        if ($("input[id='bold']:checked").val()) {
            sessionStorage.setItem("boldness", 700)
            $("txt[name=sample]").animate({
                "font-weight": 700
            })
        }
    });

    // function to invert color
    $("#invert").click(function(event) {
        event.preventDefault();
        if (sessionStorage.getItem('color') == 'white') {
            // $("body").css('color', 'black');
            $(".container").css('color', 'black');
            sessionStorage.setItem('color', 'black');
        } else {
            // $("body").css('color', 'white');
            $(".container").css('color', 'white');
            sessionStorage.setItem('color', 'white');
        }
        if (sessionStorage.getItem('background-color') == 'white') {
            // $("body").css('background-color', 'black');
            $(".container").css('background-color', 'black');
            $(".hero-unit").css('background-color', '#111111');
            sessionStorage.setItem('background-color', 'black');
        } else {
            // $("body").css('background-color', 'white');
            $(".container").css('background-color', 'white');
            $(".hero-unit").css('background-color', '#eeeeee');
            sessionStorage.setItem('background-color', 'white');
        }
    });

});

function getSize() {
    $size = $("#sizeSlider").slider('getValue');
    $("#size").val($size);
    //$("txt[name=sample]").animate({"font-size":$size + "px"});
    //sessionStorage.setItem('size', $size);
    //$("h1").animate({"font-size":$size + "px"});
    //$("label").animate({"font-size":$size + "px"})
}