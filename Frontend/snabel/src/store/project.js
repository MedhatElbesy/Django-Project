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
        const response = await fetch(
          `http://localhost:8000/projects/${this.projectID}`
        );
        if (!response.ok) {
          throw new Error(
            "Network response was not ok, failed to fetch project data"
          );
        }
        this.projectData = await response.json();
      } catch (error) {
        this.error = error.message;
        console.error(error);
      } finally {
        this.loaded = true;
      }
    },
    setProjectID(projectID) {
      this.projectID = projectID;
    },

    // ...
    //last five Project /latest

    // top rated project 

    // all project 
    // search  ()
  },
});
