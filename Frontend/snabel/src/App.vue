<template>
<div>

  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <router-view/>
  <card/>
</div>
</template>

<script>
import card from './components/cardComponent'
export default {
  data:()=>({
    }),
  methods:{},
  components:{
    card,
  }
}
</script>
<style>

</style>
