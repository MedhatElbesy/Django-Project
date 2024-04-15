<template>
  <div class="home">
    <nav class="row g-0">
      <navbar />
    </nav>
    <header class="row g-0 justify-content-center align-items-center">
      <headerSection />
    </header>
    <section class="row g-0 bg-light">
      <article>
        <sliderComponent />
      </article>
      <article>
        <lastProjectComponent />
      </article>
    </section>
    <footer class="row g-0 bg-light">
      <footerComponent />
    </footer>
  </div>
</template>

<script>
  import navbar from "../components/navComponent.vue"
  import headerSection from "../components/headerComponent.vue"
  import lastProjectComponent from "../components/lastProjectComponent.vue"
  import sliderComponent from "../components/sliderComponent.vue"
  import footerComponent from "../components/footerComponent.vue"
  export default {
    data: ()=>({}),
    components: {
      navbar,
      headerSection,
      lastProjectComponent,
      sliderComponent,
      footerComponent,
    },
    mounted() {
      window.addEventListener("scroll", this.navOnScroll);
    },
    methods: {
      navOnScroll() {
        let nav = document.querySelector("nav");
        if (window.scrollY > 80) {
          console.log("done");
          nav.classList.add("nav-on-scroll");
        } else {
          nav.classList.remove("nav-on-scroll");
        }
      }
    },
    beforeUnmount() {
      window.removeEventListener("scroll", this.navOnScroll);
    }
  }
</script>

<style scoped>
  .home {
    background: url("../assets/header.png") center center/cover fixed;
  }
  section {
    padding: 20px;
    border-radius: 24px 24px 0 0;
  }
  article {
    margin-bottom: 48px;
  }
  nav {
    width: 75%;
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translate(-50%);
    border-radius: 30px;
    transition: .5s ease-in-out;
    background-color: #FFF;
    z-index: 9999;
  }
  .nav-on-scroll {
    width: 100%;
    top: 0px;
    border-radius: 0px;
    padding: 12px;
    box-shadow: 0px 3px 7px 0px #d4d4d4b7;
  }
  header{
    height: 70vh;
  }
</style>


