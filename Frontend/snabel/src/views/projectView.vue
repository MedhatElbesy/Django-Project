<template>
  <div class="w-100">
    <!-- <nav class="row g-0">
      <navbar />
    </nav> -->
    <section class="d-flex row mx-auto" style="width: 90%">
      <h1 class="col-12 my-5 d-flex justify-content-between">
        <p>{{ project.title }}</p>

        <button
          data-bs-toggle="modal"
          data-bs-target="#reportModal"
          data-bs-objectType="project"
          :data-bs-id="project.id"
          class="text-danger btn report-flag"
        >
          <i class="fa-solid fa-flag report-flag"></i>
        </button>
      </h1>
      <h5 class="col-12 h5">{{ project.get_project_rating }} / 5 Stars!</h5>
      <div class="col-8">
        <Suspense>
          <template #default>
            <div class="">
              <projectCarouselComponent />
            </div>
          </template>
          <template #fallback>
            <div>Loading...</div>
          </template>
        </Suspense>
        <Suspense>
          <template #default>
            <div class="my-4">
              <projectCommentsComponent />
            </div>
          </template>
        </Suspense>
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
    <reportModal />
    <!-- <footer class="row g-0 bg-light">
      <footerComponent />
    </footer> -->
  </div>
</template>

<script>
import { provide } from "vue";

// import navbar from "../components/navComponent.vue";
// import navbarResp from "../components/navRespComponent.vue";
import projectDonate from "../components/projectDonationCards.vue";
import card from "../components/cardComponent.vue";
// import pay from "../components/paymentFormComponent.vue";
// import footerComponent from "../components/footerComponent.vue";
import projectCommentsComponent from "@/components/projectCommentsComponent.vue";
import projectCarouselComponent from "../components/projectCarouselComponent.vue";
import { useProjectStore } from "@/stores/project"; // Import the project store

import reportModal from "../components/reportModal.vue";

export default {
  data: () => ({
    project: {
      title: "loading",
      user: JSON.parse(sessionStorage.user).user,
    },
    object_id: null,
    content_object: null,
    loading: true, // Add loading state to track data loading status
  }),
  components: {
    // navbar,
    projectDonate,
    card,
    // pay,
    // footerComponent,
    projectCommentsComponent,
    projectCarouselComponent,
    reportModal,
  },
  created() {
    this.fetchProjectData();
  },
  methods: {
    async fetchProjectData() {
      try {
        const projectStore = useProjectStore();
        projectStore.projectID = this.$route.params.id;
        provide("projectStore", projectStore);
        // console.log(projectStore.projectID);
        const projectData = await projectStore.fetchProjectData();
        this.project = projectData;
      } catch (error) {
        console.error("Error fetching project data:", error);
      } finally {
        this.loading = false;
      }
    },
    async makeReport() {
      const reason = document.querySelector("#reason").value;
      const requestObject = {
        object_id: this.project.id,
        content_type: this.objectType,
        reason: reason,
        user: JSON.parse(sessionStorage.user).user.id,
      };
      const respons = fetch("http://localhost:8000/api/reports/create", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${JSON.parse(sessionStorage.getItem("user")).token}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify(requestObject),
      });
      console.log(respons);
    },
  },
  mounted() {
    // Adds event to the modal to set the id, content
    const reportModal = document.querySelector("#reportModal");
    console.log(reportModal);
    if (reportModal) {
      reportModal.addEventListener("show.bs.modal", (event) => {
        // Button that triggered the modal
        const button = event.relatedTarget;
        this.objectType = button.getAttribute("data-bs-objectType");
        this.object_id = button.getAttribute("data-bs-id");
      });
    }

    // add click event to report button
    const reportBtn = document.querySelector("#reportButton");
    if (reportBtn) {
      reportBtn.addEventListener("click", this.makeReport);
    }
  },
};
</script>

<style>
.report-flag il {
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  font-size: large;
}
.report-flag:hover {
  color: #ea5252;
}
</style>
