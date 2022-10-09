document.addEventListener('DOMContentLoaded', function () {
// sidenav initialization check materialize doc

var sidenav = document.querySelectorAll('.sidenav');
M.Sidenav.init(sidenav);

// modal

var modal = document.querySelectorAll('.modal');
M.Modal.init(modal);
//date picker


var datepicker = document.querySelectorAll('.datepicker');
M.Datepicker.init(datepicker, {
  format: "dd mmm, yyyy",
  i18n: {
    done: "Select"
  }
});
// select initialization
var selects = document.querySelectorAll('select');
M.For
// collapsible initialization

var collapsibles = document.querySelectorAll('.collapsible');
M.Collapsible.init(collapsibles);

});