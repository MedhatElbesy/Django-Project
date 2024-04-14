<template>
    <div class="container">
        <div class="row"><!--The Parent row  -->
            <div class="col-md-6">
                <div class="card text-start position-relative">
                    <img class="card-img" src="../assets/1.jpg" alt="Title" />
                    <div class="card-img-overlay">
                        <p class="position-absolute top-50 badge rounded-pill bg-secondary">donations</p>
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

                    <div class="col-md-6"> <!-- first div in child row-->
                        <div class="card text-start position-relative ">
                            <img class="card-img" src="../assets/1.jpg" alt="Title" />
                            <div class="card-img-overlay">
                                <p class="position-absolute donation-position badge rounded-pill bg-secondary">donations</p>
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
                    </div><!-- end first div in child row-->

                    <div class="col-md-6"><!-- second div in child row-->
                        <div class="card text-start position-relative ">
                            <img class="card-img" src="../assets/1.jpg" alt="Title" />
                            <div class="card-img-overlay">
                                <p class="position-absolute donation-position badge rounded-pill bg-secondary">donation</p>
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
                    </div><!-- end second div in child row-->
                    
                </div><!-- end  Second Row -->

                <div class="row"> <!-- Third Row in Div -->

                    <div class="col-md-6">
                        <div class="card text-start position-relative ">
                            <img class="card-img" src="../assets/1.jpg" alt="Title" />
                            <div class="card-img-overlay">
                                <p class="position-absolute donation-position badge rounded-pill bg-secondary">donation</p>
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
                    </div>

                    <div class="col-md-6">
                        <div class="card text-start position-relative ">
                            <img class="card-img" src="../assets/1.jpg" alt="Title" />
                            <div class="card-img-overlay">
                                <p class="position-absolute donation-position badge rounded-pill bg-secondary">donation</p>
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
                    </div>
                </div>

            </div><!--End The Parent div  -->
        </div><!-- end The Parent row  -->
    </div><!-- end The container  -->
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
    async created() {
        try{
            let projects  = await fetch('http://localhost:8080/projects/latest',{
                method: "GET",
                headers:{
                    "Content-Type": "application/json",
                }
            });
            let pro = await projects.json();
            console.log(pro);
        }catch(err){
            console.log(err);
        }
    }
}
</script>

<style scoped>
.top-50{
    top: 61% !important;
}
.donation-position{
    top: 45% !important; 
}
</style>