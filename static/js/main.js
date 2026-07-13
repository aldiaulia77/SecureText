// SecureText - script global
document.addEventListener("DOMContentLoaded", () => {
    // Auto-hide flash messages setelah 4 detik
    document.querySelectorAll(".flash").forEach((el) => {
        setTimeout(() => {
            el.style.transition = "opacity .4s ease";
            el.style.opacity = "0";
            setTimeout(() => el.remove(), 400);
        }, 4000);
    });
});
