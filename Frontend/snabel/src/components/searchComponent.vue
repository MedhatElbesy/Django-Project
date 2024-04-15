<template>
  <div class="search">
    <nav class="row g-0">
      <navbar />
    </nav>
    <section class="row g-0 justify-content-center align-items-center text-center mb-5">
      <div class="content mt-5">
        <h2>Search fundraisers on GoFundMe</h2>
        <p>Find fundraisers by location, title, keyword, or a person’s name</p>
      </div>
      <div class="search-field">
        <form class="col-6 col-lg-4 d-flex align-items-center my-3 m-auto">
          <i class="fa-solid fa-magnifying-glass"></i> 
          <input type="search" name="search" id="search" placeholder="Search">
        </form>
      </div>
    </section>
    <section class="mb-5 p-3">
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
  }
  h2 {
    margin-bottom: 16px;
    color: var(--mainColor);
  }
  p {
    color: var(--mainTextColor)
  }
  .search-field {
    background-color: #FFF;
    box-shadow: 0px 6px 3px 0px #dedede1f;
    position: sticky;
    top: 0;
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
  form i {
    color: var(--mainColor);
  }
</style>