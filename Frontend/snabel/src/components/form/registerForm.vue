<template>
  <form class="w-75 m-auto mt-5" enctype="multipart/form-data" @submit.prevent="registerUser">
    <div class="message">
      <!-- Start Messages -->
      <div v-if="successMessages" class="alert alert-success alert-dismissible fade show position-absolute top-0 start-50 translate-middle-x p-2" role="alert">
          <strong class="mb-0">{{ successMessages }}</strong>
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close" style="height: auto;"></button>
      </div>
      <div v-for="(messages, field) in errorMessages" :key="field" class="alert alert-danger alert-dismissible fade show position-absolute top-0 start-50 translate-middle-x p-2" role="alert">
        <ul class="mb-0">
          <li class="p-0 bullet-list" v-for="message in messages" :key="message">{{ message }}</li>
        </ul>
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close" style="height: auto;"></button>
      </div>
      <!-- End Of Messages -->
    </div>
    <p class="sign color mb-5">Already have an account? <router-link :to="{name: 'Login'}" class="text-color text-decoration-underline">Sign In</router-link></p>
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
                  type="text" autofocus>
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
    <div class="form-floating position-relative mb-3 ">
      <input v-model="user.username" aria-describedby="username" aria-label="username"
              class="form-control border-0 border-bottom shadow" name="username"
              placeholder="enter your first name"
              required type="text">
      <i class="fa-solid fa-user icon position-absolute"></i>
      <label for="username">Username</label>
    </div>
    <div class="form-floating position-relative mb-3 ">
      <input v-model="user.email" aria-describedby="email" aria-label="email"
              class="form-control border-0 border-bottom shadow" name="email"
              placeholder="enter your email" required
              type="email">
      <i class="fa-solid fa-envelope icon position-absolute"></i>
      <label for="email">Email</label>
    </div>
    <div class="form-floating position-relative mb-3 ">
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
    <div class="form-floating position-relative mb-3 ">
      <input v-model="user.password1" aria-describedby="password" aria-label="password1"
              class="form-control border-0 border-bottom shadow" name="password1"
              placeholder="enter your password"
              required type="password">
      <i id="togglePassword1"
          :class="password1Visible ? 'fas fa-eye icon' : 'fas fa-eye-slash icon'" class="position-absolute"
          @click="togglePassword1Visibility"></i>
      <label for="password">Password</label>
    </div>
    <div class="form-floating position-relative mb-3 ">
      <input v-model="user.password2" aria-describedby="password" aria-label="password"
              class="form-control border-0 border-bottom shadow" name="password2"
              placeholder="enter your password"
              required type="password">
      <i id="togglePassword2"
          :class="password2Visible ? 'fas fa-eye icon' : 'fas fa-eye-slash icon'"  class="position-absolute"
          @click="togglePassword2Visibility"></i>
      <label for="password2">Password Confirmation</label>
    </div>
    <div class="social w-100 m-auto text-center mt-5">
      <p class="text-color fw-bold position-relative">or</p>
      <ul class="social-platforms d-flex flex-wrap justify-content-evenly m-0 p-0">
        <li class="col-12 mb-3 col-md-6">
          <a href="https://google.com" title="google">
            <i class="fa-brands fa-google"></i>
            <span>Sign Up With Google</span>
          </a>
        </li>
        <li class="col-12 mb-3 col-md-6">
          <a href="https://facebook.com" title="Facebook">
            <i class="fa-brands fa-facebook-f"></i>
            <span>Sign Up With Facebook</span>
          </a>
        </li>
      </ul>
    </div>
    <div class="submit text-center col-lg-8 transition">
      <p class="terms text-color w-100">By clicking the Sign Up button below, you agree to the Snabel Terms of Service and acknowledge the Privacy Notice.</p>
      <button class="btn btn-secondary text-light fw-bold px-3 mx-5" type="submit">Sign Up</button>
    </div>
  </form>
</template>

<script>
import axios from 'axios';

export default {
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

</style>