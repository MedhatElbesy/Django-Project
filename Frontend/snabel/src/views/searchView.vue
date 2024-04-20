<template>
  <div class="search">
    <nav class="row g-0">
      <navbar />
    </nav>
    <section class="row g-0 justify-content-center align-items-center text-center mb-3">
      <div class="content mt-5">
        <h2 class="mb-4 color">Search Fundraisers On Snabel</h2>
        <p class="text-color">Find fundraisers by project category or tags</p>
      </div>
    </section>
    <section class="search-feild row flex-wrap justify-content-center g-0 p-3">
      <form class="d-flex align-items-center col-11 col-md-8 col-lg-5 mx-1">
        <select v-model="searchOption" name="options" id="">
          <option value="category">Categoty</option>
          <option value="tag">Tag</option>
        </select>
        <input 
          @focusout="outOfFocus" @focus="search" @input="search" 
          v-model="searchValue" type="search" 
          :placeholder="'search by ' + searchOption" autofocus>
        <i class="fa-solid fa-magnifying-glass"></i> 
      </form>
      <div class="col-12"></div>
      <ul v-if="searchResult.length" class="search-result mt-2 col-11  col-lg-5">
        <li v-for="category in searchResult" :key="category.id">
          <router-link to="/categories/{{category.name}}">
            <i class="fa-solid fa-magnifying-glass color invisible"></i> {{ category.name }}
          </router-link>
        </li>
      </ul>
    </section>
    <section class="row g-0 mb-5 p-2">
        <lastProjectComponent />
    </section>
    <footer class="row g-0 bg-light">
      <footerComponent />
    </footer>
  </div>
</template>

<script>
  import navbar from "@/components/navComponent.vue"
  import lastProjectComponent from "@/components/lastProjectComponent.vue"
  import footerComponent from "@/components/footerComponent.vue"
  import { useCategoryStore } from "@/stores/categoryStore"
  import { useTagStore } from "@/stores/tagStore"

  export default {
    data:()=>({
      useCategoryStore: useCategoryStore(),
      useTagStore: useTagStore(),
      searchValue: "",
      searchOption: "category",
      searchResult: [],
    }),
    components: {
      navbar,
      lastProjectComponent,
      footerComponent,
    },
    async created() {
      if(await this.useCategoryStore.fetchCategories() instanceof Error){
        this.$router.push({ name: "error" });
      }
      if(await this.useTagStore.fetchTags() instanceof Error ) {
        this.$router.push({ name: "error" });
      }
      
    },
    methods: {
      search() {
        try {
          let searchOptions = [];

          // Check Search Option
          this.searchOption == "category" ? searchOptions = this.useCategoryStore.categories : searchOptions = this.useTagStore.tags;

          // Search In Selected Search Option
          this.searchValue
          ? this.searchResult = searchOptions.filter((option) => {
              return option.name.toLowerCase().startsWith(this.searchValue.toLowerCase());
            })
          : this.searchResult = [];
        } catch(error) {
          this.$router.push({ name: "error" });
        }
      },
      outOfFocus() {
        setTimeout(()=>{this.searchResult = []}, 200)
      },
    },
  }
</script>

<style scoped>
  nav {
    padding: 12px;
    position: relative;
    z-index: 99;
  }
  .search-feild {
    position: sticky;
    top: 0;
    background-color: #FFF;
    box-shadow: 0px 2px 3px 0px #06a8df1a;
    z-index: 9;
  }
  form {
    position: relative;
    border-radius: 24px;
    transition: .3s ease-in-out;
    background-color: #F1F1F1;
  }
  form input {
    padding: 8px;
    outline: none;
    border: none;
    background-color: transparent;
    caret-color: var(--mainColor);
    display: inline-block;
    width: 100%;
  }
  form input:focus {
    caret-color: var(--mainColor);
    color: var(--mainTextColor);
  }
  form input::placeholder {
    font-style: italic;
    font-size: 14px;
  }
  select {
    padding: 8px;
    border: 1px solid var(--mainColor);
    background-color: var(--mainColor);
    border-radius: 24px 0 0 24px;
    color: #FFF;
  }
  select:focus {
    outline: none;
  }
  option {
    background-color: #F1F1F1;
    color: var(--mainTextColor);
  }
  form i {
    position: absolute;
    right: -8px;
    color: #FFF;
    background-color: var(--mainColor);
    border-radius: 50%;
    padding: 16px;
  }
  .search-result {
    border: 1px solid #cccccc71;
    border-radius: 24px;
    border-radius: 8px;
    padding: 4px 4px 0 4px;
  }
  .search-result a {
    display: inline-block;
    width: 100%;
    text-transform: capitalize;
    padding: 4px 16px;
    color: var(--mainTextColor);
    transition: .2s ease-in-out;
    border-radius: 8px;
    margin-bottom: 4px;
    border: 1px solid transparent;
    background-color: #c0c0c021;
  }
  .search-result a:hover {
    color: var(--mainColor);
    font-weight: bold;
    background-color: #cccccc71;
  }
  .search-result a:hover i {
    visibility: visible !important;
  }
</style>