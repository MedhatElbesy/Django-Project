<template>
    <!-- <div class="container"> -->
        <div class="row"><!--The Parent row  -->
            <div class="col-md-6 p-2">
                <div class="card text-start custom-card">
                    <img class="card-img" src="../assets/1.jpg" alt="Title" />
                    <div class="card-img-overlay">
                        <p class="badge rounded-pill bg-black ">donations</p>
                    </div>
                    <div class="card-body">
                        <h4 class="card-title">Title</h4>
                        <p class="card-text">Body</p>
                        <div class="progress">
                            <div class="progress-bar bg-primary w-25" role="progressbar"  aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">25%</div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-md-6"><!--The Parent div  -->

                <div class="row"><!-- First  Second Row -->

                    <div class="col-md-6 p-2"> <!-- first div in child row-->
                        <div class="card text-start">
                            <img class="card-img" src="../assets/1.jpg" alt="Title" />
                            <div class="card-img-overlay">
                                <p class="badge rounded-pill bg-black">donations</p>
                            </div>
                            <div class="card-body">
                                <h4 class="card-title">Title</h4>
                                <p class="card-text">Body</p>
                                <div class="progress">
                                    <div
                                        class="progress-bar bg-primary" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
                                        25%
                                    </div>
                                </div>
                                
                            </div>
                        </div>
                    </div><!-- end first div in child col-->

                    <div class="col-md-6 p-2"> <!-- first div in child row-->
                        <div class="card text-start">
                            <img class="card-img" src="../assets/1.jpg" alt="Title" />
                            <div class="card-img-overlay">
                                <p class="badge rounded-pill bg-black">donations</p>
                            </div>
                            <div class="card-body">
                                <h4 class="card-title">Title</h4>
                                <p class="card-text">Body</p>
                                <div class="progress">
                                    <div
                                        class="progress-bar bg-primary" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
                                        25%
                                    </div>
                                </div>
                                
                            </div>
                        </div>
                    </div><!-- end first div in child col-->

                    <div class="col-md-6 p-2"> <!-- first div in child row-->
                        <div class="card text-start">
                            <img class="card-img" src="../assets/1.jpg" alt="Title" />
                            <div class="card-img-overlay">
                                <p class="badge rounded-pill bg-black">donations</p>
                            </div>
                            <div class="card-body">
                                <h4 class="card-title">Title</h4>
                                <p class="card-text">Body</p>
                                <div class="progress">
                                    <div
                                        class="progress-bar bg-primary" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
                                        25%
                                    </div>
                                </div>
                                
                            </div>
                        </div>
                    </div><!-- end first div in child col-->
                    
                    <div class="col-md-6 p-2"> <!-- first div in child row-->
                        <div class="card text-start">
                            <img class="card-img" src="../assets/1.jpg" alt="Title" />
                            <div class="card-img-overlay">
                                <p class="badge rounded-pill bg-black">donations</p>
                            </div>
                            <div class="card-body">
                                <h4 class="card-title">Title</h4>
                                <p class="card-text">Body</p>
                                <div class="progress">
                                    <div
                                        class="progress-bar bg-primary" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
                                        25%
                                    </div>
                                </div>
                                
                            </div>
                        </div>
                    </div><!-- end first div in child col-->

                </div><!-- end  Second Row -->


            </div><!--End The Parent div  -->
        </div><!-- end The Parent row  -->
    <!-- </div> --> <!-- end The container  -->
</template>

<script>
// import axios from 'axios';
export default {
    name: 'lastProjectComponent',
    data() {
        return {
            lastProjects: []
        }
    },
    methods: {
        
    },
    // async created() {
    //     try{
    //         let projects  = await fetch('http://localhost:8000/projects/latest',{
    //             method: "GET",
    //             headers:{
    //                 "Content-Type": "application/json",
    //             }
    //         });
    //         this.lastProjects = await projects.json();
    //         // console.log(this.lastProjects[0].pictures);
    //         console.log(this.lastProjects);
    //     }catch(err){
    //         console.log(err);
    //     }
    // }
    async created() {
        try{
            let projects  = await fetch('http://localhost:8000/projects/latest',{
                method: "GET",
                headers:{
                    "Content-Type": "application/json",
                }
            });
            this.lastProjects = await projects.json();
            // console.log(this.lastProjects[0].pictures);
            console.log(this.lastProjects);
        }catch(err){
            console.log(err);
        }
    }
}
</script>

<style scoped>

.card{
    cursor: pointer;
    overflow: hidden;
}
.custom-card {
    height: 615px;
}
.custom-card img{
    z-index: 1;
}
.custom-card .card-img-overlay{
    z-index: 2;
}
.card:hover img {
    transform: scale(1.1);
}
.card img {
    transition: all 0.5s ease;
}
</style>