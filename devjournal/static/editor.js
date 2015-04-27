"use strict";

function getIfPresent(obj, k , selector) {
    var dt = $(selector);
    if(dt) {
        obj[k] = dt.val();
    }
    return obj;
}

function getProjectUrl(){
    var project_host = $("project_host");
    var project_url = $("#project_url");
}

$(document).ready(function() {
    $("#send_button").click(function() {
        var d = {
            page_name: $('#name').val(),
            page_content: $('#editor').val(),
            page_categories: $('#tags').val()
        };
        d = getIfPresent(d, 'start', "start_datetime");
        d = getIfPresent(d, 'end', "end_datetime");
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
    $(".tab-container #meta-edit-tab").click(function (e){
        $("#editor-div")[0].style.display = "none";
        $("#meta-edit")[0].style.display = "block";
    });
    $(".tab-container #editor-div-tab").click(function (e){
        $("#meta-edit")[0].style.display = "none";
        $("#editor-div")[0].style.display = "block";
    });

    $("#start_datetime").datetimepicker();
    $("#end_datetime").datetimepicker();
});