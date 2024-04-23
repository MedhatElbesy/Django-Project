<template >
    <div class="row my-3 py-2 justify-content-center justify-content-md-start ">
        <h2 class="my-5 line m-0 mx-md-4 mx-lg-5 ">More ways to make a difference.<br class="d-none d-md-block "> fundraisers inspired by what you care about.</h2>
        <select v-model="selectedOption" class="form-select one text-center my-5  mx-sm-auto mx-md-4 mx-lg-5" aria-label="Default select example" @change="fetchData">
            <option value="close_to_goal">Close to Goal</option>
            <option value="just_launched">Just Launched</option>
            <option value="top_rated">Top Rated</option>
        </select>
        <div class=" d-flex  justify-content-between align-items-center">
            <div class=" second d-flex my-5 ">
                <div class="card mx-2 border-0 " v-for="project in projetInfo" :key="project.id" style="width: 18rem;" >
                    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZYdiS6o83xt08rKMnams6WzHDiETtxkYcTg&s" class="card-img-top" alt="">
                    <div class="card-img-overlay">
                        <p class="badge rounded-pill bg-black">{{ project.donations }} donors</p>
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">This Donation For {{project.user_name}} </h5>
                        <!-- <p class="card-text">Name{{project.user}}</p> -->
                        <div class="progress">
                            <div class="progress-bar" role="progressbar" :style="{ width: (project.total_collected / project.total_target) * 100 + '%',}" :aria-valuenow="project.total_collected" aria-valuemin="0" :aria-valuemax="project.total_target">{{ (project.total_collected / project.total_target) * 100 }} %</div>
                        </div>
                        <p class="card-text">{{project.total_collected}} Raised</p>
                    </div>
                </div>
            </div>
        </div>
    </div> 
</template>

<script>
    import { useProjectStore } from "../stores/project";
// import { useRoute } from "vue-router";
// import { inject, watchEffect, ref } from "vue";

    export default {
        data:()=>({
            selectedOption: "close_to_goal",
            heighRate:{},
            projetInfo:{},
            
        }),
        methods:{
            // toDonate(){
            //     const router = useRoute();
            //         router.push({ name: 'payment', params: { id: this.projetInfo.id } });
            // },


            async fetchData() {
                try {
                    const myStore = useProjectStore();
                    if (this.selectedOption == "just_launched"){
                        const lunched = await myStore.latest();
                        this.projetInfo = lunched;
                    }else if(this.selectedOption == "top_rated"){
                        let topRated = await myStore.allProject();
                        topRated.sort((a, b) => b.get_project_rating - a.get_project_rating);
                        this.projetInfo = topRated.slice(0, 5);
                    }else{
                        const paymentData = await myStore.allProject();
                        this.projetInfo = paymentData;
                    }
                    // const topRatedData = await myStore.topRated();
                    // this.heighRate = topRatedData.results;
                } catch (error) {
                    console.error('Error fetching data:', error);
                }
                // const topRatedData = await myStore.topRated();
                // this.heighRate = topRatedData.results;
            // } catch (error) {
            //     console.error('Error fetching data:', error);
            }
        },
        async created(){
            this.fetchData();
        },
    }
</script>

<style scoped>
    .one{
        border-radius: 20px;
        left: 0; 
        width: fit-content;
        font-weight: bold;
        position:sticky;
    }
    option{
        font-weight:400;
    }
    .row{
        background-color:#198754;
        width: auto; 
        overflow: auto;
        border-radius: 15px;
    }
    .row::-webkit-scrollbar {
        display: none;
    }
    .card{
        border-radius: 15px;
        background-color:#198754;
    }
    .card:hover{
        background-color: rgba(78, 108, 136, 0.158);
        -webkit-box-shadow: -1px 9px 18px 0px rgba(0,0,0,0.75);
        -moz-box-shadow: -1px 9px 18px 0px rgba(0,0,0,0.75);
        box-shadow: -1px 9px 18px 0px rgba(0,0,0,0.75);
    }
    img{
        border-radius: 15px;
    }
    .line{
        position: sticky;
        left: 0; 
    }
</style>