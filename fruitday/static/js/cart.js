// 等待文档加载完毕后执行
$(function(){
    // 1.全选与取消全选
    var isTrue = false;
    $('#checkall').click(function(){
        // 更改状态标识
        isTrue = !isTrue;
        $("[name = check]").prop("checked",isTrue);
        countItem();
        // if(isTrue){
        //     $('[name = check]').prop('checked',true);
        // }else{
        //     $('[name = check]').prop('checked',false);
        // }
    })

    // 2.反选
    // 按钮监听，选中与取消状态改变
    $("[name = check]").change(function(){
        // 判断商品复选框，未被选中的数量 <= 0,说明全选
        //:eq :not()
        //eq(index)根据下标获取元素
        // not("")获取元素，给出否定条件
        // input:checked 匹配被选中的输入框
        //size() 获取数组长度，元素个数
        var isAll = $("[name = check]").not("input:checked").size() <= 0; 
        $('#checkall').prop('checked',isAll);
        isTrue = isAll;
        countItem();
    });
    // 3 加减数量
    var i = 1;
    $('.decrement').click(function(){
        if($(this).next().val() > 1){
            //值--
            var value = $(this).next().val();
            $(this).next().val(--value);
            var priceStr = $(this).parent().prev().html();
            var price = Number(priceStr.substring(1));

            $(this).parent().next().html('<b>&yen;'+ value * price + '</b>');
            countItem();
        }
    })

    $('.increment').click(function(){
        //值++
        var value = $(this).prev().val();
        $(this).prev().val(++value);
        // 获取单价
        var priceStr = $(this).parent().prev().html();
        var price = Number(priceStr.substring(1));
        $(this).parent().next().html('<b>&yen;'+ value * price + '</b>');
        countItem();
    })
    $('[name = countText]').blur(function(){
        // 获取输入的值,更改总价
        var count = Number($(this).val());
        console.log(count);
        var priceStr = $(this).parent().prev().html();
        var price = Number(priceStr.substring(1));
        console.log(price);
        $(this).parent().next().html('<b>&yen;'+ count * price + '</b>');
        countItem();
    })
    // 4.移出商品
    $('.action a').click(function(){
        // 删除整条商品记录.g-item
        $(this).parents('.g-item').remove();
        countItem();
    })
    // 5.工具栏中数量与价格的联动
    function countItem(){
        var sum = 0; //勾选的商品总数
        var priceSum = 0; //对应的总价格
        // 1. 遍历被勾选的元素
        // 2.获取被勾选元素中的数量与小计
        // 3.累加并显示在工具栏
        $('[name = check]:checked').each(function(){
            var Sum =  Number($(this).parents('.g-item').find('[name = countText]').val());
            var price = Number($(this).parents('.g-item').find('.t-sum').text().substring(1));
            sum += Sum;
            priceSum += price;
        })
        $('.submit-count').children().html(sum);
        $('.submit-price').children().html('&yen;'+priceSum);
    }
})