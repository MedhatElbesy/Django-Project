<template>
  <aside class="col-lg-4 p-lg-5 p-3 transition">
    <figure class="mb-lg-5 mb-3">
      <router-link to="/"><img src="../../assets/logo.png" width="50px" alt="Snabel Logo"></router-link>
    </figure>
    <div class="welcome">
      <span class="text-color">Welcome Back</span>
      <h3 class="color">Don't Forget: </h3>
      <p class="ayat">
        <strong lang="ar" title="(18) Indeed, the men who practice charity and the women who practice charity and [they who] have loaned Allāh a goodly loan - it will be multiplied for them, and they will have a noble reward. ">إِنَّ الْمُصَّدِّقِينَ وَالْمُصَّدِّقَاتِ وَأَقْرَضُوا اللَّـهَ قَرْضًا حَسَنًا يُضَاعَفُ لَهُمْ وَلَهُمْ أَجْرٌ كَرِيمٌ
        <br>
        </strong>
        <em class="text-color">Surah Al-Hadīd: 18</em>
      </p>
    </div>
  </aside>
</template>

<script>
export default {
  name: "SidebarComponent"
}
</script>

<style scoped>
  .welcome {
    padding-top: 28px;
  }
  h3 {
    margin-bottom: 24px;
  }
  .ayat {
    text-align: center;
    direction: rtl;
    padding-bottom: 40px;
    font-weight: bold;
    color: var(--mainTextColor);
    letter-spacing: 2px;
    word-spacing: 3px;
    font-family: 'Reem Kufi', sans-serif;
  }
  em {
    font-size: 12px;
  }
</style>