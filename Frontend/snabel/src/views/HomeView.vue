<template>
  <div class="home row">
    <header class="d-flex justify-content-center align-items-center">
      <headerSection />
    </header>
    <section>
      <article>
        <sliderComponent />
      </article>
      <article>
        <lastProjectComponent />
      </article>
    </section>
  </div>
</template>

<script>
  import headerSection from "../components/headerComponent.vue"
  import lastProjectComponent from "../components/lastProjectComponent.vue"
  import sliderComponent from "../components/sliderComponent.vue"
  export default {
    data: ()=>({}),
    components: {
      headerSection,
      lastProjectComponent,
      sliderComponent,
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
  section {
    border: 2px solid var(--mainColor);
    padding: 20px;
    background-color: #FFF;
    border-radius: 24px 24px 0 0;
  }
  article {
    margin-bottom: 48px;
  }

</style>


