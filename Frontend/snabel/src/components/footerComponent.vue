<template>
  <div class="links d-flex flex-wrap mb-3">
    <div class="top d-flex flex-wrap align-items-center justify-content-between px-5 mx-3 w-100">
      <figure class="d-flex align-items-center w-75"><router-link to="/">
        <img src="../assets/logo.png" width="150" alt="Snabel Logo"></router-link>
        <figcaption>A way to CHANGE the world</figcaption>
      </figure>
      <ul class="social w-25 justify-content-between">
        <li><a href="https://facebook.com" title="Facebook"><i class="fa-brands fa-facebook"></i></a></li>
        <li><a href="https://x.com" title="Twitter"><i class="fa-brands fa-twitter"></i></a></li>
        <li><a href="https://instagram.com" title="Instagram"><i class="fa-brands fa-instagram"></i></a></li>
        <li><a href="https://youtube.com" title="Youtube"><i class="fa-brands fa-youtube"></i></a></li>
        <li><a href="https://linkedin.com" title="LinkedIn"><i class="fa-brands fa-linkedin"></i></a></li>
        <li><a href="https://reddit.com" title="Reddit"><i class="fa-brands fa-reddit"></i></a></li>
      </ul>
      <ul class="w-75">
        <li>1998-2024 &copy; Snabel-ITI</li>
        <li><router-link to="/terms">Terms</router-link></li>
        <li><router-link to="/privacy">Privacy Notice</router-link></li>
        <li><router-link to="/legal">Legal</router-link></li>
      </ul>
      <ul class="w-25 justify-content-between">
        <li><a href="https://www.googleplay.com"><img src="../assets/googleplay.png" width="120" alt="googleplay"></a></li>
        <li><a href="https://www.appstore.com"><img src="../assets/appstore.png" width="120" alt="appstore"></a></li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
  .links{
    border-top: 1px solid #00000027;
  }
  figcaption {
    font-weight: bold;
    font-size: 22px;
    color: var(--mainTextColor);
  }

  ul {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    margin: 0;
    padding: 0;
  }
  .social i:hover {
    transform: scale(1.2);
  }
  ul:nth-of-type(2) li:first-child {
    color: var(--mainColor);
    font-weight: bold;
  }
  ul:nth-of-type(2) li:not(:first-child) {
    color: var(--mainTextColor);
    padding: 4px 12px;
    margin: 0 4px;
    transition: .3s ease-in-out;
  }
  ul:nth-of-type(2) li:not(:first-child):hover {
    cursor: pointer;
    color: var(--mainColor);
    background-color: #e9e9e9;
    border-radius: 12px;
  }
</style>