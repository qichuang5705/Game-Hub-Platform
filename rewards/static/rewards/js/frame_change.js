document.addEventListener("DOMContentLoaded", function () {
    const avatar = document.querySelector(".avatar-content ");
    const chat = document.querySelector(".chat-content");

    const chatShow = document.querySelector(".avatar_tab .tab_chat");
    chatShow.addEventListener("click", () => {
        avatar.classList.add("hide");
        avatar.classList.remove("show");
        chat.classList.add("show");
        chat.classList.remove("hide");
    });

    const avatarShow = document.querySelector(".chat_tab .tab_avatar");
    avatarShow.addEventListener("click", () => {
        chat.classList.add("hide");
        chat.classList.remove("show");
        avatar.classList.add("show");
        avatar.classList.remove("hide");
    });
});
