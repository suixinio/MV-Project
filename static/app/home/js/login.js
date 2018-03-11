function checkemail() {
    var reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$"); //正则表达式
    var obj = document.getElementById("username"); //要验证的对象

    console.log(obj.value)
    if (obj.value === "") { //输入不能为空
        $('#email_flag').val(0)
    } else if (!reg.test(obj.value)) { //正则验证不通过，格式不对
        $('#email_flag').val(0)
    } else {
        $('#email_flag').val(1)
    }
}


function check() {
    checkemail()
    var password = $('#password').val();
    // alert(password)
    var newpassword = md5(password);
    $('#password').val(newpassword);

    return true;
}

