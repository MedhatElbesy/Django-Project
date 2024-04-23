import {defineStore} from "pinia";
import router from "@/router";
import axios from "axios";

export const useAuthenticationStore = defineStore("authenticationStore", {
    state: () => ({
        user: {
          profile_image: '',
          first_name: '',
          last_name: '',
          email: '',
          mobile_phone: '',
          password1: '',
          password2: '',
        },
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
                    // set user data in session
                    var expirationTime = new Date().getTime() + (60 * 60 * 1000); // 1 hour in milliseconds
                    var userDataWithExpiration = {
                        user: userData.user,
                        token: userData.token,
                        expiration: expirationTime
                    };
                    var userDataJSON = JSON.stringify(userDataWithExpiration);
                    sessionStorage.setItem('user', userDataJSON);

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
            sessionStorage.removeItem("user")
            sessionStorage.clear();
            this.user = {};
            router.push({name: 'about'});
        },

        scrollToTop() {
          window.scrollTo({top: 0, behavior: 'smooth'});
        },

        updateUserDataInSessionStorage(user) {
          var userDataJSON = sessionStorage.getItem('user');

          var userDataWithExpiration = JSON.parse(userDataJSON);

          userDataWithExpiration.user = user;

          var updatedUserDataJSON = JSON.stringify(userDataWithExpiration);

          sessionStorage.setItem('user', updatedUserDataJSON);
        },

        updateProfile() {
          const token = localStorage.getItem('token');
          axios.post('http://localhost:8000/api/update_profile/', this.user, {
            headers: {
              'Content-Type': 'multipart/form-data',
              'Authorization': `Bearer ${token}`
            }
          })
              .then(response => {
                console.log('Profile Updated successful:', response.data);
                this.user = response.data.user;
                this.updateUserDataInSessionStorage(this.user);
                this.successMessages = response.data.message;
                this.errorMessages = {};
                this.scrollToTop();
              })
              .catch(error => {
                if (error.response && error.response.data) {
                  const responseData = error.response.data;
                  if (responseData && typeof responseData === 'object') {
                    this.errorMessages = responseData;
                    this.scrollToTop();
                  } else {
                    this.errorMessages = {};
                    console.error('Invalid error response:', responseData);
                  }
                } else if (error.request) {
                  console.error('No response received:', error.request);
                } else {
                  console.error('Error:', error.message);
                }
              });
        },

        getProfileImageUrl(profile_image) {
          return `http://localhost:8000/${profile_image}`
        },
    },
});
