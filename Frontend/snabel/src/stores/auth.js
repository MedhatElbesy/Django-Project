 import { defineStore } from "pinia";

export const useAuthenticationStore = defineStore("authenticationStore", {
  state: () => ({
    user: {},
    errorMessages: '',
    successMessages: '',
    // isAuth: false,
  }),

  actions: {
    async login(username, password) {
      console.log(username,password)
      try {
        const formData = new FormData();
        formData.append('username', username);
        formData.append('password', password);

        let response = await fetch(`http://localhost:8000/api/login/`, {
          method: "POST",
          body: formData
        });

        if (response.ok) {
          const userData = await response.json();
          this.user = userData;
          localStorage.setItem('token', userData.token);
          this.successMessages = userData.message;
          this.errorMessages = '';
          // this.isAuth = true;
          console.log("Login successful:", this.user, userData.message);
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
      // this.isAuth = false;
    },
  },
});
