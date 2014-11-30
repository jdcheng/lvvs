$(document).ready(function() {

    if (sessionStorage.getItem('color') != 'null') {
        $("body").css('color', sessionStorage.getItem('color'));
    }

    if (sessionStorage.getItem('background-color-color') != 'null') {
        $("body").css('background-color', sessionStorage.getItem('background-color'));
    }

    // alert("" + sessionStorage.getItem('size') + "")

    if (sessionStorage.getItem('size') != 'null') {
        $("body").css('fontSize', sessionStorage.getItem('size') + "px")
    }

    //alert("" + sessionStorage.getItem('boldness') + "")

    if (sessionStorage.getItem('boldness') != 'null') {
        $("body").css('fontWeight', sessionStorage.getItem('boldness'))
    }

    //$("body").css('text-weight', sessionStorage.getItem('boldness')) 

    if (sessionStorage.getItem("remember_choice_for_{{ question.id }}") != null) {
        $("input[value=" + sessionStorage.getItem('remember_choice_for_{{ question.id }}') + "]").prop("checked", true);
    };

    $("#vote").click(function(event) {
        if ($("input[name='choice']:checked").val()) {
            sessionStorage.setItem("remember_choice_for_{{ question.id }}", $('input[type=radio]:checked').val());
            var $id = $('input[type=radio]:checked').attr('id');
            //alert($id)
            var $name = $('label[for = ' + $id + ' ]').attr("name");
            // alert($name)
            var $party = $('label[for = ' + $id + ' ]').attr("party");
            // alert($party)
            $('input[type=radio]').prop("disabled", true);
            sessionStorage.setItem("remember_name_for_{{ question.id }}", $name);
            sessionStorage.setItem("remember_party_for_{{ question.id }}", $party);;
        }
    });

    $("#deselect").click(function(event) {
        $('input[type=radio]').prop("disabled", false);
        if ($("input[name='choice']:checked").val()) {
            $('input[type=radio]:checked').prop("checked", false);
            sessionStorage.setItem("remember_choice_for_{{ question.id }}", null);
        }
    });

});