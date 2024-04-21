<template>
  <div class="container-fluid">
    <main v-if="!loading" class="row g-0">
      <router-view />
    </main>
  </div>
</template>

<script>
  export default {
  }
</script>

<style scoped>
</style>