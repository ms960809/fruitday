// 轮播图
window.onload = function(){
    var imgIndex = 0;
    var img1 = document.getElementById('d1');
    var img2 = document.getElementById('d2');
    var imgs = [img1,img2];
    var h1 = document.getElementById('h1');
    var h2 = document.getElementById('h2');
    var h = [h1,h2];
    h1.onclick = function fh1(){
        img1.style.display = 'block';
        img2.style.display = 'none';
    }
    h2.onclick = function fh1(){
        img2.style.display = 'block';
        img1.style.display = 'none';
    }
    function a(){
                for(var i = 0; i < imgs.length; i ++){
                    if(i == imgIndex){
                        imgs[imgIndex].style.display = 'block';
                        for(var d = 0; d < h.length; d ++){
                            if(d == imgIndex){
                                h[d].style.color = 'red';
                            }
                            else{
                                h[d].style.color = 'green';
                            }
                        }
                    }
                    else{
                        imgs[i].style.display = 'none';
                        for(var d = 0; d < h.length; d ++){
                            if(d == imgIndex){
                                h[d].style.color = 'red';
                            }
                            else{
                                h[d].style.color = 'green';
                            }
                        }

                    }
                }
                imgIndex++;
                if(imgIndex == 2){
                    imgIndex = 0;
                }
                
            }
setInterval(a,3000);
}
// $(function(){
//     // 图片轮播
//      var imgIndex = 0;  //图片下标
//      var timerID;  //保存定时器ID
//      timerID = setInterval(autoPlay,1000);  //开启定时器
//     //  定时器方法，每隔一秒执行一次
//      function autoPlay(){
//         //  获取图片，根据下标设置元素显示与隐藏
//         $('.banner img').eq(imgIndex).css('display','none');
//         imgIndex = ++imgIndex == $('.banner img').length ? 0 :imgIndex;
//         $('.banner img').eq(imgIndex).css('display','block');
//         // $('.imgNav li').eq(imgIndex).css('background','gray');
//         $('.imgNav li').each(function(){
//             // 遍历数组对每个元素修改背景色
//             $(this).css('background','gray');
//         })
//         // 切换下标（变更背景颜色）
//         $('.imgNav li').eq(imgIndex).css('background','red');
//      }
//     //  鼠标移入（关闭定时器），移出（重新自动播放）操作
//     $('.banner').mouseover(function(){
//         clearInterval(timerID);
//     })
//     $('.banner').mouseout(function(){
//         timerID = setInterval(autoPlay,1000);
//     })
//     // 鼠标点击切换图片
//     $('.imgNav li').each(function(){
//         $(this).click(function(){
//             // 点击切换时，停止定时器
//             clearInterval(timerID);
//             // 背景颜色点击的为红色，其他li元素背景色为灰色
//             $(this).css('background','red').siblings().css('background','grey');
//             // 获取当前被点击元素的下标
//             var index = $(this).index();
//             $('.banner img').eq(index).css('display','block').siblings().css('display','none');
//             imgIndex = index;
//             var timerID = setInterval(autoPlay,1000);
//         })
//     })
// })
