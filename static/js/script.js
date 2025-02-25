document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.getElementById("menu-toggle");
    const navLinks = document.getElementById("nav-links");

    // Toggle navigation menu when hamburger icon is clicked
    menuToggle.addEventListener("click", function () {
        navLinks.classList.toggle("active");
        
        // Optional: Change hamburger icon to 'X' when menu is open
        if (navLinks.classList.contains("active")) {
            menuToggle.innerHTML = "&#10005;"; // X symbol
        } else {
            menuToggle.innerHTML = "&#9776;"; // Hamburger symbol
        }
    });

    // Close menu when clicking outside
    document.addEventListener("click", function (event) {
        if (!event.target.closest('.Navbar') && navLinks.classList.contains("active")) {
            navLinks.classList.remove("active");
            menuToggle.innerHTML = "&#9776;";
        }
    });

    // Close menu when a menu item is clicked
    const navButtons = document.querySelectorAll('.Navbar_content');
    navButtons.forEach(button => {
        button.addEventListener("click", function() {
            if (window.innerWidth <= 768) { // Only on mobile
                navLinks.classList.remove("active");
                menuToggle.innerHTML = "&#9776;";
            }
        });
    });

    // Handle window resize
    window.addEventListener("resize", function() {
        if (window.innerWidth > 768) {
            navLinks.classList.remove("active");
            menuToggle.innerHTML = "&#9776;";
        }
    });
});