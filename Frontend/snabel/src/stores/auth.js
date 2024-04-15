import { defineStore } from "pinia";

export const useAuthenticationStore = defineStore("authenticationStore", {
  state: () => ({
    user: {},
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
          console.log("Login successful:", this.user);
        } else {
          console.error("Login failed:", response.status, response.statusText);
        }
      } catch (error) {
        console.error("Error during login:", error);
      }
    },


    logout() {
      localStorage.removeItem('token');
      this.user = {};
    }
  },
});
