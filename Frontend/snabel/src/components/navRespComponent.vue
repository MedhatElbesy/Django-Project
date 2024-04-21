<template>
  <div class="d-flex justify-content-between align-items-center">
    <ul class="left d-flex ">
      <li><router-link to="/search"><i class="fa-solid fa-magnifying-glass"></i></router-link></li>
      <li @mouseover="display=true" @mouseleave="display=false">
        <span>For Individuals <i class="fa-solid fa-angle-down"></i></span>
        <div class="links">
          <individualsLinks />
        </div>
      </li>
      <li><router-link to="/">For Charities</router-link></li>
    </ul>
    <figure class="logo d-flex justify-content-center align-items-center mb-0"><router-link to="/"><img src="../assets/logo.png" alt="Snabel Logo"></router-link></figure>
    <div class="right d-flex justify-content-end">
      <router-link to="/search" class="fw-bold color">Start SnabelSadaka</router-link>
      <router-link to="/login" class="fw-bold text-color">Log In</router-link>
    </div>
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
  li {
    padding: 4px 12px;
    margin: 0 4px;
    color: var(--mainTextColor);
    transition: background-color .3s ease-in-out;
    border-radius: 12px;
  }
  li a {
    color: var(--mainTextColor);
  }
  li:hover,
  li a:hover {
    cursor: pointer;
    color: var(--mainColor);
    background-color: #f5f5f5;
  }

  li:nth-child(2) {
    position: relative;
  }
  li:nth-child(2):hover {
    border-radius: 12px 12px 0 0;
  }
  li:nth-child(2) i {
    transform: rotate(360deg);
    transition: .5s ease-in-out;
  }
  li:nth-child(2):hover i {
    transform: rotate(-180deg);
  }

  .links {
    position: absolute;
    top: 100%;
    left: 0;
    display: none;
  }
  li:nth-child(2):hover .links {
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

  .right a {
    padding: 4px 12px;
    transition: .3s ease-in-out;
  }
  .right a:first-child {
    border: 2px solid var(--mainColor);
    border-radius: 20px;
  }
  .right a:first-child:hover {
    color: #FFF;
    background-color: var(--mainColor);
  }
  .right a:last-child:hover {
    color: var(--mainColor);
  } 
</style>