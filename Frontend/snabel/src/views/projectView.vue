<template>
  <Suspense>
    <template #default>
      <!-- <projectDonationCardsVue /> -->
      <h1>yay</h1>
    </template>
    <template #fallback>
      <div>Loading...</div>
    </template>
  </Suspense>
</template>

<script>
// import projectDonationCardsVue from "../components/projectDonationCards.vue";
export default {
  name: "projectView",
  components: {
    // projectDonationCardsVue,
  },
};
</script>
