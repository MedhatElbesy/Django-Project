<template>
  <ul class="links">
    <li><router-link :to="{name: 'userDonation'}">Your Impact</router-link></li>
    <li><router-link :to="{name: 'profile'}">Account Settings</router-link></li>
    <li><router-link :to="{name: 'AddProject'}">Start SnabelSadaka</router-link></li>
    <li><router-link :to="{name: 'about'}">Help Center</router-link></li>
    <li class="log-out fw-bold" @click="useAuthenticationStore.logout()">Log Out</li>
  </ul>
</template>

<script>
import { useAuthenticationStore } from "@/stores/auth";
  export default {
    data: ()=>({
      useAuthenticationStore: useAuthenticationStore(),
      }),
  }
</script>

<style scoped>
  ul {
      padding: 8px;
      margin: 0;
    }
.links {
    background-color: #f5f5f5;
    border-radius: 12px 0 12px 12px;
    width: fit-content;
  }

  .user img {
    width: 45px;
    height: 45px;
    border-radius: 50%;
    margin-right: 12px;
  }

  .links li a,
  .log-out {
    display: inline-block;
    width: 100%;
    text-transform: capitalize;
    padding: 4px 16px;
    color: var(--mainTextColor);
    transition: .5s ease-in-out;
    border-radius: 8px;
  }

  .links li:hover {
    color: var(--mainColor);
    background-color: #cccccc71;
  }

  .log-out:hover {
    color: #DC3545 !important;
  } 
</style>