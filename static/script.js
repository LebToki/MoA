$(document).ready(function () {
    const body = $('body');
    const toggleButton = $('#toggle-theme');

    toggleButton.on('click', function () {
        body.toggleClass('dark-mode');
        toggleButton.text(body.hasClass('dark-mode') ? 'Switch to Light Mode' : 'Switch to Dark Mode');
    });

    // Preserve theme across page reloads
    if (localStorage.getItem('theme') === 'dark') {
        body.addClass('dark-mode');
        toggleButton.text('Switch to Light Mode');
    }

    toggleButton.on('click', function () {
        body.toggleClass('dark-mode');
        if (body.hasClass('dark-mode')) {
            localStorage.setItem('theme', 'dark');
            toggleButton.text('Switch to Light Mode');
        } else {
            localStorage.setItem('theme', 'light');
            toggleButton.text('Switch to Dark Mode');
        }
    });
});
