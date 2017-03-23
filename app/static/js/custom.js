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

// Active Nav Bar
$(function () {
    $('.nav li').click(function () {
        $(this).addClass('active').siblings().removeClass('active');
    })
});

//Clock Time
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
    if (i < 10) {
        i = "0" + i
    }
    ;  // add zero in front of numbers < 10
    return i;
}

// Pagination table - Patient
$(document).ready(function () {
    $('#patient_table').dataTable();
});

// Pagination table - Medicine
$(document).ready(function () {
    $('#medicine_table').dataTable();
});
