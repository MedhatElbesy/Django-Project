<template {{test()}}>
    <div class="card" style="width: 18rem;">
    <img src="" class="card-img-top" alt="">
    <div class="card-body">
        <h5 class="card-title"> title</h5>
        <p class="card-text">{{name}}</p>
        <input type="range"  default value="10.25">
        <p class="card-text">mony</p>
    </div>
</div>
</template>

<script>
export default {
    data:()=>({
        // all:[],
        name:''

    }),
    methods:{
        // async test(){
        //     let data = await fetch('http://127.0.0.1:8000/payment/list/2');
        //     let jsonData = await data.json()
        //     console.log(jsonData);
        //     // this.all=jsonData;
        //     this.name=jsonData.status;
        
        // }
    },
    async created(){
        try{
            let data = await fetch('http://127.0.0.1:8000/payment/list/2',{
                method:"GET",
                headers:{
                    "Content-Type":"application/json",
                }
            });
            let jsonData = await data.json();
            console.log(jsonData);
        }catch(e){
            console.log(e);
        }
    }
}
</script>

<style>

</style>