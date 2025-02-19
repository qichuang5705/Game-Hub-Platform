document.addEventListener("DOMContentLoaded", () => {
    const uploadGameSection = document.querySelector(".upload-game-container");
    const gamePostedSection = document.querySelector(".container_game_posted");

    // Close upload Game
    const closeUploadGame = document.querySelector(".close-upload");
    closeUploadGame.addEventListener("click", () => {
        uploadGameSection.classList.add("hide");
        uploadGameSection.classList.remove("show");

        gamePostedSection.classList.add("show");
        gamePostedSection.classList.remove("hide");
    });

    // Open upload Game
    const openUploadGame = document.querySelector(".open-upload-btn");
    openUploadGame.addEventListener("click", () => {
        uploadGameSection.classList.add("show");
        uploadGameSection.classList.remove("hide");

        gamePostedSection.classList.add("hide");
        gamePostedSection.classList.remove("show");
    });

});