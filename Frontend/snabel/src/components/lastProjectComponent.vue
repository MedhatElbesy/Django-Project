<template>
    <!-- <div class="container"> -->
        <div class="row position-relative" v-if="lastProjects.length > 0"><!--The Parent row  -->
            <div class="col-md-6 p-2">
                <div class="card text-start custom-card">
                    <img class="card-img" :src="lastProjects[0].pictures" alt="Title" />
                    <div class="card-img-overlay">
                        <p class="badge rounded-pill bg-black ">{{lastProjects[0].donations}} donations</p>
                    </div>
                    <div class="card-body mt-3">
                        <h4 class="card-title pt-2">{{ lastProjects[0].title }}</h4>
                        <p class="card-text pt-2">{{ lastProjects[0].description }}</p>
                        <div class="progress mt-3">
                            <div class="progress-bar bg-primary" role="progressbar"  aria-valuenow="25" :style="{ width: (lastProjects[0].total_collected /lastProjects[0].total_target)*100  + '%' }" aria-valuemin="0" aria-valuemax="100">{{ parseInt((lastProjects[0].total_collected / lastProjects[0].total_target) * 100) }}%</div>
                        </div>
                    </div>
                    <router-link :to="{name: 'ProjectTest', params: {id: lastProjects[0].id}}" class="btn btn-primary mylink">Details</router-link>
                </div>

            </div>

            <div class="col-md-6"><!--The Parent div  -->

                <div class="row "><!-- First  Second Row -->

                    <div class="col-md-6 p-2 position-relative" v-for="(project, index) in lastProjects.slice(1)" :key="index"> 
                        <div class="card text-start">
                            <img class="card-img" :src="project.pictures" alt="Title" style="max-height: 175px;"/>
                            <div class="card-img-overlay">
                                <p class="badge rounded-pill bg-black">{{project.donations}} donations</p>
                            </div>
                            <div class="card-body">
                                <h4 class="card-title">{{ project.title }}</h4>
                                <p class="card-text">{{ project.description }}</p>
                                <div class="progress">
                                    <div
                                        class="progress-bar bg-primary" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100" :style="{ width: (project.total_collected /project.total_target)*100  + '%' }">
                                        {{ parseInt((project.total_collected / project.total_target) * 100) }}%
                                    </div>
                                </div>
                                
                            </div>
                            <router-link :to="{name: 'ProjectTest', params: {id: project.id}}" class="btn btn-primary mylink w-50 mx-auto my-2">Details</router-link>
                        </div>
                    </div>
                </div><!-- end  Second Row -->


            </div><!--End The Parent div  -->
        </div><!-- end The Parent row  -->
    <!-- </div> --> <!-- end The container  -->
</template>

<script>
import {useProjectStore} from '@/stores/project'
export default {
    name: 'lastProjectComponent',
    data() {
        return {
            lastProjects: []
        }
    },
    methods: {
        
    },
    async created() {
        try{
            let project = await useProjectStore();
            this.lastProjects = await project.latest();
        }catch(err){
            console.log(err);
        }
    }
}
</script>

<style scoped>

.card{
    /* cursor: pointer; */
    overflow: hidden;
}

.custom-card {
    height: 615px;
}
.card:hover img {
    transform: scale(1.1);
}
.card img {
    transition: all 0.5s ease;
}
.mylink {
    z-index: 1;
}


</style>