<template>
    <div>
        <nav class="row g-0">
            <navbar />
        </nav>
        <section class="d-flex">
            <div class="border border-2 border-danger col-8 medhat">

            </div>
            <Suspense>
            <template #default>
            <projectDonate/>
            </template>
            <template #fallback>
            <div>Loading...</div>
            </template>
        </Suspense>
        </section>
        <card/>
        <pay/>
        <footer class="row g-0 bg-light">
            <footerComponent />
        </footer>
    </div>
    
</template>

<script>
import navbar from "../components/navComponent.vue"
import projectDonate from "../components/projectDonationCards.vue"
import card from "../components/cardComponent.vue"
import pay from "../components/paymentFormComponent.vue"
import footerComponent from "../components/footerComponent.vue"
export default {
    data:()=>({
        

    }),
    components:{
        navbar,
        projectDonate,
        card,
        pay,
        footerComponent
    },

}
</script>

<style>
.medhat{
    height: 200px;
}
</style>