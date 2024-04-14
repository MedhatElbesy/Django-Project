<template>
  <div class="home row">
    <header class="d-flex justify-content-center align-items-center">
      <headerSection />
    </header>
    <div class="container p-3">
      <sliderComponent />
    </div>
  </div>
</template>

<script>
  import headerSection from "../components/headerComponent.vue"
  import sliderComponent from "../components/sliderComponent.vue"
  export default {
    data: ()=>({

    }),
    components: {
      headerSection,
      sliderComponent
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


