/**
 * Created by haibh on 22-Mar-17.
 */
// Add your javascript here
$(function () {
    $(".nav li").on("click", function () {
        $(".nav li").removeClass("active");
        $(this).addClass("active");
    });

});