<template>
  <div class="d-none d-lg-flex justify-content-between align-items-center">
    <ul class="left d-flex">
      <li>
        <router-link :to="{name: 'Search'}"><i class="fa-solid fa-magnifying-glass"></i> Search</router-link>
      </li>
      <li class="individuals">
        <a>
          <span>For Individuals <i class="fa-solid fa-angle-down"></i></span>
          <div class="links">
            <individualsLinks />
          </div>
        </a>
      </li>
      <li><router-link :to="{name: 'Home'}">For Charities</router-link></li>
    </ul>
    <figure class="logo d-flex justify-content-center align-items-center mb-0">
      <router-link :to="{name: 'Home'}"><img src="../assets/logo.png" alt="Snabel Logo"/></router-link>
    </figure>
    <ul class="right d-flex justify-content-end align-items-center">
      <li><router-link :to="{name: 'AddProject'}" class="fw-bold color">Start SnabelSadaka</router-link></li>
      <li class="user-data position-relative" v-if="test">
        <div class="user cursor-pointer">
          <!-- <img :src="`http://localhost:8000/${authentication.userData.profile_image}`" :alt="userData.username">
          <span>{{ `${userData.first_name} ${userData.last_name}` }}</span> -->
          <img src="https://placehold.co/500x500" alt="user">
          <span>user khaled</span> <i class="fa-solid fa-angle-down"></i>
        </div>
        <div class="user-links">
          <userLinks />
        </div>
      </li>
      <li v-else><router-link :to="{name: 'Login'}" class="fw-bold text-color">Log In</router-link></li>
    </ul>
  </div>
</template>

<script scoped>
import individualsLinks from "./links/individualsLinks.vue";
import userLinks from "./links/userLinks.vue";
import { useAuthenticationStore } from "@/stores/auth"
export default {
  data: () => ({
    authentication: {
      useAuthenticationStore: useAuthenticationStore(),
      userData: useAuthenticationStore.user,
      isAuth: useAuthenticationStore.isAuth,
    },
  }),
  components: {
    individualsLinks,
    userLinks,
  },
  computed: {
    test() {
      // let test = this.authentication.useAuthenticationStore.user;
      // return true;
      return false;
    }
  },

};
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
    margin: 0 4px;
    color: var(--mainTextColor);
  }

  li a {
    padding: 4px 12px;
    color: var(--mainTextColor);
    border-radius: 12px;
    transition: background-color 0.3s ease-in-out;
  }

  .left li a:hover {
    cursor: pointer;
    color: var(--mainColor);
    background-color: #f5f5f5;
  }

  .individuals a {
    position: relative;
    border-radius: 12px 12px 0 0;
  }
  .individuals i,
  .user-data i {
    transform: rotate(360deg);
    transition: 0.5s ease-in-out;
  } 
  .individuals:hover i,
  .user-data:hover i {
    transform: rotate(-180deg);
  }

  .links {
    position: absolute;
    top: 100%;
    left: 0;
    display: none;
  }

  li:nth-child(2):hover .links,
  .user-data:hover .user-links {
    display: block;
    animation: show 350ms linear both;
  }
  
  .right li a,
  .user-links a {
    padding: 4px 12px;
    transition: 0.3s ease-in-out;
  }
  .right li:first-child a{
    border: 2px solid var(--mainColor);
    border-radius: 20px;
  }
  .right li:first-child a:hover {
    color: #fff;
    background-color: var(--mainColor);
  }
  .right li:last-child a:hover {
    color: var(--mainColor);
  }

  .user-data {
    cursor: pointer;
    padding: 4px 12px;
    border-radius: 12px;
    
  }
  .user-data:hover {
    background-color: #f5f5f5;
  }

  .user-data .user img {
    width: 45px;
    height: 45px;
    border-radius: 50%;
    margin-right: 12px;
  }

  @keyframes show {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }
</style>
