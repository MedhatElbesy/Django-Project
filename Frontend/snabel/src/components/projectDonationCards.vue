<template>
  <div class="donations-info wrapper row">
    <div class="donation-info col">
      <!-- Amount raised and donors -->
      <p>
        ${{ project.total_collected }} raised of ${{ project.total_target
        }}<br />1,121 kind-hearted donors
      </p>

      <!-- Progress bar -->
      <p class="progress-bar">
        <label for="file">Donation progress:</label>
        <progress
          id="file"
          value="{{ project.total_collected }}"
          max="{{ project.total_target }}"
        >
          32%
        </progress>
      </p>

      <!-- Call to action -->
      <p>
        <button class="btn btn-warning">Donate Now</button>
      </p>

      <!-- Share icons -->
      <p class="share-icons">
        <!-- Copy, Facebook, Twitter, Email -->
        <span>Help us by spreading the word!</span>
        <i class="fa fa-copy" aria-hidden="true" title="Copy"></i>
        <i class="fa fa-facebook" aria-hidden="true" title="Facebook"></i>
        <i class="fa fa-twitter" aria-hidden="true" title="Twitter"></i>
        <i class="fa fa-envelope" aria-hidden="true" title="Email"></i>
      </p>
      <p class="recent-donations">
        <!-- Recent donations -->
        <i class="fa-solid fa-tower-broadcast"></i>
        <span> 295 Recent Donations</span>
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

<style scoped>
/* Add your scoped styles here */
</style>

<script>
import { useProjectStore } from "../stores/project";
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
