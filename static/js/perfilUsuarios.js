document.addEventListener('DOMContentLoaded', function() {
    const logoutButton = document.getElementById('logoutButtonJovenes');
    const overlay = document.getElementById('overlay');
    const confirmLogout = document.getElementById('confirmLogout');
    const cancelLogout = document.getElementById('cancelLogout');

    logoutButton.addEventListener('click', (event) => {
        event.preventDefault();
        overlay.style.display = 'flex';
    });

    cancelLogout.addEventListener('click', () => {
        overlay.style.display = 'none';
    });
});