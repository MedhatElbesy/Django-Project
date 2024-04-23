<template>
  <div class="w-100 p-0">
    <nav class="row g-0">
      <navbar />
    </nav>
    <section class="d-flex row mx-auto" >
    </section>
    <!-- <card /> -->
    <pay />

    <footer class="row g-0 bg-light">
      <footerComponent />
    </footer>
  </div>
</template>

<script>
import { provide } from "vue";

import navbar from "../components/navComponent.vue";
// import projectDonate from "../components/projectDonationCards.vue";
// import card from "../components/cardComponent.vue";
import pay from "../components/paymentFormComponent.vue";
import footerComponent from "../components/footerComponent.vue";

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
    // card,
    pay,
    footerComponent,
  },
  created() {
    this.fetchProjectData();
  },
  methods: {
    async fetchProjectData() {
      try {
        const projectStore = useProjectStore();
        provide("projectStore", projectStore);
        console.log(projectStore.projectID);
        console.log("hhhhhhh");
        const projectData = await projectStore.fetchProjectData();
        this.project = projectData;
      } catch (error) {
        console.error("Error fetching project data:", error);
      } finally {
        this.loading = false;
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
