document.addEventListener("DOMContentLoaded", function () {
    let links = document.querySelectorAll(".main-nav ul li a");
    let currentPath = window.location.pathname;

    links.forEach(link => {
        if (link.getAttribute("href") === currentPath) {
            link.classList.add("active");
        }
    });
});
