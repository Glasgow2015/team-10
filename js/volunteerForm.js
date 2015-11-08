$(function() {
    $('input[id="form-dob-calendar-field"]').
    daterangepicker({
        startDate: new moment(),
        singleDatePicker: true,
        showDropdowns: true
    });
});
