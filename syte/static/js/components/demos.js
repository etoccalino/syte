
function setupDemos(el) {
  var href = el.href;

  if ($('#demos-profile').length > 0) {
    window.location = href;
    return;
  }

  var spinner = new Spinner(spin_opts).spin();
  $('#demos-link').append(spinner.el);

  require(
    ["json!/demos", "text!templates/demos-profile.html"],
    function(demos_data, demos_view) {
      if (demos_data.error || demos_data.length == 0) {
        spinner.stop(); // DEBUG
        adjustSelection('home');  // DEBUG
        // window.location = href;
        return;
      }

      var template = Handlebars.compile(demos_view);
      $(template(demos_data)).modal().on('hidden', function () {
        $(this).remove();
        if (currSelection === 'demos') {
          adjustSelection('home');
        }
      });

      spinner.stop();
    });
}
