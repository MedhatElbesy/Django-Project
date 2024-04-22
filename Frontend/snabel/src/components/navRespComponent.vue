<template>
  <div class="d-lg-none transition">
    <ul class="main w-100 d-flex justify-content-between align-items-center">
      <li> 
        <router-link class="btn btn-link" :to="{name: 'Search'}"><i class="fa-solid fa-magnifying-glass"></i></router-link>
      </li>
      <figure class="logo d-flex justify-content-center align-items-center mb-0">
        <router-link :to="{name: 'Home'}"><img src="../assets/logo.png" style='width: 45px' alt="Snabel Logo"/></router-link>
      </figure>
      <li class="bar">
        <button class="btn btn-link" @click="showLinks=true"><i class="fa-solid fa-bars"></i></button>
      </li>
    </ul>
    <div v-if="showLinks" class="nav-links col-12 col-sm-9">
      <i @click="showLinks = false" class="btn btn-link fa-sharp fa-solid fa-xmark"></i>
      <ul class="wrap d-flex flex-wrap">
        <li class="user-data d-flex flex-column align-items-center">
          <img src="https://placehold.co/500x500" class="rounded-circle" width="70" alt="user">
          <h5>
            <span>user khaled</span>
            <i @click="showUser=true" class="btn btn-link fa-solid fa-angle-right"></i>
          </h5>
        </li>
        <!-- Show User Links -->
        <li class="data" v-if="showUser">
          <ul class="user-links">
            <h5 class="">
              <i @click="showUser=false" class="btn btn-link fa-solid fa-angle-left"></i>
              <span>Account</span>
            </h5>
            <li class="mt-5"><router-link :to="{name: 'About'}">Your Impact</router-link></li>
            <li><router-link :to="{name: 'About'}">Account Settings</router-link></li>
            <li><router-link :to="{name: 'AddProject'}">Start SnabelSadaka</router-link></li>
            <li><router-link :to="{name: 'About'}">Help Center</router-link></li>
            <li class="log-out fw-bold"><router-link :to="{name: 'Home'}">Log Out</router-link></li>
          </ul>
        </li>
        <li class="individuals open" @click="showIndividuals = true">
          <p>For Individuals <br><span>Start fundraising, tips, and resources</span></p> 
          <i class="fa-solid fa-angle-right"></i>
        </li>
        <!-- Show Individuals Links -->
        <li class="data" v-if="showIndividuals">
          <h5>
            <i @click="showIndividuals=false" class="btn btn-link fa-solid fa-angle-left"></i>
            <span>For Individuals</span>
          </h5>
          <div>
            <individualsLinks />
          </div>
        </li>
        <li class="about">
          <router-link class="open w-100" :to="{name: 'About'}">
            <p>About <br><span>How it works, pricing, and more</span></p> 
            <i class="fa-solid fa-angle-right"></i>
          </router-link>
        </li>
        <li class="charities">
          <router-link class="open w-100" :to="{name: 'About'}">
            <p>For Charities <br>
              <span>raise money for the nonprofits you care</span>
            </p> 
            <i class="fa-solid fa-angle-right"></i>
          </router-link></li>
        <li class="donate text-center mt-4"><router-link :to="{name: 'AddProject'}" class="transition fw-bold color">Start SnabelSadaka</router-link></li>
      </ul>
    </div>
  </div>
</template>

<script scoped>
import individualsLinks from "./links/individualsLinks.vue";
import { useAuthenticationStore } from "@/stores/auth";

export default {
  data: () => ({
    showLinks: false,
    showUser: false,
    showIndividuals: false,
    authentication: {
      useAuthenticationStore: useAuthenticationStore(),
      userData: useAuthenticationStore.user,
      isAuth: useAuthenticationStore.isAuth,
    },
  }),
  components: {
    individualsLinks,
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

body {
  position: relative;
}
.nav-links,
.data {
  background-color: #f5f5f5;
  animation: show 350ms linear both;
  transform: translateX(100%);
  position: fixed;
  height: 100vh;
  top: 0;
  right: 0;
  padding: 8px;
  overflow: auto;
  }
  ul {
    padding: 8px;
    margin: 0;
  }
  .main li {
    transition: .3s ease-in-out;
    cursor: pointer;
    width: 100%;
    padding: 8px;
  }
  li {
    transition: .3s ease-in-out;
    cursor: pointer;
    width: 100%;
    padding: 20px;
  }
  .individuals,
  .about a,
  .charities a{
    font-size: 20px;
    color: #706f6f;
  }
  .individuals:hover,
  .about:hover,
  .charities:hover {
    background-color: #cccccc71;
  }

  .open {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .open p {
    margin: 0;
  }
  .open span {
    color: #8b8b8b;
    font-size: 14px;

  }

  .data {
    position: absolute;
    width: 100%;
  }
  .data li  {
    padding: 0;
  }
  .user-links li a {
    display: inline-block;
    width: 100%;
    transition: .3s ease-in-out;
    cursor: pointer;
    width: 100%;
    padding: 12px;
    color: var(--mainTextColor);
  }
  .user-links li a:hover {
    color: var(--mainColor);
  }
  .user-links li:hover {
    background-color: #cccccc71;
  }
  .user-links li:last-child a:hover {
    color: #DC3545 !important;
  }
  .donate a {
    border: 2px solid var(--mainColor);
    border-radius: 20px;
    padding: 8px 16px;
  }
  .donate a:hover {
    color: #fff;
    background-color: var(--mainColor);
  }
  .bar {
    text-align: right;
  }
  .btn-link {
    color: var(--mainTextColor);
    font-weight: bold;
    text-decoration: none;
    padding: 8px;
    border-radius: 50%;
    height: 40px;
    width: 40px;
    transition: .3s ease-in-out;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .btn-link:hover{
    background-color: #cccccc71;
  }
  h5 {
    display: flex;
    align-items: center;
    color: var(--mainColor);
  }
  h5 span {
    padding: 8px;
  }

  @keyframes show {
    100% {
      transform: translateX(0);
    }
  }
</style>
