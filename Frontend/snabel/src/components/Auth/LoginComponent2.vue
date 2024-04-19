<template>
  <div class="auth-page row g-0  bg-light vh-100">
    <article class="col-lg-4 p-lg-5 p-3 transition">
      <figure class="mb-lg-5 mb-3">
        <router-link to="/"><img src="../../assets/logo.png" width="50px" alt="Snabel Logo"></router-link>
      </figure>
      <div class="welcome">
        <span class="text-color">Welcome Back</span>
        <h3 class="color">Don't Forget: </h3>
        <p class="ayat">
          <strong lang="ar" title="(18) Indeed, the men who practice charity and the women who practice charity and [they who] have loaned Allāh a goodly loan - it will be multiplied for them, and they will have a noble reward. ">إِنَّ الْمُصَّدِّقِينَ وَالْمُصَّدِّقَاتِ وَأَقْرَضُوا اللَّـهَ قَرْضًا حَسَنًا يُضَاعَفُ لَهُمْ وَلَهُمْ أَجْرٌ كَرِيمٌ
          <br>
          </strong>
          <em class="text-color">Surah Al-Hadīd: 18</em>
        </p>
      </div>
    </article>
    <article class="login d-flex flex-wrap align-content-center transition shadow col-lg-8">
      <form class="w-75 m-auto mt-5" @submit.prevent="authenticationStore.login(user.username, user.password)">
        <div>
          <p class="signup color mb-5">Don't have an account? <router-link to="/register" class="text-color text-decoration-underline">Sign Up</router-link></p>
          <p>Sign in to <strong class="color">Snabel</strong></p>
          <div class="form-floating mb-3 position-relative">
            <input v-model="user.username" aria-describedby="username"
                    aria-label="username" class="form-control border-0 border-bottom shadow"
                    name="username" placeholder="enter your first name"
                    required autofocus type="text">
            <i class="fa-solid fa-user icon position-absolute"></i>
            <label for="username">Username</label>
          </div>
          <div class="form-floating mb-3 position-relative">
            <input v-model="user.password" aria-describedby="password"
                    aria-label="password" class="form-control border-0 border-bottom shadow"
                    name="password" placeholder="enter your password"
                    required type="password">
            <i id="togglePassword" class="fas fa-eye-slash icon position-absolute"></i>
            <label for="password">Password</label>
          </div>
          <router-link to="/forget-password" class="text-color text-decoration-underline">Forgot your password?</router-link>
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
        <div class="submit text-center col-lg-8 transition">
          <p class="terms text-color w-100">By clicking the Log In button below, you agree to the Snabel Terms of Service and acknowledge the Privacy Notice.</p>
          <button class="btn btn-secondary text-light fw-bold px-3 mx-5" type="submit">Log In</button>
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
  .signup {
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