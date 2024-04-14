<template>
  <div class="container-fluid auth-page py-4 vh-100">
    <div class="row justify-content-center align-items-center">
      <div class="col-md-10 col-lg-8 col-xl-6">
        <div class="card m-2 p-4 shadow-lg text-black h-75 w-7">
          <div class="card-body p-2">
            <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Reset Password</p>
            <form class="mx-1 mx-md-4">
              <div class="row">
                <div class="col">
                  <div class="form-floating mb-3 position-relative">
                    <input v-model="user.password1" aria-describedby="password"
                           aria-label="password" class="form-control border-0 border-bottom shadow"
                           name="password" placeholder="enter your password"
                           required type="password">
                    <i id="togglePassword" class="fas fa-eye-slash icon position-absolute"></i>
                    <label for="password">Password</label>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col">
                  <div class="form-floating mb-3 position-relative">
                    <input v-model="user.password1" aria-describedby="password"
                           aria-label="password" class="form-control border-0 border-bottom shadow"
                           name="password" placeholder="enter your password"
                           required type="password">
                    <i id="togglePassword" class="fas fa-eye-slash icon position-absolute"></i>
                    <label for="password">Password</label>
                  </div>
                </div>
              </div>
              <div class="d-flex justify-content-center mx-4 my-3 mb-lg-4">
                <button class="btn btn-lg" type="button">Reset Password</button>
              </div>
              <p class="text-center">Return To <router-link to="/login">Sign In</router-link></p>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import {useAuthenticationStore} from "../../stores/auth";

export default {
  name: "ForgetPasswordComponent",
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