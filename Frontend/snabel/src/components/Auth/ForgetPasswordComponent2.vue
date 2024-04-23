<template>
  <div class="row g-0 auth-page bg-light vh-100">
    <article class="col-12 col-lg-4 p-lg-5 p-3 transition">
      <figure class="mb-lg-5 mb-3">
        <router-link :to="{name: 'home'}"><img src="../../assets/logo.png" width="50px" alt="Snabel Logo"></router-link>
      </figure>
      <div class="welcome">
        <h3 class="text-color">Let's Find Your <strong class="color">Snabel</strong> Account</h3>
      </div>
    </article>
    <article class="reset d-flex flex-wrap align-content-center shadow col-12 col-lg-8 transition">
      <form class="w-75 m-auto mt-5">
        <p class="signup color mb-5">Don't have an account? <router-link :to="{name: 'Register'}" class="text-color text-decoration-underline">Sign Up</router-link></p>
        <div class="form-floating mb-3 position-relative">
          <input v-model="user.email" aria-describedby="email" aria-label="email"
                  class="form-control border-0 border-bottom shadow" name="email"
                  placeholder="enter your email address"
                  required type="email">
          <i class="fa-solid fa-envelope icon position-absolute"></i>
          <label for="email">Email</label>
        </div>
        <p class="request text-color mb-5">Enter your email address and we'll send you instructions to reset your password</p>
        <div class="submit col-lg-8 col-12 transition">
          <router-link :to="{name: 'login'}" class="fw-bold text-color"><i class="fa-solid fa-angle-left"></i> Return To Sign In</router-link>
          <button class="btn btn-secondary text-light fw-bold px-3 mx-5" type="submit">Request Password Reset</button>
        </div>
      </form>
    </article>
  </div>
</template>
<script>
  import {useAuthenticationStore} from "../../stores/auth";
  export default {
    name: "LoginComponent",
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
  .welcome {
    padding-top: 28px;
  }
  h3 {
    margin-bottom: 24px;
  }
  .reset {
    border-top-left-radius: 52px;
    background-color: #FFF;
    position: relative;
  }
  .signup {
    text-align: right;
  }
  .submit {
    border-top: 1px solid #e2e2e2;
    bottom: 0;
    right: 0;
    /* width: 100%; */
    position: fixed;
    padding: 50px 25px;
    display: flex;
    align-items: center;
    justify-content: flex-end;
  }
  .submit a {
    border: 1px solid #8d8d8d31;
    padding: 6px 16px;
    border-radius: 8px;
    transition: .5s;
  }
  .submit a:hover {
    border: 1px solid rgb(141, 141, 141);
    background-color: #b9b7b72a;;
    color: var(--mainTextColor);
  }
  .submit a i {
    padding-right: 16px;
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

  @media screen and (max-width: 992px) {
    .reset {
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
      flex-wrap: wrap;
      text-align: center;
    }
    .submit a,
    .submit button {
      display: inline-block;
      width: 70%;
      margin-bottom: 12px;
    }
  }
</style>