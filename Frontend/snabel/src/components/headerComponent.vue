<template>
  <div class="text-center">
    <h1>Your Home<br> For Help</h1>
    <button><router-link to="/">Start A Fund</router-link></button>
  </div>
</template>

<script>
  export default {
  }
</script>

<style scoped>
  h1 {
    margin-bottom: 28px;
    font-weight: bold;
    color: var(--mainColor);
    letter-spacing: 2px;
    word-spacing: 3px;
  }
  button {
    cursor: pointer;
    padding: 12px 24px;
    color: var(--mainColor);
    font-weight: bold;
    border: 2px solid var(--mainColor);
    border-radius: 16px;
    transition: .3s ease-in-out;
  }
  button:hover {
    padding: 12px 24px;
    color: #FFF;
    background-color: var(--mainColor);
    font-weight: bold;
    border: 2px solid var(--mainColor);
    border-radius: 12px;
  }
</style>