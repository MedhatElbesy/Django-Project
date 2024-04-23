<template>
    <div>
        <nav class="row g-0">
            <navbar />
            <navbarResp />
        </nav>
        <section v-if="userProject.length > 0" class="row g-0 pt-5">
            <h3 class="color my-4 text-center">Available Projects</h3>
            <div class="row w-75 m-auto g-0 justify-content-around align-items-center mb-5 p-2">
                <div class="project d-flex transition col-md-5 col-lg-4 col-xl-3" v-for="(project, index) in userProject" :key="index">
                    <router-link :to="{name: 'ProjectTest', params: {id: project.id}}" class="w-100 d-flex flex-wrap justify-content-between align-items-center">
                        <figure class="col-4 col-md-12 mb-sm-0 mb-md-3">
                        <img :src="`http://localhost:8000/${project.pictures}`" :alt="project.title">
                        </figure>
                        <div class="wrap col-7 col-md-12">
                        <div class="data px-sm-0 px-md-3">
                            <p class="title fw-bold color m-0">{{project.title}}</p>
                            <p class="user text-color">by {{project.user_name}}</p>
                        </div>
                        <div class="donations-progress position-relative">
                            <label for="donations"
                            :style="{ left: `${parseInt((project.total_collected / project.total_target) * 100)}%` }">
                            </label>
                            <progress class="w-100" id="donations" :value="parseInt((project.total_collected / project.total_target) * 100 +0)" max="100"></progress>
                        </div>
                        <p class="m-0 text-color">{{ project.total_collected }} raised</p>
                        </div>
                    </router-link>
                </div>
            </div>
            </section>
            <!-- <div class="col-md-4" v-for="(project, index) in userProject" :key="index">
                <div class="card">
                <img class="card-img-top w-50" :src="getImageUrl(project.pictures)" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">{{ project.title }}</h5>
                    <p class="card-text">{{ project.description }}</p>
                </div>
                </div>
            </div> -->
        <div v-else>
            <p>No projects found.</p>
        </div>
        <footer class="row g-0 bg-light">
            <footerComponent />
        </footer>
    </div>
</template>

<script>
    import { useProjectStore } from '@/stores/project';
    import navbar from "@/components/navComponent.vue";
    import navbarResp from "../components/navRespComponent.vue";
    import footerComponent from "@/components/footerComponent.vue";

    export default {
        name: "userProjectComponent",
        data() {
            return {
                userProject: [],
            }
        },
        components: {
            navbar,
            navbarResp,
            footerComponent,
        },
        methods: {
            getImageUrl(image){
                if(image.includes('http://127.0.0.1:8000')){
                    return image;
                }
                return `http://127.0.0.1:8000${image}`;
            },
            getName(){
                return "Mohamed Isamil";
            }
        },
        async created() {
            let projects = await useProjectStore().allProject();
            console.log(projects);
            let user_id = JSON.parse(sessionStorage.getItem('user')).user.id;
            projects = projects.filter(project => project.user == user_id);
            this.userProject = projects;
            console.log(this.userProject);
        }
    }
</script>

<style scoped>
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
  @media screen and (max-width: 768px) {
    .row {
      width: 100% !important;
    }
  }
</style>