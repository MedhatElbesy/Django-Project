<template>
  <div class="home row">
    <header class="d-flex justify-content-center align-items-center">
      <headerSection />
    </header>
  </div>
</template>

<script>
  import headerSection from "../components/headerComponent.vue"
  export default {
    data: ()=>({}),
    components: {
      headerSection,
    }
  }
</script>

<style scoped>
  .home {
    background: url("../assets/header.png") center center/cover fixed;
  }
  header{
    height: 70vh;
  }

</style>


