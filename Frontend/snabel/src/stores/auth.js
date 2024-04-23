import {defineStore} from "pinia";
import router from "@/router";

export const useAuthenticationStore = defineStore("authenticationStore", {
    state: () => ({
        user: {},
        errorMessages: '',
        successMessages: '',
    }),

    actions: {
        async login(email, password) {
            console.log(email, password)
            try {
                const formData = new FormData();
                formData.append('email', email);
                formData.append('password', password);

                let response = await fetch(`http://localhost:8000/api/login/`, {
                    method: "POST",
                    body: formData
                });

                if (response.ok) {
                    const userData = await response.json();
                    this.user = userData;
                    localStorage.setItem('token', userData.token);
                    // set user data in session
                    var expirationTime = new Date().getTime() + (60 * 60 * 1000); // 1 hour in milliseconds
                    var userDataWithExpiration = {
                        user: userData.user,
                        expiration: expirationTime
                    };
                    var userDataJSON = JSON.stringify(userDataWithExpiration);
                    sessionStorage.setItem('user', userDataJSON);

                    this.successMessages = userData.message;
                    this.errorMessages = '';
                    router.push('/profile');
                } else {
                    this.errorMessages = "Login Failed, error in email or password!"
                    console.error("Login failed:", response.status, response.statusText);
                }
            } catch (error) {
                console.error("Error during login:", error);
                this.errorMessages = error;
                this.successMessages = '';
            }
        },


        logout() {
            localStorage.removeItem('token');
            this.user = {};
        }
    },
});
