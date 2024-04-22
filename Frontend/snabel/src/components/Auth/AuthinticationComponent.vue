<template>
  <div class="row g-0 auth-page bg-light position-relative vh-100">
    <sidebarComponent/>
    <article class="form-container d-flex flex-wrap align-content-center shadow transition col-lg-8">
      <component :is="selectedForm" />
    </article>
  </div>
</template>
<script>
  import sidebarComponent from "@/components/Auth/SidebarComponent.vue";
  import loginForm from "@/components/form/loginForm.vue";
  import registerForm from "@/components/form/registerForm.vue";
  export default {
    name: "LoginComponent",
    components: {
      sidebarComponent,
      loginForm,
      registerForm,
    },
    computed: {
      selectedForm() {
        if (this.$route.name === "Login") {
          return 'loginForm';
        } else if (this.$route.name === "Register") {
          return 'registerForm';
        } else if (this.$route.name === "ForgetPassword") {
          return 'forgetPasswordForm';
        } else {
          return 'loginForm';
        }
      }
    }
  }
</script>

<style scoped>
  
</style>