"use strict";
$(document).ready(function() {
    $("#send_button").click(function() {
        var d = {
            page_name: $('#name').val(),
            page_content: $('#editor').val(),
            page_categories: $('#tags').val()
        };
        $.ajax({
            method: 'POST',
            url: document.location,
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(d),
            dataType: 'json',
            success: function(data, status, xhr){
                if(data.redirect) {
                    window.location.href = data.redirect;
                }
                $("#send_button").style.backgroundColor = 'green';
            },
            error: function(xhr, status, errorThrown) {
                console.log(status + ': ' + errorThrown);
                $("#send_button").style.backgroundColor = 'red';
            }
        });
    });
});