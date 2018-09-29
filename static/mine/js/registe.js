$(function () {

    $('#account').blur(function () {
        $.get('/axf/checkacc/',{'account':$(this).val()},function (response) {
            if (response['status'] == '-1'){
                $('#acc').show().html(response['message'])
            }
            else {
                 $('#acc').hide()
            }

        })
    })
    $('#password').blur(function () {
       var password = $(this).val()
       if (password.length<6 || password.length>12){
           $('#psd').show().html('密码格式不正确')
          }
       else {
             $('#psd').hide()
       }
    })
    $('#mypassword').blur(function () {
       var mypassword = $(this).val()
       if (password.length<6 || password.length>12 || mypassword != $('#password').val()){
           $('#mypsd').show().html('密码不一致')
          }
       else {
             $('#mypsd').hide()
       }
    })
});