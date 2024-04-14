<template>
  <div class="container-fluid">
    <!-- <nav class="row">
      <navbar />
    </nav>-->
    <main class="row">
      <router-view />
    </main>
  </div>
</template>


<script>
  // import navbar from "./components/navComponent.vue"

  export default {
    data: ()=>({
    }),
    components: {
      // navbar,
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
    padding: 8px;
    box-shadow: 0px 2px 5px 0px #d4d4d47e;
  }
</style>
