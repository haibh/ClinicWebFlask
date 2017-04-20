//Clock Time
function startTime() {
    var today = new Date();
    document.getElementById('clock_display').innerHTML = today.toDateString() + ' ' + today.toLocaleTimeString();
    var t = setTimeout(startTime, 1000);
}


// Pagination table:
$(document).ready(function () {
    $('#patient_table').dataTable();
    $('#medicine_table').dataTable();
});

