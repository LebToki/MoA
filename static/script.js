$(document).ready(function () {
    // Load saved theme
    const theme = localStorage.getItem('theme') || 'light-mode';
    $('body').addClass(theme);

    // Toggle theme on button click
    $('#toggle-theme').click(function () {
        $('body').toggleClass('light-mode dark-mode');

        // Save the selected theme to localStorage
        const currentTheme = $('body').hasClass('dark-mode') ? 'dark-mode' : 'light-mode';
        localStorage.setItem('theme', currentTheme);

        // Update button text
        const buttonText = $('body').hasClass('dark-mode') ? 'Switch to Light Mode' : 'Switch to Dark Mode';
        $(this).text(buttonText);
    });

    // Reset conversation
    $('#reset-conversation').click(function () {
        $.post('/reset', function () {
            location.reload();
        });
    });

    // Set initial button text
    const initialButtonText = $('body').hasClass('dark-mode') ? 'Switch to Light Mode' : 'Switch to Dark Mode';
    $('#toggle-theme').text(initialButtonText);
});
