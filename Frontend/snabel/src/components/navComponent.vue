<template>
  <div class="d-none d-lg-flex justify-content-between align-items-center">
    <ul class="left d-flex">
      <li>
        <router-link :to="{name: 'search'}"><i class="fa-solid fa-magnifying-glass"></i> Search</router-link>
      </li>
      <li class="individuals">
        <a>
          <span>For Individuals <i class="fa-solid fa-angle-down"></i></span>
          <div class="individuals-links">
            <individualsLinks />
          </div>
        </a>
      </li>
      <li><router-link :to="{name: 'home'}">For Charities</router-link></li>
    </ul>
    <figure class="logo d-flex justify-content-center align-items-center mb-0">
      <router-link :to="{name: 'home'}"><img src="../assets/logo.png" alt="Snabel Logo"/></router-link>
    </figure>
    <ul class="right d-flex justify-content-end align-items-center">
      <li><router-link :to="{name: 'AddProject'}" class="fw-bold color">Start SnabelSadaka</router-link></li>
      <li class="user-data position-relative" v-if="loggedUser">
        <div class="user cursor-pointer">
          <img :src="loggedUser.profile_image" :alt="loggedUser.username">
          <span>{{ loggedUser.username }}</span>
        </div>
        <div class="user-links">
          <userLinks />
        </div>
      </li>
      <li v-else><router-link :to="{name: 'login'}" class="fw-bold text-color">Log In</router-link></li>
    </ul>
  </div>
</template>

<script scoped>
import individualsLinks from "@/components/links/individualsLinks.vue";
import userLinks from "@/components/links/userLinks.vue";

export default {
  computed: {
    loggedUser() {
      const userData = sessionStorage.getItem('user');
      if (userData) {
        const user = JSON.parse(userData);
        return {
          username: user.user.username,
          profile_image: user.user.profile_image ? `http://localhost:8000${user.user.profile_image}` : 'https://placehold.co/500x500',
        };
      } else {
        return null;
      }
    }
  },
  components: {
    individualsLinks,
    userLinks,
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

  .individuals-links,
  .user-links {
    position: absolute;
    top: 100%;
    display: none;
  }
  .user-links {
    right: 0;
  }
  li:nth-child(2):hover .individuals-links,
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
    border-radius: 12px 12px 0 0;
    
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
