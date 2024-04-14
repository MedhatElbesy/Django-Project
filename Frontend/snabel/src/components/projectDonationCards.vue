<template>
  <div class="donations-info wrapper row">
    <div class="donation-info col">
      <!-- Amount raised and donors -->
      <p>
        ${{ project.total_collected }} raised of ${{ project.total_target }}
      </p>

      <!-- Progress bar -->
      <p class="progress-bar">
        <label for="donation-progress">Donation progress:</label>
        <progress
          id="donation-progress"
          :value="project.total_collected"
          :max="project.total_target"
        >
          {{ (project.total_collected / project.total_target) * 100 }}%
        </progress>
      </p>
      <p>{{ project.donations }} kind-hearted donors</p>
      <!-- Call to action -->
      <p>
        <button class="btn btn-warning d-block w-100 mx-2">Donate Now</button>
      </p>

      <!-- Share icons -->
      <div class="share-icons">
        <!-- Copy, Facebook, Twitter, Email -->
        <span class="d-flex">Help us by spreading the word!</span>
        <p class="d-flex justify-content-around social-icons">
          <i class="fa fa-copy" aria-hidden="true" title="Copy"></i>
          <i class="fa-brands fa-facebook"></i>
          <i class="fa-brands fa-x-twitter"></i>
          <i class="fa fa-envelope" aria-hidden="true" title="Email"></i>
        </p>
      </div>
      <p class="recent-donations">
        <!-- Recent donations -->
        <i class="fa-solid fa-tower-broadcast"></i>
        <span> Recent Donations </span>
        <!-- from payments pinia store -->
      </p>

      <div class="donator-info row">
        <!-- icon -->
        <div class="col-3"><i class="fa-solid fa-hand-holding-dollar"></i></div>
        <div class="col">
          <p class="donator-name">John Doe</p>
          <p class="donation-amount">$121,569</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>

<script>
import { useProjectStore } from "../store/project";
import { useRoute } from "vue-router";

export default {
  async setup() {
    const route = useRoute();
    const projectStore = useProjectStore();
    const currentProjectID = route.params.id;
    projectStore.setProjectID(currentProjectID);
    try {
      await projectStore.fetchProjectData();

      const project = projectStore.projectData;
      console.log("Project data:", project);
      console.log(project);
      return { project, projectID: currentProjectID };
    } catch (error) {
      console.error("Failed to fetch project data:", error);
      return { project: null, projectID: currentProjectID };
    }
  },
};
</script>

<style></style>
