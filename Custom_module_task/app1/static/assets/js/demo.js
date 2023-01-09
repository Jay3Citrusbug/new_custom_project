/*$(document).on("click", "#save_campaign_btn", function () {
    let campaign_name = $("#campaign_name").val()
    $("#camp_name").text(campaign_name)
    $("#campaign_name").val(campaign_name)
    let name = $("#campaign_name").val()
    let trigger_type
    let trigger_val
    if ($("#Keywords")[0].checked == true) {
        trigger_type = 'Keywords'
        trigger_val = {
            'number': $("#keyword_trigger_number").val(),
            'keyword': $("#keyword_trigger_keyword").val()
        }
    }
    else if ($("#date_based")[0].checked == true) {
        trigger_type = 'date_based'
        trigger_val = {
            'date_field': $("#date_based_trigger_date_field").val(),
            'before_day': $("#date_based_trigger_before_day").val()
        }
    }
    else if ($("#tags")[0].checked == true) {
        trigger_type = 'tags'
        trigger_val = {
            'tag_based': $("#tag_based_trigger").val()
        }
    }
    else
        trigger_type = trigger_val = ''


    let status = true
    let sending_window_status = $("#sending_window_status")[0].checked
    let days = {
        'monday': $("#monday")[0].checked,
        'tuesday': $("#tuesday")[0].checked,
        'wednesday': $("#wednesday")[0].checked,
        'thursday': $("#thursday")[0].checked,
        'friday': $("#friday")[0].checked,
        'saturday': $("#saturday")[0].checked,
        'sunday': $("#sunday")[0].checked,

    }
    let start_time = $("#start_time").val()
    let end_time = $("#end_time").val()
    let send_number = $("#send_number").val()
    let double_optin_status = $("#double_optin_status")[0].checked
    let double_optin_keyword = $("#double_optin_keyword").val()
    let double_optin_message = $("#double_optin_message").val()
    let limit_multiple_status = $("#limit_multiple_status")[0].checked
    let limit_multiple_message = $("#limit_multiple_message").val()
    let cancellation_trigger_status = $("#cancellation_trigger_status")[0].checked
    let on_reply = $("#on_reply")[0].checked


    console.log("name =", name);
    console.log("trigger_type =", trigger_type)
    console.log("trigger_val =", trigger_val)
    console.log("status =", status)
    console.log("sending_window_status =", sending_window_status)
    console.log("days =", days)
    console.log("start_time =", start_time)
    console.log("end_time =", end_time)
    console.log("send_number =", send_number)
    console.log("double_optin_status =", double_optin_status)
    console.log("double_optin_keyword =", double_optin_keyword)
    console.log("double_optin_message =", double_optin_message)
    console.log("limit_multiple_status =", limit_multiple_status)
    console.log("limit_multiple_message =", limit_multiple_message)
    console.log("cancellation_trigger_status =", cancellation_trigger_status)
    console.log("on_reply =", on_reply)
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    console.log("csrf =", csrftoken)
    let fd = new FormData()
    fd.append('name', name)
    fd.append('trigger_type', trigger_type)
    fd.append('trigger_val', trigger_val)
    fd.append('status', status)
    fd.append('sending_window_status', sending_window_status)
    fd.append('days', days)
    fd.append('start_time', start_time)
    fd.append('end_time', end_time)
    fd.append('send_number', send_number)
    fd.append('double_optin_status', double_optin_status)
    fd.append('double_optin_keyword', double_optin_keyword)
    fd.append('double_optin_message', double_optin_message)
    fd.append('limit_multiple_status', limit_multiple_status)
    fd.append('limit_multiple_message', limit_multiple_message)
    fd.append('cancellation_trigger_status', cancellation_trigger_status)
    fd.append('on_reply', on_reply)
    console.log("-------------------------")
    console.log("Form data")
    console.log(fd)
    // window.location = '/campaign'
    $.ajax({
        url: '/add_campaign',
        method: 'POST',
        data: fd,
        cache: false,
        processData: false,
        contentType: false,
        async: true,

        success: function (list) {
            console.log("insert success")

        },
        error: function (response) {
            console.log('Inside error block------');
        },
        complete: function () {
        }
    });

});*/