<template>
  <div class="links d-flex">
    <ul v-if="categories.length">
      <h6>Categories</h6>
      <li v-for="(category, i) in categories" :key="category.id">
        <router-link v-if="i < numTodisplay" :to="'/about/' + category.id">{{ category.name }}</router-link>
      </li>
      <li v-if="categories.length > numTodisplay"><router-link to="/about">see all</router-link></li>
    </ul>
    <ul v-if="tags.length">
      <h6>Tags</h6>
      <li v-for="(tag, i) in tags" :key="tag.id">
        <router-link v-if="i < numTodisplay" :to="'/about/' + tag.id">{{ tag.name }}</router-link>
      </li>
      <li v-if="tags.length > numTodisplay"><router-link to="/about">see all</router-link></li>
    </ul>
    <ul>
      <h6>How it works</h6>
      <li><router-link to="/about">how Snabel Works?</router-link></li>
      <li><router-link to="/about">what is crowdFunding</router-link></li>
      <li><router-link to="/about">snabel team</router-link></li>
      <li><router-link to="/about">about snabel</router-link></li>
    </ul>
  </div>
</template>

<script>
  import { useCategoryStore } from "@/stores/categoryStore"
  import { useTagStore } from "@/stores/tagStore"

  export default {
    data: ()=>({
      numTodisplay: 4,
      useCategoryStore: useCategoryStore(),
      useTagStore: useTagStore(),
      categories: [],
      tags: [],
      }),
    async created() {
        await this.useCategoryStore.fetchCategories() instanceof Error 
        ? this.$router.push({ name: "error" }) : this.categories =  this.useCategoryStore.categories;
        await this.useTagStore.fetchTags() instanceof Error 
        ? this.$router.push({ name: "error" }) : this.tags = this.useTagStore.tags;
    }
  }
</script>

<style scoped>
  .links {
    cursor: default;
    background-color: #f5f5f5;
    border-radius: 0 12px 12px 12px;
  }
  ul {
    padding: 12px;
  }
  ul:not(:last-child) {
    margin-right: 12px;
  }

  h6 {
    color: var(--mainTextColor);
    font-weight: bold;
  }

  ul li a {
    display: inline-block;
    width: 100%;
    text-transform: capitalize;
    padding: 4px 16px;
    color: var(--mainTextColor);
    transition: .5s ease-in-out;
    border-radius: 8px;
  }
  ul li a:hover {
    color: var(--mainColor);
    background-color: #cccccc71;
  }
</style>