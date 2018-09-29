$(function () {

    //设置cookie
    typeindex = $.cookie('index')
    console.log(1)
    if (typeindex){
        $('.type-slider li').eq(typeindex).addClass('action');
    }
    else {
        $('.type-slider li:first').addClass('action');
    }


    $('.type-slider li').click(function () {

        $.cookie('index',$(this).index(),{exprires:3,path:'/'})
    });


    //隐藏滚动条
    $('.market').width(innerWidth+8)


    //全部分类下拉
    allbt = false
    $('#allbt').click(function () {
        allbt = !allbt
        if (allbt) {
            $('#childview').show()
            $('#allbt i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down')
            $('#sortview').hide()
            $('#sortbt i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
        }
        else {
            $('#childview').hide()
            $('#allbt i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
        }
    })

    sortbt = false
    $('#sortbt').click(function () {
        sortbt = !sortbt
        if (sortbt) {
            $('#sortview').show()
            $('#sortbt i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down')
            $('#childview').hide()
            $('#allbt i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')

        }
        else {
            $('#sortview').hide()
            $('#sortbt i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')

        }
    })
    //加入购物车
    //加操作
    $('.bt-wrapper>.num').hide()
    $('.bt-wrapper>.glyphicon-minus').hide()

    $('.bt-wrapper .num').each(function () {
        if (parseInt($(this).html())) {
            $(this).show()
            $(this).prev().show()
        }
    })

    $('.bt-wrapper>.glyphicon-plus').click(function () {
        goodid = $(this).attr('goodid')
        var $thisbt = $(this)
        $.get('/axf/addtocart/',{'goodid':goodid},function (response) {
            // console.log(response)
            if (response['status'] == '1'){
                $thisbt.prev().html(response['number']).show()
                $thisbt.prev().prev().show()
            }
            else {
                window.open('/axf/login/',target='_self')
            }
        })
    })

    //减操作
    $('.bt-wrapper>.glyphicon-minus').click(function () {
        goodid = $(this).attr('goodid')
        var $thisbt = $(this)
        $.get('/axf/subcart/',{'goodid':goodid},function (response) {
            console.log(response)
            if (response['status'] == '1'){
                $thisbt.next().html(response['number'])
                if (response['number'] <= '0') {
                    $thisbt.hide()
                    $thisbt.next().hide()

                }
            }
        })
    })
});