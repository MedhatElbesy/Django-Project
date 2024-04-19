<template>
  <div class="row g-0 auth-page bg-light position-relative">
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
    <article class="col-lg-4  p-lg-5 p-3">
      <figure class="mb-lg-5 mb-3">
        <router-link to="/"><img src="../../assets/logo.png" width="50px" alt="Snabel Logo"></router-link>
      </figure>
      <div class="welcome">
        <span class="text-color">Welcome To Snable</span>
        <h3 class="color">Always Remember: </h3>
        <p class="ayat"><strong lang="ar" title="Never will you attain the good [reward] until you spend [in the way of Allah] from that which you love. And whatever you spend - indeed, Allah is Knowing of it.">لَن تَنَالُوا الْبِرَّ حَتَّىٰ تُنفِقُوا مِمَّا تُحِبُّونَ ۚ
          <br>وَمَا تُنفِقُوا مِن شَيْءٍ فَإِنَّ اللَّهَ بِهِ عَلِيمٌ<br></strong>
          <em class="text-color">Surah Al Imran: 92</em>
        </p>
      </div>
    </article>
    <article class="login d-flex flex-wrap align-content-center shadow col-lg-8">
      <form class="w-75 m-auto mt-5" enctype="multipart/form-data" @submit.prevent="registerUser">
        <p class="signin color mb-5">Already have an account? <router-link to="/login" class="text-color text-decoration-underline">Log In</router-link></p>
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
        <div class="submit text-center col-lg-8">
          <p class="terms text-color w-100">By clicking the Sign Up button below, you agree to the Snabel Terms of Service and acknowledge the Privacy Notice.</p>
          <button class="btn btn-secondary text-light fw-bold px-3 mx-5" type="submit">Sign Up</button>
        </div>
      </form>
    </article>
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
  .bullet-list {
      list-style-type: disc;
      margin-left: 20px;
  }

  .bullet-list li {
      margin-left: 10px;
  }
  .welcome {
    padding-top: 28px;
  }
  h3 {
    margin-bottom: 24px;
  }
  .ayat {
    text-align: center;
    direction: rtl;
    padding-bottom: 40px;
    font-weight: bold;
    color: var(--mainTextColor);
    letter-spacing: 2px;
    word-spacing: 3px;
    font-family: 'Reem Kufi', sans-serif;
  }
  em {
    font-size: 12px;
  }
  .login {
    border-top-left-radius: 52px;
    background-color: #FFF;
  }
  .signin {
    text-align: right;
  }
  .submit {
    position: fixed;
    right: 0;
    bottom: 0;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: flex-end;
    background-color: #FFF;
    padding: 25px;
    border-top: 1px solid #e2e2e2;
  }
  form input {
    color: var(--mainColor);
  }
  form input:focus {
    caret-color: var(--mainColor);
    color: var(--mainTextColor);
  }
  form label {
    color: var(--mainColor);
  }
  .icon {
    top: 50%;
    right: 10px;
    transform: translateY(-50%);
    color: var(--mainColor)
  }
  .social {
    padding-bottom: 150px;
  }
  .social p::before{
    content: "";
    position: absolute;
    height: 1px;
    width: 40%;
    top: 50%;
    left: 3%;
    transform: translateY(50%);
    border: 1px solid #8f8f8f48;
  }
  .social p::after{
    content: "";
    position: absolute;
    height: 1px;
    width: 40%;
    top: 50%;
    right: 3%;
    transform: translateY(50%);
    border: 1px solid #8f8f8f48;
  }
  .social-platforms a {
    color: #FFF;
    border-radius: 8px;
    display: inline-block;
  }
  .social-platforms i {
    padding: 12px;
    width: 40px;
  }
  .social-platforms span {
    padding: 12px;
    width: 200px;
    display: inline-block;
    border-radius: 8px;
  }
  .social-platforms li:first-child a {
    background-color: #C53329;
  }
  .social-platforms li:first-child span {
    background-color: #F44235;
    border-left: 1px solid #e76464;
  }
  .social-platforms li:last-child a {
    background-color: #3A5998;
  }
  .social-platforms li:last-child span {
    background-color: #243B68;
    border-left: 1px solid #4666a7;
  }

  @media screen and (max-width: 992px) {
    .login {
      border-top-right-radius: 52px;
    }
  }
  @media screen and (max-width: 576px) {
    form {
      width: 100% !important;
      padding-right: 16px;
      padding-left: 16px;
    }
    .submit {
      position: static;
      justify-content: center;
    }
    .social {
      padding-bottom: 0;
    }
  }
</style>