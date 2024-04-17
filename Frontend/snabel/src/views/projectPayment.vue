<template>
  <div class="w-100">
    <nav class="row g-0">
      <navbar />
    </nav>
    <section class="d-flex row mx-auto" style="width: 90%">
      <h1 class="col-12 my-5">
        {{ project.title }}
      </h1>
      <div class="col-8">
        <projectCommentsComponent />
      </div>
      <div class="col-4">
        <Suspense>
          <template #default>
            <!-- <div style="height: 70vh; position: sticky; top: 50px"> -->
            <projectDonate />
            <!-- </div> -->
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
    project: {
      title: "loading",
    },
    loading: true, // Add loading state to track data loading status
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
    this.fetchProjectData();
  },
  methods: {
    async fetchProjectData() {
      try {
        const projectData = await useProjectStore().fetchProjectData();
        this.project = projectData;
      } catch (error) {
        console.error("Error fetching project data:", error);
      } finally {
        this.loading = false; // Set loading state to false when data fetching is complete
      }
    },
  },
};
</script>

<style>
.medhat {
  height: 200px;
}
</style>
