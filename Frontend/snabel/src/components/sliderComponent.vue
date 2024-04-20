<template>
    <div id="productImage" class="carousel slide " data-bs-ride="carousel" v-if="projects.length > 0">
        <!-- buttons indicators -->
        <div class="carousel-indicators">
            <button v-for="(project, index) in topProjects" 
                :key="index"
                type="button" 
                data-bs-target="#productImage" 
                :data-bs-slide-to="index"
                :class="{ 'active': index === 0 }" 
                aria-current="true" 
                aria-label="Slide {{ index + 1 }}"
                >
            </button>
        </div>
        <!-- items -->
        <div class="carousel-inner">
            <!--  image item -->
            <div 
                v-for="(project, index) in topProjects"
                :key="index"
                :class="{ 'carousel-item': true, active: index === 0 }"
            >
                <img :src="getImageUrl(project.pictures)" class="d-block w-100" alt="...">
                <div class="carousel-caption d-none d-md-block">
                    <h5>First slide label</h5>
                    <p>Some representative placeholder content for the first slide.</p>
                </div>
            </div>


        </div>

        <!-- Next & previous -->
        <button class="carousel-control-prev" type="button" data-bs-target="#productImage" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#productImage" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>
</template>

<script>
import { useProjectStore } from '@/stores/project'
export default {
    name: 'SliderComponent',
    data() {
        return {
            topProjects: []
        }
    },
    async created(){
        let projects = await useProjectStore().allProject()
        projects.sort((a, b) => b.get_project_rating - a.get_project_rating);
        // this.topProjects = projects.results;
        this.topProjects = projects.slice(0, 5);
        console.log(this.topProjects[0].pictures);
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
    }
}
</script>

<style scoped>
    #productImage{
        height: 400px;
        width: 100%;
    }
    #productImage img{
        height: 400px;
    }
    #productImage .carousel-item{
        height: 400px;
    }
    #productImage .carousel-item img{
        height: 400px;
    }
    #productImage .carousel-item img{
        object-fit: cover;
    }
    .carousel-item{
        height: 400px;
    }
    .carousel-control-prev-icon, .carousel-control-next-icon {
        height: 50px;
        width: 50px;
        outline: black;
        background-color: rgba(0, 0, 0);
        background-size: 100%, 100%;
        border-radius: 50%;
        border: 1px solid black;
    }
    
    .carousel-indicators [data-bs-target]{
        background-color: black;
    }
    #productImage .carousel-indicators button{
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background-color: black;
        opacity: 1;
    }
    #productImage .carousel-indicators .active{
        background-color: white;
    }
    
</style>