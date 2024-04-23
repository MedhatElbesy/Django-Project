<template>
    <div>
        <div v-if="userProject.length > 0" class="row pt-5">
            <div class="col-md-4" v-for="(project, index) in userProject" :key="index">
                <div class="card">
                <img class="card-img-top w-50" :src="getImageUrl(project.pictures)" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">{{ project.title }}</h5>
                    <p class="card-text">{{ project.description }}</p>
                </div>
                </div>
            </div>
        </div>
        <div v-else>
            <p>No projects found.</p>
        </div>
    </div>
</template>
<script>
import { useProjectStore } from '@/stores/project'
    export default {
        name: "userProjectComponent",
        data() {
            return {
                userProject: []
            }
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
        async created(){
            let projects = await useProjectStore().allProject();
            let user_id =JSON.parse(sessionStorage.getItem('user')).user.id;
            projects = projects.filter(project => project.user == user_id);
            this.userProject = projects
            console.log(this.userProject);
        }
    }
</script>