<template>
  <div class="about">
    <nav class="row g-0">
      <navbar />
      <navbarResp />
    </nav>
    <h1 class="mt-5 color text-center">Helping people help each other</h1>
  </div>
</template>
<script>
  import navbar from "@/components/navComponent.vue";
  import navbarResp from "../components/navRespComponent.vue";
  export default {
    components: {
      navbar,
      navbarResp
    }
  };
</script>
