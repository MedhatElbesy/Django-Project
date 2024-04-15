<template>
  <div class="search">
    <nav class="row g-0">
      <navbar />
    </nav>
    <section class="row g-0 justify-content-center align-items-center text-center mb-3">
      <div class="content mt-5">
        <h2 class="mb-4 color">Search Fundraisers On Snabel</h2>
        <p class="text-color">Find fundraisers by project category or tags</p>
      </div>
    </section>
    <section class="row g-0 search-feild p-3">
      <form class="col-6 col-lg-4 d-flex align-items-center p-2 m-auto">
        <i class="fa-solid fa-magnifying-glass color"></i> 
        <input type="search" name="search" id="search" placeholder="Search">
      </form>
    </section>
    <section class="row g-0 mb-5 p-2">
        <lastProjectComponent />
    </section>
    <footer class="row g-0 bg-light">
      <footerComponent />
    </footer>
  </div>
</template>

<script>
  import navbar from "../components/navComponent.vue"
  import lastProjectComponent from "../components/lastProjectComponent.vue"
  import footerComponent from "../components/footerComponent.vue"

  export default {
    data:()=>({
      searchPosition: null
    }),
    components: {
      navbar,
      lastProjectComponent,
      footerComponent,
    },
  }
</script>

<style scoped>
  nav {
    padding: 12px;
    position: relative;
    z-index: 99;
  }
  .search-feild {
    position: sticky;
    top: 0;
    background-color: #FFF;
    box-shadow: 0px 6px 3px 0px #dedede5b;
    box-shadow: 0px 2px 3px 0px #06a8df1a;
    z-index: 9;
  }
  form {
    text-align: left;
    padding: 8px 16px;
    border-radius: 24px;
    background-color: #F1F1F1;
    transition: .3s ease-in-out;
  }
  form input {
    flex-grow: 1;
    margin-left: 16px;
    outline: none;
    border: none;
    background-color: transparent;
    caret-color: var(--mainColor);
  }
  form input:focus {
    caret-color: var(--mainColor);
    color: var(--mainTextColor);
  }
</style>