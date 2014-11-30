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
        sessionStorage.setItem('background-color', 'white');
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
        $sizeValue = sessionStorage.getItem("size");
    } else {
        $sizeValue = "18";
    }

    $("#size").val($sizeValue);

    $("#sizeSlider").slider({
        min: 18,
        max: 72,
        value: $sizeValue,
        slide: function(event, ui) {
            getSize();
        }
    });

    $("#applySize").click(function(event) {
        event.preventDefault();
        sessionStorage.setItem('size', $size);
        $("txt[name=sample]").animate({
            "font-size": $size + "px"
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
            $("body").css('color', 'black');
            sessionStorage.setItem('color', 'black');
        } else {
            $("body").css('color', 'white');
            sessionStorage.setItem('color', 'white');
        }
        if (sessionStorage.getItem('background-color') == 'white') {
            $("body").css('background-color', 'black');
            sessionStorage.setItem('background-color', 'black');
        } else {
            $("body").css('background-color', 'white');
            sessionStorage.setItem('background-color', 'white');
        }
    });
});

function getSize() {
    $size = $("#sizeSlider").slider("values", 0);
    $("#size").val($size);
}

function validate_user_id() {
    var x = document.getElementById("user_id").value;
    if (x == null || x == "") {
        alert("Please enter your user id");
        document.getElementById("user_id").style.backgroundColor = "FF9494";
        return false;
    }
}