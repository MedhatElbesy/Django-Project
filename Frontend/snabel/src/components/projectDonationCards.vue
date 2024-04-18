<template>
  <div class="donations-info wrapper row">
    <div class="donation-info col">
      <!-- Amount raised and donors -->
      <p>
        ${{ project.total_collected }} raised of ${{ project.total_target }}
      </p>

      <!-- Progress bar -->
      <div class="progress">
        <div
          class="progress-bar bg-success"
          role="progressbar"
          :style="{
            width: (project.total_collected / project.total_target) * 100 + '%',
          }"
          :aria-valuenow="project.total_collected"
          aria-valuemin="0"
          :aria-valuemax="project.total_target"
        >
          {{ (project.total_collected / project.total_target) * 100 }}%
        </div>
      </div>

      <p>{{ project.donations }} kind-hearted donors</p>
      <!-- Call to action -->
      <p>
        <button class="text-light btn btn-warning d-block w-100 mx-2">
          Donate Now
        </button>
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
      <!-- start donator info row -->

      <div
        class="donator-info row my-2"
        v-for="(payment, index) in projectPayment"
        :key="index"
      >
        <!-- icon -->
        <div class="col-3"><i class="fa-solid fa-hand-holding-dollar"></i></div>
        <div class="col row">
          <span class="donator-name col" style="overflow: hidden">{{
            payment.user_name
          }}</span>
          |
          <span class="donation-amount col">${{ payment.amount }}</span>
        </div>
      </div>
      <!-- end donator info row -->
    </div>
  </div>
</template>

<style scoped>
.donation-info {
  background-color: rgb(243, 241, 241);
  border-radius: 16px;
  padding: 2em;
  max-width: 450px;
}

.btn-warning {
  border-radius: 16px;
  font-weight: bold;
}
.share-icons {
  margin: 1em;
}
.social-icons {
  margin: 1em;
  font-size: x-large;
}
i {
  font-size: larger;
}
</style>

<script>
import { useProjectStore } from "../stores/project";
// import { useRoute } from "vue-router";

export default {
  async setup() {
    // getting project id
    // const route = useRoute();
    const projectStore = useProjectStore();
    const currentProjectID = 1;
    projectStore.setProjectID(currentProjectID);

    // fetching project data by id
    try {
      await projectStore.fetchProjectData();
      let projectPayment = await projectStore.fetchProjectPayment();
      // make project payment = to latest 5
      projectPayment = projectPayment.slice(-5).reverse();
      const project = projectStore.projectData;
      console.log(projectPayment);
      // console.log("Project data:", project);
      // console.log(project);
      return { project, projectID: currentProjectID, projectPayment };
    } catch (error) {
      console.error("Failed to fetch project data:", error);
      return { project: null, projectID: currentProjectID };
    }
  },
};
</script>
