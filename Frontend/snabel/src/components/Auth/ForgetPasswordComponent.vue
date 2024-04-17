<template>
  <div class="row justify-content-center align-items-center auth-page py-4 vh-100">
    <div class="col-md-10 col-lg-8 col-xl-6">
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

      <div class="card m-2 p-4 shadow-lg text-black h-75 w-7">
        <div class="card-body p-2">
          <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Forget Password</p>
          <form class="mx-1 mx-md-4" @submit.prevent="sendResetPassword">
            <div class="row">
              <div class="col">
                <div class="form-floating mb-3 position-relative">
                  <input v-model="email" aria-describedby="email" aria-label="email"
                         class="form-control border-0 border-bottom shadow" name="email"
                         placeholder="enter your email address"
                         required type="email">
                  <i class="fa-solid fa-envelope icon position-absolute"></i>
                  <label for="email">Email</label>
                </div>
              </div>
            </div>
            <p class="text-muted my-3">Enter your email address and we'll send you instructions to reset your password
              <span class="text-success">or</span> Return To
              <router-link to="/login">Sign In</router-link>
            </p>
            <div class="d-flex justify-content-center mx-4 my-3 mb-lg-4">
              <button class="btn btn-lg" type="submit">Request password reset</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "ResetPasswordComponent",
  data: () => ({
    email: '',
    errorMessages: {},
    successMessages: '',
  }),

  methods: {
    scrollToTop() {
      window.scrollTo({top: 0, behavior: 'smooth'});
    },

    sendResetPassword() {
      axios.post("http://127.0.0.1:8000/api/forget_password/", {email: this.email}, {
        headers: {
          'Content-Type': 'application/json' // Specify the content type as JSON
        }
      })
          .then(response => {
            console.log('Reset Password Sent Successful:', response.data);
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
    }
  }
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