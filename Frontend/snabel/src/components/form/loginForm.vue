<template>
    <form class="w-75 m-auto mt-5" @submit.prevent="authenticationStore.login(user.email, user.password)">
      <div class="row g-0 message">
        <!-- Start Messages -->
        <div v-if="authenticationStore.successMessages" class="alert alert-success alert-dismissible fade show position-absolute top-0 start-50 translate-middle-x p-2" role="alert">
            <strong class="ms-4">{{ authenticationStore.successMessages }}</strong>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close" style="height: auto;"></button>
          </div>
          <div v-if="authenticationStore.errorMessages" class="alert alert-danger alert-dismissible fade show position-absolute top-0 start-50 translate-middle-x p-2" role="alert">
            <strong class="ms-4">{{ authenticationStore.errorMessages }}</strong>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close" style="height: auto;"></button>
          </div>
          <!-- End Of Messages -->
      </div>
      <div>
        <p class="sign color mb-5">Don't have an account? <router-link :to="{name: 'register'}" class="text-color text-decoration-underline">Sign Up</router-link></p>
        <p>Sign in to <strong class="color">Snabel</strong></p>
        <div class="form-floating mb-3 position-relative">
          <input v-model="user.email" aria-describedby="email"
                  aria-label="email" class="form-control border-0 border-bottom shadow"
                  name="email" placeholder="enter your first name"
                  required autofocus type="text">
          <i class="fa-solid fa-user icon position-absolute"></i>
          <label for="email">Email</label>
        </div>

        <div class="form-floating position-relative mb-3 ">
        <input v-model="user.password" aria-describedby="password" aria-label="password"
            class="form-control border-0 border-bottom shadow" name="password"
            placeholder="enter your password"
                required type="password">
        <i id="togglePassword1" :class="passwordVisible ? 'fas fa-eye icon' : 'fas fa-eye-slash icon'" class="position-absolute" @click="togglePasswordVisibility"></i>
        <label for="password">Password</label>
      </div>
        <router-link :to="{name: 'forgetPassword'}" class="text-color text-decoration-underline">Forgot your password?</router-link>
      </div>
      <div class="social w-100 m-auto text-center mt-5">
        <p class="text-color fw-bold position-relative">or</p>
        <ul class="social-platforms d-flex flex-wrap justify-content-evenly m-0 p-0">
          <li class="col-12 mb-3 col-md-6">
            <a href="https://google.com" title="google">
              <i class="fa-brands fa-google"></i>
              <span>Sign In With Google</span>
            </a>
          </li>
          <li class="col-12 mb-3 col-md-6">
            <a href="https://facebook.com" title="Facebook">
              <i class="fa-brands fa-facebook-f"></i>
              <span>Sign In With Facebook</span>
            </a>
          </li>
        </ul>
      </div>
      <div class="submit text-center col-lg-8">
        <p class="terms text-color w-100">By clicking the Log In button below, you agree to the Snabel Terms of Service and acknowledge the Privacy Notice.</p>
        <button class="btn btn-secondary text-light fw-bold px-3 mx-5" type="submit">Log In</button>
      </div>
    </form>
  <!-- </div> -->
</template>


<script>
  import {useAuthenticationStore} from "../../stores/auth";

  export default {
    data: () => ({
      authenticationStore: useAuthenticationStore(),
      user: {
        email: '',
        password: '',
      },
      passwordVisible: false,
    }),

    methods: {
        togglePasswordVisibility() {
        this.passwordVisible = !this.passwordVisible;
        const passwordInput = document.querySelector('input[name="password"]');
        if (passwordInput) {
          passwordInput.type = this.passwordVisible ? 'text' : 'password';
        }
      },
    }
}
</script>

<style scoped>
  
</style>