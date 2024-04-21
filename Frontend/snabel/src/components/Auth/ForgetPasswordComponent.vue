<template>
  <div class="row g-0 auth-page bg-light position-relative">
    <!-- Start Messages -->
    <div v-if="successMessages" class="alert alert-success alert-dismissible fade show position-absolute top-0 start-50 translate-middle-x p-2" role="alert">
        <strong class="mb-0">{{ successMessages }}</strong>
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close" style="height: auto;"></button>
    </div>
    <div v-if="errorMessages" class="alert alert-danger alert-dismissible fade show position-absolute top-0 start-50 translate-middle-x p-2" role="alert">
        <strong class="mb-0">{{ errorMessages }}</strong>
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close" style="height: auto;"></button>
    </div>
    <!-- End Of Messages -->

    <SidebarComponent/>

    <article class="reset d-flex flex-wrap align-content-center shadow col-lg-8 vh-100">
      <form class="w-75 m-auto mt-5"  @submit.prevent="sendResetPassword">
        <p class="signup color mb-5">Don't have an account? <router-link to="/register" class="text-color text-decoration-underline">Sign Up</router-link></p>
        <div class="form-floating mb-3 position-relative">
          <input v-model="email" aria-describedby="email" aria-label="email"
                 class="form-control border-0 border-bottom shadow" name="email"
                 placeholder="enter your email address"
                 required type="email">
          <i class="fa-solid fa-envelope icon position-absolute"></i>
          <label for="email">Email</label>
        </div>
        <p class="request text-color mb-5">Enter your email address and we'll send you instructions to reset your password</p>
        <div class="submit col-lg-8 col-12">
          <router-link to="/login" class="fw-bold text-color"><i class="fa-solid fa-angle-left"></i> Return To Sign In</router-link>
          <button class="btn btn-secondary text-light fw-bold px-3 mx-5" type="submit">Request Password Reset</button>
        </div>
      </form>
    </article>
  </div>
</template>

<script>
import axios from "axios";
import SidebarComponent from "@/components/Auth/SidebarComponent.vue";

export default {
  name: "ResetPasswordComponent",
  data: () => ({
    email: '',
    errorMessages: '',
    successMessages: '',
  }),

  components:{
    SidebarComponent
  },

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
            this.errorMessages = '';
            this.scrollToTop();
          })
          .catch(error => {
            this.successMessages = '';
            if (error.response && error.response.data) {
              const responseData = error.response.data;
              if (responseData && typeof responseData === 'object') {
                this.errorMessages = responseData.error;
                this.scrollToTop();
              } else {
                this.errorMessages = 'Invalid error response';
                console.error('Invalid error response:', responseData);
              }
            } else if (error.request) {
              this.errorMessages = 'No response received try again later';
              console.error('No response received:', error.request);
            } else {
                this.errorMessages = `Error occurred`;
                console.error('Error:', error.message);

            }
          });
    }
  }
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