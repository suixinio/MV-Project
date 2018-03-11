username_flag = false
password_flag = false
repassword_flag = false
mail_flag = false
icon_flag = false

$(function () {
    $('#username').change(function () {
        var username = $(this).val();
        //$(selector).get(url,data,success(response,status,xhr),dataType)
        //可选。规定连同请求发送到服务器的数据。
        //可选。规定当请求成功时运行的函数,一定不要忘记传参数
        $.get('/app/checkuser/', {'username': username}, function (data) {
            console.log(data);
            if (data['status'] == '888') {
                $('#username_info').html(data['msg']).css('color', 'green');
                username_flag = true
            } else {
                $('#username_info').html(data['msg']).css('color', 'red');
                username_flag = false
            }
        })
    })

    $('#password').change(function () {
        var password = $(this).val();
        if (password.length < 6 | password.length > 16) {
            $('#password_info').html('密码长度不符合规范').css('color', 'red');
            password_flag = false
        } else {
            $('#password_info').html('密码长度规范').css('color', 'green');
            password_flag = true
        }
    })


    $('#repassword').change(function () {
        var repassword = $(this).val();
        var password = $('#password').val();
        if (password == repassword) {
            $('#repsw_info').html('密码一致').css('color', 'green');
            repassword_flag = true
        } else {
            $('#repsw_info').html('密码不一致').css('color', 'red');
            repassword_flag = false
        }
    })

    $('#u_email').change(function () {
        var reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$"); //正则表达式
        var obj = document.getElementById("u_email"); //要验证的对象

        console.log(obj.value)
        if (obj.value === "") { //输入不能为空
            alert("输入不能为空!");
            $('#email_info').html('输入不能为空').css('color', 'red');
            mail_flag = false;
        } else if (!reg.test(obj.value)) { //正则验证不通过，格式不对
            $('#email_info').html('输入邮箱格式不正确').css('color', 'red');
            mail_flag = false;
        } else {
            $('#email_info').html('邮箱验证通过').css('color', 'green');
            mail_flag = true
        }
    })

})

function deal_icons() {
    var filePath = $("#exampleInputFile").val();
    console.log(filePath)
    if ("" != filePath) {
        var fileType = getFileType(filePath);
        //判断上传的附件是否为图片

        if ("jpg" != fileType && "jpeg" != fileType && "bmp" != fileType && "png" != fileType && "gif" != fileType) {
            $("#file").val("");
            alert("请上传JPG,JPEG,BMP,PNG,GIF格式的图片");
            return
        } else {
            // TODO 获取大小出错,不解决放着
            //获取附件大小（单位：KB）
            // var fileSize = document.getElementById("file").files[0].size / 1024;
            // if (fileSize > 2048) {
            //     alert("图片大小不能超过2MB");
            // }
            // alert('123')

        }
        icon_flag = true
    }
}

function getFileType(filePath) {
    var startIndex = filePath.lastIndexOf(".");
    if (startIndex != -1)
        return filePath.substring(startIndex + 1, filePath.length).toLowerCase();
    else return "";
}

// TODO lj 提交表单的时候进行摘要，信息更安全
function check() {

    // 处理头像
    deal_icons()
    // alert('123')

    // var coinfile = $('exampleInputFile').val()
    // console(coinfile,typeof coinfile)

    if (!(mail_flag && repassword_flag && username_flag && password_flag && icon_flag)) {
        return false
    }
    var password = $('#password').val();
    var repassword = $('#repassword').val();
    var username = $('#username').val();
    var u_mail = $('#u_email').val();

    if ((password != repassword) && (password == '' && repassword == '' && username == '' && u_mail == '')) {
        return false
    }
    var newpassword = md5(password);
    // alert(newpassword)
    $('#password').val(newpassword);
    console.log('摘要后的', newpassword);
    return true;
}











