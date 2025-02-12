document.addEventListener("DOMContentLoaded", () => {
    const loginSection = document.querySelector(".login");
    const registerSection = document.querySelector(".register");
    const forgotPasswordSection = document.querySelector(".forgot_password");
    const pageAccountSection = document.querySelector(".page_account");
    const adminSection = document.querySelector(".admin");
    const resetPasswordSection = document.querySelector(".reset_password");
    const accountSection = document.querySelector(".account-wrapper");
    const avatar = document.querySelector(".avatar-wrapper");
    const userAccount = document.querySelector(".page_home_user");
    const guestAccount = document.querySelector(".page_home");
    const cartShow = document.querySelector(".page_home .cart");

    const createNewAccountButton = document.querySelector(".login_footer span:last-child");
    const createButton = document.querySelector(".register_footer .create-account-btn");
    const loginButtonFromRegister = document.querySelector(".register_footer .login-btn");
    const loginButtonFromForgot = document.querySelector(".forgot_password_footer .login-btn");
    const forgotPasswordButton = document.querySelector(".login_footer .forgot-password-btn");
    const createButtonFromForgot = document.querySelector(".forgot_password_footer .create-account-btn");
    const resetPasswordFromForgot = document.querySelector(".forgot_password_footer .send-code-btn");
    const loginFromReset = document.querySelector(".reset_password_footer .reset_password-btn");

    const openLoginPage = document.querySelector(".open-login-btn");
    const openAdminPage = document.querySelector(".open-admin-btn");
    const openChangePasswordPage = document.querySelector(".open-change-password-btn");
    
    const closeLogin = document.querySelector(".close-login");
    const closeRegister = document.querySelector(".close-register");
    const closeForgotPassword = document.querySelector(".close-forgot_password");
    const closeAdmin = document.querySelector(".close-admin");
    const closeResetPassword = document.querySelector(".close-reset_password");

    const openAccount = document.querySelector(".avatar-wrapper");
    const closeAccount = document.querySelector(".close-account");

    const loginToUser = document.querySelector(".login_footer .btn-login");
    const logoutToGuest = document.querySelector(".logout-account-btn");

    const opencartShow = document.querySelector(".cart-btn");

    //
    opencartShow.addEventListener("click", () => {
        if (cartShow.classList.contains("open")) {
            cartShow.classList.remove("open");
            cartShow.classList.add("close");
        } else {
            cartShow.classList.remove("close");
            cartShow.classList.add("open");
        }
    });

    //Login --> User Page
    loginToUser.addEventListener("click", () => {
        loginSection.classList.add("hide");
        loginSection.classList.remove("show");

        pageAccountSection.classList.add("hide");
        pageAccountSection.classList.remove("show");

        guestAccount.classList.remove("exist");
        guestAccount.classList.add("alternative");

        setTimeout(() => {
            userAccount.classList.add("exist");
            userAccount.classList.remove("alternative");
        }, 100);
    });

    //Usser Logout -> Guest
    logoutToGuest.addEventListener("click", () => {
        userAccount.classList.add("alternative");
        userAccount.classList.remove("exist");

        accountSection.classList.add("hide");
        accountSection.classList.remove("show");

        avatar.classList.add("close");
        avatar.classList.remove("open");

        setTimeout(() => {
            guestAccount.classList.remove("hide");
            guestAccount.classList.add("exist");
            guestAccount.classList.remove("alternative");
        }, 100);
    });


    //Show Account
    openAccount.addEventListener("click", () => {

        setTimeout(() => {
            avatar.classList.add("open");
            avatar.classList.remove("close");
            accountSection.classList.add("show");
            accountSection.classList.remove("hide");
        }, 150);
    });

    //Close Account
    closeAccount.addEventListener("click", () => {

        setTimeout(() => {
            avatar.classList.add("close");
            avatar.classList.remove("open");
            accountSection.classList.add("hide");
            accountSection.classList.remove("show");
        }, 200);
    });

    // Show Login
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

    // Show Admin
    openAdminPage.addEventListener("click", () => {
        pageAccountSection.classList.add("show");
        pageAccountSection.classList.remove("hide");

        cartShow.classList.add("close");
        cartShow.classList.remove("open");
        
        setTimeout(() => {
            adminSection.classList.add("show");
            adminSection.classList.remove("hide");
        }, 100);
    });

    // Account --> Fogot Password
    openChangePasswordPage.addEventListener("click", () => {
        pageAccountSection.classList.add("show");
        pageAccountSection.classList.remove("hide");

        setTimeout(() => {
            forgotPasswordSection.classList.add("show");
            forgotPasswordSection.classList.remove("hide");
        }, 100);
    });

    // Close Login
    closeLogin.addEventListener("click", () => {
        loginSection.classList.add("hide");
        loginSection.classList.remove("show");

        pageAccountSection.classList.add("hide");
        pageAccountSection.classList.remove("show");
    });

    // Close Register
    closeRegister.addEventListener("click", () => {
        registerSection.classList.add("hide");
        registerSection.classList.remove("show");

        pageAccountSection.classList.add("hide");
        pageAccountSection.classList.remove("show");
    });

    // Close Forgot Password
    closeForgotPassword.addEventListener("click", () => {
        forgotPasswordSection.classList.add("hide");
        forgotPasswordSection.classList.remove("show");

        pageAccountSection.classList.add("hide");
        pageAccountSection.classList.remove("show");
    });

    // Close Reset Password
    closeResetPassword.addEventListener("click", () => {
        resetPasswordSection.classList.add("hide");
        resetPasswordSection.classList.remove("show");

        pageAccountSection.classList.add("hide");
        pageAccountSection.classList.remove("show");
    });

    // Close Admin
    closeAdmin.addEventListener("click", () => {
        adminSection.classList.add("hide");
        adminSection.classList.remove("show");

        pageAccountSection.classList.add("hide");
        pageAccountSection.classList.remove("show");
    });
    
    // Login -> Register
    createNewAccountButton.addEventListener("click", () => {
        loginSection.classList.add("hide");
        loginSection.classList.remove("show");
        setTimeout(() => {
            registerSection.classList.add("show");
            registerSection.classList.remove("hide");
        }, 100);
    });

    // Register -> Login
    createButton.addEventListener("click", () => {
        registerSection.classList.add("hide");
        registerSection.classList.remove("show");
        setTimeout(() => {
            loginSection.classList.add("show");
            loginSection.classList.remove("hide");
        }, 100);
    });

    // Forgot Password -> Login
    loginButtonFromForgot.addEventListener("click", () => {
        if (avatar.classList.contains("hide"))
        {
            forgotPasswordSection.classList.add("hide");
            forgotPasswordSection.classList.remove("show");
            setTimeout(() => {
                loginSection.classList.add("show");
                loginSection.classList.remove("hide");
            }, 100);
        }
    });

    // Login -> Forgot Password
    forgotPasswordButton.addEventListener("click", () => {
        loginSection.classList.add("hide");
        loginSection.classList.remove("show");
        setTimeout(() => {
            forgotPasswordSection.classList.add("show");
            forgotPasswordSection.classList.remove("hide");
        }, 100);
    });

    // Forgot Password -> Register
    createButtonFromForgot.addEventListener("click", () => {
        if (avatar.classList.contains("hide"))
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
    loginButtonFromRegister.addEventListener("click", () => {
        registerSection.classList.add("hide");
        registerSection.classList.remove("show");

        setTimeout(() => {
            loginSection.classList.add("show");
            loginSection.classList.remove("hide");
        }, 100);
    });

    // Forgot Password -> Reset Password
    resetPasswordFromForgot.addEventListener("click", () => {
        forgotPasswordSection.classList.add("hide");
        forgotPasswordSection.classList.remove("show");
        setTimeout(() => {
            resetPasswordSection.classList.add("show");
            resetPasswordSection.classList.remove("hide");
        }, 100);
    });

    // Reset Password -> Login
    loginFromReset.addEventListener("click", () => {
        if (avatar.classList.contains("open"))
        {
            resetPasswordSection.classList.add("hide");
            resetPasswordSection.classList.remove("show");

            pageAccountSection.classList.add("hide");
            pageAccountSection.classList.remove("show");
        } else
        {
            resetPasswordSection.classList.add("hide");
            resetPasswordSection.classList.remove("show");
            setTimeout(() => {
                loginSection.classList.add("show");
                loginSection.classList.remove("hide");
            }, 100);
        }
    });


});

