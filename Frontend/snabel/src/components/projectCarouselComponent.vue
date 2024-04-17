<template>
  <div
    id="carouselExampleAutoplaying"
    class="carousel slide carousel-fade"
    data-bs-ride="carousel"
  >
    <div class="carousel-inner">
      <!-- v-for="(projectItem, indx) in project"
        :class="{ active: indx === 0 }"
        :key="indx" -->
      <div class="carousel-item active">
        <img :src="project.pictures" class="d-block w-100" alt="..." />
      </div>
    </div>
    <button
      class="carousel-control-prev"
      type="button"
      data-bs-target="#carouselExampleAutoplaying"
      data-bs-slide="prev"
    >
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button
      class="carousel-control-next"
      type="button"
      data-bs-target="#carouselExampleAutoplaying"
      data-bs-slide="next"
    >
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</template>

<!-- <script>
import { useProjectStore } from "../stores/project";
import { useRoute } from "vue-router";

export default {
  setup() {
    const projectStore = useProjectStore();
    const route = useRoute();
    const currentProjectID = route.params.id || 1; // assuming project ID is in route params

    projectStore.setProjectID(currentProjectID);

    const fetchProjectData = async () => {
      try {
        await projectStore.fetchProjectData();
        return projectStore.projectData;
      } catch (error) {
        console.error("Failed to fetch project data:", error);
        return null;
      }
    };

    return {
      projects: fetchProjectData(),
      projectID: currentProjectID,
    };
  },
};
</script> -->
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

<style></style>
