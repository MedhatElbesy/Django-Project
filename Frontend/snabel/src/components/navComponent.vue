<template>
  <div class="d-flex justify-content-between align-items-center">
    <ul class="d-flex left">
      <li><router-link to="/"><i class="fa-solid fa-magnifying-glass"></i> Search</router-link></li>
      <li @mouseover="display=true" @mouseleave="display=false">
        <span>For Individuals <i class="fa-solid fa-angle-down"></i></span>
        <div class="links">
          <individualsLinks />
        </div>
      </li>
      <li><router-link to="/">For Charities</router-link></li>
    </ul>
    <figure class="logo d-flex justify-content-center align-items-center mb-0"><router-link to="/"><img src="../assets/logo.png" alt="Snabel Logo"></router-link></figure>
    <ul class="d-flex justify-content-end right">
      <li class="fw-bold"><router-link to="/">Start A GoFundMe</router-link></li>
      <li class="fw-bold"><router-link to="/">Log In</router-link></li>
    </ul>
  </div>
</template>

<script scoped>
  import individualsLinks from "./links/individualsLinks.vue"
  export default {
    data:()=>({
      display: false,
    }),
    components: {
      individualsLinks,
    },
  }
</script>

<style scoped>
  ul {
    padding: 8px;
    margin: 0;
  }
  figure {
    flex: 1;
  }
  ul li {
    padding: 4px 12px;
    margin: 0 4px;
    color: var(--mainTextColor);
    transition: .3s ease-in-out;
  }
  ul li:hover {
    cursor: pointer;
    color: var(--mainColor);
    background-color: #f5f5f5;
    border-radius: 12px;
  }

  .left li:nth-child(2) {
    position: relative;
  }
  .left li:nth-child(2):hover {
    border-radius: 12px 12px 0 0;
  }
  .left li:nth-child(2) i {
    transform: rotate(360deg);
    transition: .5s ease-in-out;
  }
  .left li:nth-child(2):hover i {
    transform: rotate(-180deg);
  }
  .left .links {
    position: absolute;
    top: 100%;
    left: 0;
    display: none;
  }
  .left li:nth-child(2):hover .links {
    display: block;
    animation: show 350ms linear both;
  }
  @keyframes show{
    0% { 
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }

  .right li:first-child {
    color: var(--mainColor);
    border-radius: 20px;
    border: 2px solid var(--mainColor);
  }
  .right li:first-child:hover {
    color: #FFF;
    background-color: var(--mainColor);
  }
</style>