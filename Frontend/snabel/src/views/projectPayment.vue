<template>
  <div class="w-100">
    <nav class="row g-0">
      <navbar />
    </nav>
    <section class="d-flex row mx-auto" style="width: 90%">
      <h1 class="col-12 my-5">
        {{ project.title }}
      </h1>
      <div class="border border-2 border-danger col-8 medhat">
        <projectCommentsComponent />
      </div>
      <div class="col-4">
        <Suspense>
          <template #default>
            <projectDonate />
          </template>
          <template #fallback>
            <div>Loading...</div>
          </template>
        </Suspense>
      </div>
    </section>
    <card />
    <pay />

    <footer class="row g-0 bg-light">
      <footerComponent />
    </footer>
  </div>
</template>

<script>
import navbar from "../components/navComponent.vue";
import projectDonate from "../components/projectDonationCards.vue";
import card from "../components/cardComponent.vue";
import pay from "../components/paymentFormComponent.vue";
import footerComponent from "../components/footerComponent.vue";
import projectCommentsComponent from "@/components/projectCommentsComponent.vue";
import { useProjectStore } from "@/stores/project"; // Import the project store

export default {
  data: () => ({
    project: {},
  }),
  components: {
    navbar,
    projectDonate,
    card,
    pay,
    footerComponent,
    projectCommentsComponent,
  },
  created() {
    const project = useProjectStore().projectData;
    this.project = project;
  },
};
</script>

<style>
.medhat {
  height: 200px;
}
</style>
