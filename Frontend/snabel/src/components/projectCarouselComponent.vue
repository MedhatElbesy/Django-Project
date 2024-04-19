<template>
  <div class="my-3">
    <div
      id="carouselExampleAutoplaying"
      class="carousel slide carousel-fade"
      data-bs-ride="carousel"
    >
      <div class="carousel-inner">
        <!-- v-for="(projectItem, indx) in project"
        :key="indx" -->
        <div
          class="carousel-item"
          :class="{ active: indx === 0 }"
          v-for="(image, indx) in project.images"
          :key="indx"
        >
          <img
            :src="image.image || project.pictures"
            class="d-block w-100"
            alt="..."
          />
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
    <hr class="w-50 mx-auto" />
    <h5 class="h4">Sadaka started by: {{ project.user_name }}</h5>
    <span>{{ project.remaining_days }} days left</span>
    <hr class="w-50 mx-auto" />
    <h5 class="h4">The amazing story about this project</h5>
    <span class="badge bg-primary mx-1"
      ><i class="fa-solid fa-list"> </i> {{ project.category_name }}</span
    >
    <br />
    <span
      v-for="(tag, index) in project.tags_info"
      :key="index"
      class="badge bg-success mx-1"
      ><i class="fa-solid fa-tag"> </i>{{ tag.name }}
    </span>
    <p class="my-3">
      {{ project.description }}
    </p>
  </div>
</template>

<script>
// import { useRoute } from "vue-router";
import { ref, watchEffect, inject } from "vue";

export default {
  async setup() {
    // getting project id
    // const route = useRoute();
    const projectStore = inject("projectStore");
    const projectID = ref(null);
    const loading = ref(false);
    const error = ref(null);
    const projectData = ref({});
    console.log("from child ", projectID);
    console.log("from child carousel ", projectData);
    watchEffect(() => {
      projectID.value = projectStore.projectID;
      projectData.value = projectStore.projectData;
      loading.value = projectStore.loading;
      error.value = projectStore.error;
    });
    // getting id from url
    const currentProjectID = projectID;
    try {
      const project = projectData;
      return { project, projectID: currentProjectID };
    } catch (error) {
      alert("here");
      console.error("Failed to fetch project data:", error);
      return { project: null, projectID: currentProjectID };
    }
  },
};
</script>

<style></style>
