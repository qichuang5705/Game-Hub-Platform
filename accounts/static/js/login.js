document.addEventListener("DOMContentLoaded", () => {
    const loginSection = document.querySelector(".login");
    const registerSection = document.querySelector(".register");
    const forgotPasswordSection = document.querySelector(".forgot_password");
    const pageAccountSection = document.querySelector(".page_account");
    const resetPasswordSection = document.querySelector(".reset_password");
    const accountSection = document.querySelector(".account-wrapper");
    const avatar = document.querySelector(".avatar-wrapper");
    const userAccount = document.querySelector(".page_home_user");
    const guestAccount = document.querySelector(".page_home");
    const cartShow = document.querySelector(".page_home .cart");
    const cartUserShow = document.querySelector(".page_home_user .cart_user");

    const loginToUser = document.querySelector(".btn-login");
    const logoutToGuest = document.querySelector(".logout-account-btn");

    

    //open user choice
    const opencartUserShow = document.querySelector(".avatar-wrapper");
    opencartUserShow.addEventListener("click", () => {
        if (cartUserShow.classList.contains("close"))
        {
            cartUserShow.classList.add("open");
            cartUserShow.classList.remove("close");
        } else {
            cartUserShow.classList.remove("open");
            cartUserShow.classList.add("close");
        }
    });

    //open guest choice
    const opencartShow = document.querySelector(".cart-btn");
    opencartShow.addEventListener("click", () => {
        if (cartShow.classList.contains("close"))
        {
            cartShow.classList.add("open");
            cartShow.classList.remove("close");
        } else {
            cartShow.classList.remove("open");
            cartShow.classList.add("close");
        }
    });

    //Show Info
    const openAccount = document.querySelector(".show-info-btn");
    openAccount.addEventListener("click", () => {
        cartUserShow.classList.add("close");
        cartUserShow.classList.remove("open");

        setTimeout(() => {
            avatar.classList.add("open");
            avatar.classList.remove("close");
            accountSection.classList.add("show");
            accountSection.classList.remove("hide");
        }, 150);
    });

    //Close Info
    const closeAccount = document.querySelector(".close-account");
    closeAccount.addEventListener("click", () => {
        avatar.classList.add("close");
        avatar.classList.remove("open");
        accountSection.classList.add("hide");
        accountSection.classList.remove("show");
    });

    // Show Login
    const openLoginPage = document.querySelector(".open-login-btn");
    openLoginPage.addEventListener("click", () => {
        pageAccountSection.classList.add("show");
        pageAccountSection.classList.remove("hide");

        cartShow.classList.add("close");
        cartShow.classList.remove("open");

        setTimeout(() => {
            loginSection.classList.add("show");
            loginSection.classList.remove("hide");
        }, 100);
    });

    // Account --> Fogot Password
    const openChangePasswordPage = document.querySelector(".open-change-password-btn");
    openChangePasswordPage.addEventListener("click", () => {
        pageAccountSection.classList.add("show");
        pageAccountSection.classList.remove("hide");

        setTimeout(() => {
            forgotPasswordSection.classList.add("show");
            forgotPasswordSection.classList.remove("hide");
        }, 100);
    });

    // Close Login
    const closeLogin = document.querySelector(".close-login");
    closeLogin.addEventListener("click", () => {
        loginSection.classList.add("hide");
        loginSection.classList.remove("show");

        pageAccountSection.classList.add("hide");
        pageAccountSection.classList.remove("show");
    });

    // Close Register
    const closeRegister = document.querySelector(".close-register");
    closeRegister.addEventListener("click", () => {
        registerSection.classList.add("hide");
        registerSection.classList.remove("show");

        pageAccountSection.classList.add("hide");
        pageAccountSection.classList.remove("show");
    });

    // Close Forgot Password
    const closeForgotPassword = document.querySelector(".close-forgot_password");
    closeForgotPassword.addEventListener("click", () => {
        forgotPasswordSection.classList.add("hide");
        forgotPasswordSection.classList.remove("show");

        pageAccountSection.classList.add("hide");
        pageAccountSection.classList.remove("show");
    });

    // Close Reset Password
    const closeResetPassword = document.querySelector(".close-reset_password");
    closeResetPassword.addEventListener("click", () => {
        resetPasswordSection.classList.add("hide");
        resetPasswordSection.classList.remove("show");

        pageAccountSection.classList.add("hide");
        pageAccountSection.classList.remove("show");
    });
    
    // Login -> Register
    const createNewAccountButton = document.querySelector(".login_footer span:last-child");
    createNewAccountButton.addEventListener("click", () => {
        loginSection.classList.add("hide");
        loginSection.classList.remove("show");
        setTimeout(() => {
            registerSection.classList.add("show");
            registerSection.classList.remove("hide");
        }, 100);
    });

    // Login -> Forgot Password
    const forgotPasswordButton = document.querySelector(".login_footer .forgot-password-btn");
    forgotPasswordButton.addEventListener("click", () => {
        loginSection.classList.add("hide");
        loginSection.classList.remove("show");
        setTimeout(() => {
            forgotPasswordSection.classList.add("show");
            forgotPasswordSection.classList.remove("hide");
        }, 100);
    });
    
    // Forgot Password -> Login
    const loginButtonFromForgot = document.querySelector(".forgot_password_footer .login-btn");
    loginButtonFromForgot.addEventListener("click", () => {
        if (userAccount.classList.contains("alternative"))
        {
            forgotPasswordSection.classList.add("hide");
            forgotPasswordSection.classList.remove("show");
            setTimeout(() => {
                loginSection.classList.add("show");
                loginSection.classList.remove("hide");
            }, 100);
        }
    });

    // Forgot Password -> Register
    const createButtonFromForgot = document.querySelector(".forgot_password_footer .create-account-btn");
    createButtonFromForgot.addEventListener("click", () => {
        if (userAccount.classList.contains("alternative"))
        {
            forgotPasswordSection.classList.add("hide");
            forgotPasswordSection.classList.remove("show");
            setTimeout(() => {
                registerSection.classList.add("show");
                registerSection.classList.remove("hide");
            }, 100);
        }
    });

    // Register -> Login
    const loginButtonFromRegister = document.querySelector(".register_footer .login-btn");
    loginButtonFromRegister.addEventListener("click", () => {
        registerSection.classList.add("hide");
        registerSection.classList.remove("show");

        setTimeout(() => {
            loginSection.classList.add("show");
            loginSection.classList.remove("hide");
        }, 100);
    });

});