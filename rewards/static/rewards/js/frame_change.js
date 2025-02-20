document.addEventListener("DOMContentLoaded", function () {
    const avatar = document.querySelector(".avatar-content ");
    const chat = document.querySelector(".chat-content");
    const avt = document.querySelector(".avt");
    const cht = document.querySelector(".cht");

    const chatShow = document.querySelector(".avatar_tab .tab_chat");
    chatShow.addEventListener("click", () => {
        avatar.classList.add("hide");
        avatar.classList.remove("show");
        avt.classList.remove("active");
        chat.classList.add("show");
        cht.classList.add("active");
        chat.classList.remove("hide");
    });

    const avatarShow = document.querySelector(".chat_tab .tab_avatar");
    avatarShow.addEventListener("click", () => {
        chat.classList.add("hide");
        chat.classList.remove("show");
        cht.classList.remove("active");
        avatar.classList.add("show");
        avt.classList.add("active");
        avatar.classList.remove("hide");
    });

});



