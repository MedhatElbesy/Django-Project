<template>
  <div class="about">
    <nav class="row g-0">
      <navbar />
      <navbarResp />
    </nav>
    <h1 class="mt-5 color text-center">Helping people help each other</h1>
    <figure class="text-center my-5">
      <img src="../assets/about.png" alt="about">
    </figure>
    <div class="offset-2 col-8 my-5">
      <p class="text-color ">
        <strong class="color">Snabel</strong> launched in 2024 as a fundraising platform dedicated to helping people help each other. 
        which enables nonprofit organizations to maximize their impact through a suite of online fundraising tools.
      </p>
      <p class="text-color ">Together, <strong class="color">Snabel</strong> and you are building a future where everyone has the ability to make a meaningful difference for the people,causes, and communities they care about most.
    </p>
    </div>
    <footer>
        <footerComponent />
    </footer>
  </div>
</template>
<script>
  import navbar from "@/components/navComponent.vue";
  import navbarResp from "../components/navRespComponent.vue";
  import footerComponent from "../components/footerComponent.vue"

  export default {
    components: {
      navbar,
      navbarResp,
      footerComponent,
    }
  };
</script>
