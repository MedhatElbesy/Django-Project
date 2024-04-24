<template>
  <div class="text-center">
    <!-- <h1 class="w-75 mb-5 m-auto" lang="ar" title="The likeness of those who spend their wealth in the Way of Allah, is as the likeness of a grain (of corn); it grows seven ears, and each ear has a hundred grains. Allah gives manifold increase to whom He pleases. And Allah is All-Sufficient for His creatures' needs, All-Knower.">
      مَّثَلُ ٱلَّذِينَ يُنفِقُونَ أَمۡوَٰلَهُمۡ فِي سَبِيلِ ٱللَّهِ كَمَثَلِ حَبَّةٍ 
      <br>أَنۢبَتَتۡ سَبۡعَ سَنَابِلَ فِي كُلِّ سُنۢبُلَةٖ مِّاْئَةُ حَبَّةٖۗ وَٱللَّهُ يُضَٰعِفُ لِمَن يَشَآءُۚ وَٱللَّهُ وَٰسِعٌ عَلِيمٌ      
      <em class="text-color">Surah Al Imran: 92</em>
    </h1> -->
    <h1 class="w-75 mb-5 m-auto">Your Home<br> For Help</h1>
    <router-link :to="{name: 'search'}">Give A Sadaka</router-link>
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