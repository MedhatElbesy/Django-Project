<template>
  <ul class="links">
    <li><router-link :to="{name: 'About'}">Your Impact</router-link></li>
    <li><router-link :to="{name: 'About'}">Account Settings</router-link></li>
    <li><router-link :to="{name: 'AddProject'}">Start SnabelSadaka</router-link></li>
    <li><router-link :to="{name: 'About'}">Help Center</router-link></li>
    <li class="log-out fw-bold"><router-link :to="{name: 'Home'}">Log Out</router-link></li>
  </ul>
</template>

<script>
  export default {
    data: ()=>({
      }),
    async created() {
    }
  }
</script>

<style scoped>
  ul {
      padding: 8px;
      margin: 0;
    }
.links {
    cursor: default;
    background-color: #f5f5f5;
    border-radius: 12px;
    position: absolute;
    top: 100%;
    right: 0;
    display: none;
  }

  .user img {
    width: 45px;
    height: 45px;
    border-radius: 50%;
    margin-right: 12px;
  }

  .links li a {
    display: inline-block;
    width: 100%;
    text-transform: capitalize;
    padding: 4px 16px;
    color: var(--mainTextColor);
    transition: .5s ease-in-out;
    border-radius: 8px;
  }

  .links li a:hover {
    color: var(--mainColor);
    background-color: #cccccc71;
  }

  .log-out a:hover {
    color: #DC3545 !important;
  } 
</style>