var loader_script = '<div id="pre-loader">' +
    '<div class="spinner-border text-primary" role="status">' +
    '<span class="sr-only">Loading...</span>' +
    '</div>' +
    '</div>';
window.start_loader = function() {
    if ($('body>#pre-loader').length <= 0) {
        $('body').append(loader_script)
    }
}
window.end_loader = function() {
    var loader = $('body>#pre-loader')
    if (loader.length > 0) {
        loader.remove()
    }
}

(function($) { // Begin jQuery
    $(function() { // DOM ready
      // If a link has a dropdown, add sub menu toggle.
      $('nav ul li a:not(:only-child)').click(function(e) {
        $(this).siblings('.nav-dropdown').toggle();
        // Close one dropdown when selecting another
        $('.nav-dropdown').not($(this).siblings()).hide();
        e.stopPropagation();
      });
      // Clicking away from dropdown will remove the dropdown class
      $('html').click(function() {
        $('.nav-dropdown').hide();
      });
      // Toggle open and close nav styles on click
      $('#nav-toggle').click(function() {
        $('nav ul').slideToggle();
      });
      // Hamburger to X toggle
      $('#nav-toggle').on('click', function() {
        this.classList.toggle('active');
      });
    }); // end DOM ready
  })(jQuery); // end jQuery