import { defineStore } from "pinia";

export const useProjectStore = defineStore("project", {
  state: () => ({
    projectData: null,
    projectID: null,
    loaded: false,
    error: null,
  }),
  actions: {
    async fetchProjectData() {
      try {
        const response = fetch(`localhost:8000/${this.projectID}`);
        if (!response.ok) {
          throw new Error(
            "Network response was not ok, failed to fetch project data"
          );
        }
        this.projectData = await response.json();
      } catch (error) {
        console.log(error);
      } finally {
        this.loaded = true;
      }
    },
    // ...
  },
  setProjectID(projectID) {
    this.projectID = projectID;
  },
  //   getters: () => ({

  //   }),
});
