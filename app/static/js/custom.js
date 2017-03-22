/**
 * Created by haibh on 22-Mar-17.
 */
// Add your javascript here
// $(function () {
//     $(".nav li").on("click", function () {
//         $(".nav li").removeClass("active");
//         $(this).addClass("active");
//     });
// });

$(function () {
    $('.nav li').click(function () {
        $(this).addClass('active').siblings().removeClass('active');
    })
});


function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('clock_display').innerHTML =
    h + ":" + m + ":" + s;
    var t = setTimeout(startTime, 500);
}
function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}

