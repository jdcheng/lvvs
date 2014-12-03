$(document).ready(function() {

    if (sessionStorage.getItem('color') != 'null') {
        $(".container").css('color', sessionStorage.getItem('color'));
    }

    if (sessionStorage.getItem('background-color') != 'null') {
        $(".container").css('background-color', sessionStorage.getItem('background-color'));
    }

    if (sessionStorage.getItem('size') != 'null') {
        $("#ballot-container *").css('font-size', sessionStorage.getItem('size') + "px")
    }

    if (sessionStorage.getItem('boldness') != 'null') {
        $("#ballot-container *").css('fontWeight', sessionStorage.getItem('boldness'))
    }

    if (sessionStorage.getItem("remember_choice_for_{{ question.id }}") != 'null') {
        $("input[value=" + sessionStorage.getItem('remember_choice_for_{{ question.id }}') + "]").prop("checked", true);
        //alert(""+sessionStorage.getItem('background-color'))
        if (sessionStorage.getItem('background-color') == 'black'){
            //alert("test1")
            $("label[value=" + sessionStorage.getItem('remember_choice_for_{{ question.id }}') + "]").css('background-color', 'white');
            $("label[value=" + sessionStorage.getItem('remember_choice_for_{{ question.id }}') + "]").css('color', 'black');
        }
        else{
            //alert("test2")
            //alert(sessionStorage.getItem('remember_party_for_{{ question.id }}') + ""))
            $("label[value=" + sessionStorage.getItem('remember_choice_for_{{ question.id }}') + "]").css('background-color', 'black');
            $("label[value=" + sessionStorage.getItem('remember_choice_for_{{ question.id }}') + "]").css('color', 'white');
            //alert(""+sessionStorage.getItem('remember_party_for_{{ question.id }}') + "]"))
        }
        //alert("testagain")
    };

    if ($("input[name='choice']:checked").val()) {
       $("input[name='choice']:radio").attr('disabled', true);
    }

    $("#ballot-container *").css('line-height', "2.0em");

    $("#vote").click(function(event) {
        event.preventDefault();
        if ($("input[name='choice']:checked").val()) {
            sessionStorage.setItem("remember_choice_for_{{ question.id }}", $('input[type=radio]:checked').val());
            var $id = $('input[type=radio]:checked').attr('id');
            // alert($id)
            var $name = $('label[for = ' + $id + ' ]').attr("name");
            // alert($name)
            var $party = $('label[for = ' + $id + ' ]').attr("party");
            // alert($party)
            $('input[type=radio]').prop("disabled", true);
            sessionStorage.setItem("remember_name_for_{{ question.id }}", $name);
            sessionStorage.setItem("remember_party_for_{{ question.id }}", $party);
        }
        $(this).unbind("click").click();
    });

    $("#deselect2").click(function(event){
        $('input[type=radio]').prop("disabled", false);
        if (sessionStorage.getItem('background-color') == 'black'){
            //alert("test1")
            $("label").css('background-color', 'black');
            $("label").css('color', 'white');
        }
        else{
            //alert("test2")
            //alert(sessionStorage.getItem('remember_party_for_{{ question.id }}') + ""))
            $("label").css('background-color', 'white');
            $("label").css('color', 'black');
            //alert(""+sessionStorage.getItem('remember_party_for_{{ question.id }}') + "]"))
        }
        if ($("input[name='choice']:checked").val()) {
            $('input[type=radio]:checked').prop("checked", false);
            sessionStorage.setItem("remember_choice_for_{{ question.id }}", null);
            sessionStorage.setItem("remember_name_for_{{ question.id }}", "No selection for this race");
            sessionStorage.setItem("remember_party_for_{{ question.id }}", " ");
        }
    });
});