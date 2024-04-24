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
  import addProjectForm from "@/components/form/addProjectForm.vue";
  export default {
    name: "LoginComponent",
    components: {
      sidebarComponent,
      loginForm,
      registerForm,
      addProjectForm,

    },
    computed: {
      selectedForm() {
        if (this.$route.name === "=login") {
          return 'loginForm';
        } else if (this.$route.name === "register") {
          return 'registerForm';
        } else if (this.$route.name === "forgetPassword") {
          return 'forgetPasswordForm';
        } else if (this.$route.name === "AddProject") {
          return 'addProjectForm';
        } else {
          return 'loginForm';
        }
      }
    }
  }
</script>

<style scoped>
  
</style>