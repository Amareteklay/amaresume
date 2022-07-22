// Function to display and hide alert messages.
setTimeout(function() {
        let messagesBox = document.getElementById('messages-notes');
        if (messagesBox) {
            messagesBox.style.display = 'none';
        }
    },
    2500);

// Add event listener to menu items in navbar
document.addEventListener('DOMContentLoaded', function() {
    const navbarItems = document.getElementsByClassName('nav-link');
    for (let i = 0; i < navbarItems.length; i++) {
        if (navbarItems[i].href === window.location.href) {
            navbarItems[i].classList.add('active-menu');
        }
    }
});