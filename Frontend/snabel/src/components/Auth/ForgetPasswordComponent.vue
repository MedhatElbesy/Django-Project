<template>
  <div class="row justify-content-center align-items-center auth-page py-4 vh-100">
    <div class="col-md-10 col-lg-8 col-xl-6">
      <div class="card m-2 p-4 shadow-lg text-black h-75 w-7">
        <div class="card-body p-2">
          <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Forget Password</p>
          <form class="mx-1 mx-md-4">
            <div class="row">
              <div class="col">
                <div class="form-floating mb-3 position-relative">
                  <input v-model="user.email" aria-describedby="email" aria-label="email"
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
              <button class="btn btn-lg" type="button">Request password reset</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import {useAuthenticationStore} from "../../stores/auth";

export default {
  name: "ResetPasswordComponent",
  data: () => ({
    authenticationStore: useAuthenticationStore(),
    user: {
      username: '',
      password: '',
    },

    errorMessages: {},
    successMessages: '',
  })
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