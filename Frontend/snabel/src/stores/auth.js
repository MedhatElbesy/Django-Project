import { defineStore } from "pinia";

export const useAuthenticationStore = defineStore("authenticationStore", {
  state: () => ({
    isAuthenticated: false,
    user: {
      profile_image: '',
      first_name: '',
      last_name: '',
      username: '',
      email: '',
      mobile_phone: '',
      password1: '',
      password2: '',
    },
  }),

  actions: {
    async login(email, password) {
      try {
        let response = await fetch(`http://127.0.0.1:8000/api/login/`,
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ email, password }),
          }
        );

        if (response.ok) {
          const userData = await response.json();
          this.isAuthenticated = true;
          this.user = userData;
          localStorage.setItem('token', userData.token);
          console.log("Login successful:", this.user);
        } else {
          this.isAuthenticated = false;
          console.error("Login failed:", response.status, response.statusText);
        }
      } catch (error) {
        this.isAuthenticated = false;
        console.error("Error during login:", error);
      }
    },


    logout() {
      localStorage.removeItem('token');
      this.isAuthenticated = false;
      this.user = {};
    }
  },
});
