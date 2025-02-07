document.addEventListener("DOMContentLoaded", () => {
    const baseSection = document.querySelector(".page_home");
    const loginSection = document.querySelector(".login");
    const registerSection = document.querySelector(".register");
    const forgotPasswordSection = document.querySelector(".forgot_password");
    const pageAccountSection = document.querySelector(".page_account");
    const adminSection = document.querySelector(".admin");
    const resetPasswordSection = document.querySelector(".reset_password");

    const createNewAccountButton = document.querySelector(".login_footer span:last-child");
    const createButton = document.querySelector(".register_footer .create-account-btn");
    const loginButtonFromRegister = document.querySelector(".register_footer .login-btn");
    const loginButtonFromForgot = document.querySelector(".forgot_password_footer .login-btn");
    const forgotPasswordButton = document.querySelector(".login_footer .forgot-password-btn");
    const createButtonFromForgot = document.querySelector(".forgot_password_footer .create-account-btn");
    const resetPasswordFromForgot = document.querySelector(".forgot_password_footer .send-code-btn");
    const loginFromReset = document.querySelector(".reset_password_footer .reset_password-btn");

    const openAccountPage = document.querySelector(".open-account-btn");
    const openAdminPage = document.querySelector(".open-admin-btn");
    const closeLogin = document.querySelector(".close-login");
    const closeRegister = document.querySelector(".close-register");
    const closeForgotPassword = document.querySelector(".close-forgot_password");
    const closeAdmin = document.querySelector(".close-admin");
    const closeResetPassword = document.querySelector(".close-reset_password");

    // Show Page Account
    openAccountPage.addEventListener("click", () => {
        pageAccountSection.classList.add("show");
        pageAccountSection.classList.remove("hide");
        baseSection.classList.add("hide");
        setTimeout(() => {
            loginSection.classList.add("show");
            loginSection.classList.remove("hide");
        }, 100);
    });

    // Show Admin
    openAdminPage.addEventListener("click", () => {
        pageAccountSection.classList.add("show");
        pageAccountSection.classList.remove("hide");
        baseSection.classList.add("hide");
        setTimeout(() => {
            adminSection.classList.add("show");
            adminSection.classList.remove("hide");
        }, 100);
    });

    // Close Login
    closeLogin.addEventListener("click", () => {
        loginSection.classList.add("hide");
        loginSection.classList.remove("show");

        pageAccountSection.classList.add("hide");
        pageAccountSection.classList.remove("show");

        baseSection.classList.remove("hide");
        baseSection.classList.add("show");
    });

    // Close Register
    closeRegister.addEventListener("click", () => {
        registerSection.classList.add("hide");
        registerSection.classList.remove("show");

        pageAccountSection.classList.add("hide");
        pageAccountSection.classList.remove("show");
        
        baseSection.classList.remove("hide");
        baseSection.classList.add("show");
    });

    // Close Forgot Password
    closeForgotPassword.addEventListener("click", () => {
        forgotPasswordSection.classList.add("hide");
        forgotPasswordSection.classList.remove("show");

        pageAccountSection.classList.add("hide");
        pageAccountSection.classList.remove("show");
        
        baseSection.classList.remove("hide");
        baseSection.classList.add("show");
    });

    // Close Reset Password
    closeResetPassword.addEventListener("click", () => {
        resetPasswordSection.classList.add("hide");
        resetPasswordSection.classList.remove("show");

        pageAccountSection.classList.add("hide");
        pageAccountSection.classList.remove("show");
        
        baseSection.classList.remove("hide");
        baseSection.classList.add("show");
    });

    // Close Admin
    closeAdmin.addEventListener("click", () => {
        adminSection.classList.add("hide");
        adminSection.classList.remove("show");

        pageAccountSection.classList.add("hide");
        pageAccountSection.classList.remove("show");
        
        baseSection.classList.remove("hide");
        baseSection.classList.add("show");
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
        forgotPasswordSection.classList.add("hide");
        forgotPasswordSection.classList.remove("show");
        setTimeout(() => {
            loginSection.classList.add("show");
            loginSection.classList.remove("hide");
        }, 100);
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
        forgotPasswordSection.classList.add("hide");
        forgotPasswordSection.classList.remove("show");
        setTimeout(() => {
            registerSection.classList.add("show");
            registerSection.classList.remove("hide");
        }, 100);
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
        resetPasswordSection.classList.add("hide");
        resetPasswordSection.classList.remove("show");
        setTimeout(() => {
            loginSection.classList.add("show");
            loginSection.classList.remove("hide");
        }, 100);
    });

    /* Login -> Base
    loginToBase.addEventListener("click", () => {
        resetPasswordSection.classList.add("hide");
        resetPasswordSection.classList.remove("show");
        setTimeout(() => {
            loginSection.classList.add("show");
            loginSection.classList.remove("hide");
        }, 100);
    });
    */

});
