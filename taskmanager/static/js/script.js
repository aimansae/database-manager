document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialization check materialize doc

    var sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
  });

// modal

document.addEventListener('DOMContentLoaded', function() {
  var modal = document.querySelectorAll('.modal');
  M.Modal.init(modal);
});