<template>
  <div class="about">
    <h1>This is an about page</h1>
    <userProjectComponentVue />
  </div>
</template>
<script>
  import userProjectComponentVue from "../components/userProjectComponent.vue";
  
  export default {
    components: {
      userProjectComponentVue,
    },
  };
</script>
