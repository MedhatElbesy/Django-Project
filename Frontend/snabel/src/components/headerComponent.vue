<template>
  <div class="text-center">
    <h1 lang="ar">لَن تَنَالُوا الْبِرَّ حَتَّىٰ تُنفِقُوا مِمَّا تُحِبُّونَ ۚ
      <br>وَمَا تُنفِقُوا مِن شَيْءٍ فَإِنَّ اللَّهَ بِهِ عَلِيمٌ<br>
      <em class="text-color">Surah Al Imran: 92</em>
    </h1>
    <router-link to="/search">Give A Sadaka</router-link>
  </div>
</template>

<script>
  export default {
  }
</script>

<style scoped>
  h1 {
    direction: rtl;
    margin-bottom: 40px;
    font-weight: bold;
    color: var(--mainColor);
    text-shadow: 0px 2px 4px #41ccfa;
    letter-spacing: 2px;
    word-spacing: 3px;
    font-family: 'Reem Kufi', sans-serif;
  }
  em {
    font-size: 16px;
    text-shadow: none;
  }
  a {
    cursor: pointer;
    padding: 12px 24px;
    color: var(--mainColor);
    border: 2px solid var(--mainColor);
    border-radius: 16px;
    transition: .3s ease-in-out;
    font-weight: bold;
  }
  a:hover {
    color: #FFF;
    background-color: var(--mainColor);
  }
</style>