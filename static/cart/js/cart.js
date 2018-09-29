$(function () {
    $('.cart').width(innerWidth)

    $('.cart .confirm-wrapper').click(function () {
        cartid = $(this).attr('cartid')
        // console.log(cartid)
        var $thistbt = $(this)

        $.get('/axf/changeselectstatus/',{'cartid':cartid},function (response) {
            console.log(response)

            if (response['status'] == '1'){

                $thistbt.children().remove()
                if (response['isselect']) {
                    $thistbt.append('<span class="glyphicon glyphicon-ok"></span>')
                }
                else {
                    $thistbt.append('<span class="no"></span>')
                }
            }
        })
    })


    $('.cart .bill .all').click(function () {
        var isall = $(this).attr('isall')
        isall = (isall == 'false') ? true : false
        $(this).attr('isall',isall)
        var $thistbt = $(this)
        $thistbt.children().remove()
        if (isall) {
            $thistbt.append('<span class="glyphicon glyphicon-ok"></span>').append('<b>全选</b>')
        }
        else {
            $thistbt.append('<span class="no"></span>').append('<b>全选</b>')
        }


        $.get('/axf/allselect/',{'isall':isall},function (response) {
            console.log(response)

            if (response['status'] == '1'){

                $('.confirm-wrapper').each(function () {
                    $(this).children().remove()
                    if (response['isselect']) {
                        $(this).append('<span class="glyphicon glyphicon-ok"></span>')
                    }
                    else {
                        $(this).append('<span class="no"></span>')
                    }
                })
            }
        })
    })
});