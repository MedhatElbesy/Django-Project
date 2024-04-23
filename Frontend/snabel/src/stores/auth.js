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
                    localStorage.setItem('token', userData.token);
                    this.user = JSON.stringify(userData)
                    sessionStorage.setItem('user', this.user);
                    this.successMessages = userData.message;
                    this.errorMessages = '';
                    router.push({name: 'home'});
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
            sessionStorage.clear();
            this.user = {};
            router.push({name: 'about'});
        }
    },
});
