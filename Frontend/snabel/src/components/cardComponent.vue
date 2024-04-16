<template >
    <div class="container my-3 py-2">
        <h2 class="my-5 line">More ways to make a difference.<br> fundraisers inspired by what you care about.</h2>
        <select class="form-select one text-center my-5" aria-label="Default select example">
            <option selected>Close to Goal</option>
            <option value="1">Just Launched</option>
            <option value="2">Needs Momentum</option>
            <option value="3">Happening Worldwide</option>
            <option value="4">Charities</option>
        </select>
        <div class=" d-flex  justify-content-between align-items-center">
            <div class=" second d-flex my-5 ">
                <div class="card mx-2 border-0 " v-for="project in projects" :key="project.id" style="width: 18rem;">
                    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZYdiS6o83xt08rKMnams6WzHDiETtxkYcTg&s" class="card-img-top" alt="">
                    <div class="card-img-overlay">
                        <p class="badge rounded-pill bg-black">test</p>
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">Title{{project.project_title}} </h5>
                        <p class="card-text">Name{{project.user}}</p>
                        <input type="range"  default value="10.25">
                        <p class="card-text">mony</p>
                    </div>
                </div>
            </div>
        </div>
    </div> 
</template>

<script>
export default {
    data:()=>({
        projects:[],


    }),
    methods:{

    },
    async created(){
        try{
            let data = await fetch('http://localhost:8000/payment/list',{
                method:"GET",
                headers:{
                    "Content-Type":"application/json",
                }
            });
            let jsonData = await data.json();
            console.log(jsonData[0]);
            this.projects=jsonData;
        }catch(e){
            console.log(e);
        }
    }
}

</script>

<style scoped>
    /* *{
        padding: 0;
        margin: 0;
        box-sizing: border-box;
    } */
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
    .container{
        background-color: #4e6c8882;
        width: 100%;
        overflow: auto;
        border-radius: 15px;
        
    }
    .container::-webkit-scrollbar {
        display: none;
    }
    .card{
        border-radius: 15px;
        /* background-color: transparent !important; */
        background-color: #4e6c88;
    }
    .card:hover{
        background-color: #4e6c884f;
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