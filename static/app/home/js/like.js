$(function () {

    $('.movie-like').click(function () {
        // alert(123)
        // var likes = $('this').('div').attr('postid')
        var postid = $(this).attr('postid')
        // var postid = likes.parent('.movie-like')
        // var postid = likes
        // alert(postid,likes)

        console.log('attr:' + postid);
        $.getJSON('/app/addlike/', {'postid': postid}, function (data) {
            console.log(data)
            if (data['status'] == '302') {
                window.open('/app/login/', target = '_self');
            } else if (data['status'] == '200') {
                console.log(data['num'])
                // goods.prev('span').html(data['num'])
            }
        })
    })
    $('.no-like').click(function () {
        // alert(123)
        // var likes = $('this').('div').attr('postid')
        var postid = $(this).attr('postid')
        // var postid = likes.parent('.movie-like')
        // var postid = likes
        // alert(postid,likes)

        console.log('attr:' + postid);
        $.getJSON('/app/sublike/', {'postid': postid}, function (data) {
            console.log(data)
            if (data['status'] == '302') {
                window.open('/app/login/', target = '_self');
            } else if (data['status'] == '200') {
                console.log(data['num'])
                // goods.prev('span').html(data['num'])
            }
        })
    })

})


$(function () {
    // $('#like').click(function () {
    // }
    // $('#movie_list_right').delegate('p', 'click', function () {
    //     alert("ssss");
    // });

    // $('#movie_list>li').each(function (index) {
    //     // $(this).on('click', function () {
    //     //     $('.text').val($('.evals>li').eq(index).html());
    //     // })
    //     $('#movie-like').click(function () {
    //     alert(123)
    // })
    // })


})