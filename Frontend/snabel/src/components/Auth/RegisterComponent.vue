<template>
    <div class="row justify-content-center align-items-center m-0 auth-page">
      <div class="col-lg-6 col-xl-6">
        <div class="card m-2 border-0 text-black h-75 bg-transparent">
          <div class="card-body p-4">
            <h1 class="card-title text-center text-light fw-bold mb-3">
              Create an account
            </h1>
            <div class="row justify-content-center align-items-center">
              <!-- Start Messages -->
              <div v-if="successMessages" class="alert alert-success alert-dismissible fade show" role="alert">
                <strong>{{ successMessages }}</strong>
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
              </div>
              <div v-for="(messages, field) in errorMessages" :key="field" class="alert alert-danger alert-dismissible fade show" role="alert">
                <ul>
                  <li v-for="message in messages" :key="message">{{ message }}</li>
                </ul>
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
              </div>
              <!-- End Of Messages -->

              <!-- Form Here-->
              <form class="mx-1 mx-md-4" enctype="multipart/form-data" @submit.prevent="registerUser">
                <div class="mb-3 text-center">
                  <div id="image_preview"
                       class="bg-light border position-relative border-1 d-inline-block text-center rounded rounded-circle position-relative overflow-hidden"
                       @click="triggerFileInput">
                    <img alt="Current Image" class="rounded rounded-circle"
                         height="100"
                         src="https://thumbs.dreamstime.com/b/default-avatar-profile-icon-vector-social-media-user-image-182145777.jpg">
                    <i class="fas fa-camera position-absolute" style="bottom: 15px; right: 8px;"></i>
                  </div>
                  <input id="image_input" accept="image/*" name="profile_image"
                         style="display: none;"
                         type="file" @change="handleFileChange">
                </div>

                <div class="row">
                  <div class="col-12 col-sm-6">
                    <div class="form-floating mb-3">
                      <input id="first_name" v-model="user.first_name"
                             class="form-control  border-0 border-bottom shadow"
                             name="first_name" placeholder="name@example.com"
                             type="text">
                      <label for="first_name">First Name</label>
                    </div>
                  </div>
                  <div class="col-12 col-sm-6">
                    <div class="form-floating mb-3">
                      <input id="last_name" v-model="user.last_name" class="form-control  border-0 border-bottom shadow"
                             name="last_name" placeholder="name@example.com"
                             type="text">
                      <label for="last_name">Last Name</label>
                    </div>
                  </div>
                </div>

                <div class="row">
                  <div class="col mb-3">
                    <div class="form-floating position-relative">
                      <input v-model="user.username" aria-describedby="username" aria-label="username"
                             class="form-control border-0 border-bottom shadow" name="username"
                             placeholder="enter your first name"
                             required type="text">
                      <i class="fa-solid fa-user icon position-absolute"></i>
                      <label for="username">Username</label>
                    </div>
                  </div>
                </div>

                <div class="row">
                  <div class="col mb-3">
                    <div class="form-floating position-relative">
                      <input v-model="user.email" aria-describedby="email" aria-label="email"
                             class="form-control border-0 border-bottom shadow" name="email"
                             placeholder="enter your email" required
                             type="email">
                      <i class="fa-solid fa-envelope icon position-absolute"></i>
                      <label for="email">Email</label>
                    </div>
                  </div>
                </div>

                <div class="row">
                  <div class="col mb-3">
                    <div class="form-floating position-relative">
                      <input v-model="user.mobile_phone" aria-describedby="mobile_phone" aria-label="mobile_phone"
                             class="form-control border-0 border-bottom shadow" name="mobile_phone"
                             placeholder="enter your first name"
                             required type="text">
                      <i class="fa-solid fa-mobile icon position-absolute"></i>
                      <label for="mobile_phone">Mobile Phone</label>
                    </div>
                    <!--<div v-if="errorMessages.mobile_phone" class="text-danger" >
                      <ul>
                        <li v-for="message in errorMessages.mobile_phone" :key="message">{{ message }}</li>
                      </ul>
                    </div> -->
                  </div>
                </div>

                <div class="row">
                  <div class="col mb-3">
                    <div class="form-floating position-relative">
                      <input v-model="user.password1" aria-describedby="password" aria-label="password1"
                             class="form-control border-0 border-bottom shadow" name="password1"
                             placeholder="enter your password"
                             required type="password">
                      <i id="togglePassword1"
                         :class="password1Visible ? 'fas fa-eye icon position-absolute' : 'fas fa-eye-slash icon position-absolute'"
                         @click="togglePassword1Visibility"></i>
                      <label for="password">Password</label>
                    </div>
                  </div>
                </div>

                <div class="row">
                  <div class="col mb-3">
                    <div class="form-floating position-relative">
                      <input v-model="user.password2" aria-describedby="password" aria-label="password"
                             class="form-control border-0 border-bottom shadow" name="password2"
                             placeholder="enter your password"
                             required type="password">
                      <i id="togglePassword2"
                         :class="password2Visible ? 'fas fa-eye icon position-absolute' : 'fas fa-eye-slash icon position-absolute'"
                         @click="togglePassword2Visibility"></i>
                      <label for="password2">Password Confirmation</label>
                    </div>
                  </div>
                </div>

                <div class="d-flex justify-content-center mx-4 mb-3 mb-lg-4">
                  <button class="btn btn-lg rounded auth-button" type="submit">Sign In</button>
                </div>
              </form>
            </div>
            <p class="text-center text-light">Already have an account? <router-link to="/login">Sign In</router-link></p>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "RegisterComponent",

  data: () => ({
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

    password1Visible: false,
    password2Visible: false,

    errorMessages: {},
    successMessages: '',
  }),

  methods: {
    scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    },

    registerUser() {
      axios.post('http://localhost:8000/api/register/', this.user, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
          .then(response => {
            console.log('Registration successful:', response.data);
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

    togglePassword1Visibility() {
      this.password1Visible = !this.password1Visible;
      const passwordInput = document.querySelector('input[name="password1"]');
      if (passwordInput) {
        passwordInput.type = this.password1Visible ? 'text' : 'password';
      }
    },

    togglePassword2Visibility() {
      this.password2Visible = !this.password2Visible;
      const passwordInput = document.querySelector('input[name="password2"]');
      if (passwordInput) {
        passwordInput.type = this.password2Visible ? 'text' : 'password';
      }
    },

    triggerFileInput() {
      const fileInput = document.getElementById('image_input');
      fileInput.click(); // Simulate click on file input
    },

    handleFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        this.user.profile_image = file;
        const reader = new FileReader();
        reader.onload = () => {
          const output = document.getElementById('image_preview');
          output.innerHTML = `<img src="${reader.result}" alt="New Image" height="100">`;
        };
        reader.readAsDataURL(file);
      }
    }
  },
}
</script>

<style scoped>
.auth-page {
  background-image: url('@/assets/bg.jpg');
  background-size: cover;
  background-position: center;
}

.auth-button {
  background: #a8ff78; /* fallback for old browsers */
  background: -webkit-linear-gradient(to right, #78ffd6, #a8ff78); /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to right, #78ffd6, #a8ff78); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

}

.icon {
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
}
</style>