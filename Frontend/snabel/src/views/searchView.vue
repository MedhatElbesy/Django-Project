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
        <select v-model="searchData.searchOption" name="options" id="">
          <option value="category">Categoty</option>
          <option value="tag">Tag</option>
        </select>
        <input
          @focus="search" @input="search" 
          v-model="searchData.searchValue" type="search" 
          :placeholder="'search by ' + searchData.searchOption" autofocus>
        <i class="fa-solid fa-magnifying-glass"></i> 
      </form>
    </section>
    <section v-if="searchData.searchResult.length" class="m-auto">
      <h3 class="color my-4 text-center">Available Projects</h3>
      <div class="row w-75 m-auto g-0 justify-content-around align-items-center mb-5 p-2">
        <div class="project transition col-md-6 col-lg-4 col-xl-3" v-for="project in searchData.searchResult" :key="project.id">
          <router-link :to="{name: 'ProjectTest', params: {id: project.id}}">
            <figure>
              <img :src="`http://localhost:8000/${project.pictures}`" :alt="project.title">
            </figure>
            <div class="data px-3">
              <p class="title fw-bold color m-0">{{project.title}}</p>
              <p class="user text-color">by {{project.user_name}}</p>
            </div>
            <div class="position-relative">
              <label for="donations"
                :style="{ left: `${parseInt((project.total_collected / project.total_target) * 100)}%` }">
              </label>
              <progress class="w-100" id="donations" :value="parseInt((project.total_collected / project.total_target) * 100 +0)" max="100"></progress>
            </div>
            <p class="m-0 text-color">{{ project.total_collected }} raised</p>
          </router-link>
        </div>
      </div>
    </section>
    <section v-else class="container">
      <lastProjectComponent />
    </section>
    <footer class="row g-0 bg-light">
      <footerComponent />
    </footer>
  </div>
</template>

<script>
  import navbar from "@/components/navComponent.vue";
  import lastProjectComponent from "@/components/lastProjectComponent.vue";
  import footerComponent from "@/components/footerComponent.vue";
  import { useCategoryStore } from "@/stores/categoryStore";
  import { useProjectStore } from "@/stores/project";
  import { useTagStore } from "@/stores/tagStore";

  export default {
    data:()=>({
      stores: {
        useCategoryStore: useCategoryStore(),
        useTagStore: useTagStore(),
        useProjectStore: useProjectStore(),
      },
      allProjects: [],
      searchData: {
        searchValue: "",
        searchOption: "category",
        searchResult: [],
      },
    }),
    components: {
      navbar,
      lastProjectComponent,
      footerComponent,
    },
    async created() {
      // Fetch Categories
      await this.stores.useCategoryStore.fetchCategories();
      // Fetch Tags
      await this.stores.useTagStore.fetchTags();
      // Fetch Projects
      this.allProjects = await this.stores.useProjectStore.allProject();
    },
    methods: {
      search() {
        try {
          let searchValue = this.searchData.searchValue.trim().toLowerCase();
          if(!searchValue) {
            this.searchData.searchResult =[];
            return;
          }

          // Search In Selected Search Option
          if(this.searchData.searchOption == "category") {
            this.searchData.searchResult = this.allProjects.filter((project) => {
              return project.category_name.toLowerCase().startsWith(searchValue);
            })
          } else if(this.searchData.searchOption == "tag") {
            this.searchData.searchResult = this.allProjects.filter((project) => {
              return project.tags_info.some((tag)=>{
                return tag.name.toLowerCase().startsWith(searchValue);
              });
            });
          }
        } catch(error) {
          console.log(error)
        }
      },
    }
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
    box-shadow: 0px 2px 3px 0px #1fc3fa1a;
    z-index: 9;
  }
  form {
    position: relative;
    border-radius: 24px;
    transition: .3s ease-in-out;
    background-color: #F1F1F1;
  }
  form [type="search"] {
    padding: 8px;
    outline: none;
    border: none;
    background-color: transparent;
    caret-color: var(--mainColor);
    display: inline-block;
    width: 100%;
  }
  form [type="search"] :focus {
    caret-color: var(--mainColor);
    color: var(--mainTextColor);
  }
  form [type="search"] ::placeholder {
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
  .show {
    animation: show 3s alternate forwards;
    transition: 3s ease-in-out;
    transform-origin: top center;
    opacity:0;
  }
  .project {
    cursor: pointer;
    border-radius: 12px;
    padding: 12px;
  }
  .project:hover {
    background-color: #F8F8F8;
    box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
  }
  .project figure {
    overflow: hidden;
    margin-bottom: 24px;
  }
  .project figure img{
    width: 100%;
    height: 150px;
    border-radius: 12px;
  }
  .project .title {
    text-transform: capitalize;
  }
  progress {
    height: 6px;
    background-color: #ddd;
    border-radius: 12px;
  }

  progress::-webkit-progress-bar {
    background-color: #ddd;
    border-radius: 10px;
  }

  progress::-webkit-progress-value {
    background-color: var(--mainColor);
    border-radius: 12px;
  }
  label {
    position: absolute;
    top: 15px;
    transform: translate(-50%, -50%);
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background-color: var(--mainColor);
    padding: 8px;;
  }
</style>