import { defineStore } from "pinia";

export const useProjectStore = defineStore("project", {
  state: () => ({
    baseURL: `http://localhost:8000`,
    projectData: null,
    projectID: null,
    loaded: false,
    error: null,
  }),
  actions: {
    async fetchProjectData() {
      let response;
      try {
        // response = await fetch(`${this.baseURL}/projects/${this.projectID}`);
        response = await fetch(`${this.baseURL}/projects/9`);

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
        // eslint-disable-next-line no-unsafe-finally
        return this.projectData;
      }
    },
    setProjectID(projectID) {
      this.projectID = projectID;
    },

    async fetchProjectPayment() {
      try {
        const response = await fetch(
          `${this.baseURL}/payment/listByProject/${this.projectID}`
        );
        if (!response.ok) {
          throw new Error(
            "Network response was not ok, failed to fetch project payment"
          );
        }
        return response.json();
      } catch (error) {
        console.log(error);
      }
    },
    // ...
    // top rated project
    //last five Project /latest
    async topRated() {
      try {
        const response = await fetch(`${this.baseURL}/ratings`);
        if (!response.ok) {
          throw new Error(
            "Network response was not ok, failed to fetch highest rated"
          );
        }
        return response.json();
      } catch (error) {
        console.log(error);
      }
    },
    async latest() {
      try {
        const response = await fetch(`${this.baseURL}/projects/latest`);
        if (!response.ok) {
          throw new Error(
            "Network response was not ok, failed to fetch project payment"
          );
        }
        return response.json();
      } catch (error) {
        console.log(error);
      }
    },

    // all project
    async allProject() {
      try {
        const response = await fetch(`${this.baseURL}/projects/`);
        if (!response.ok) {
          throw new Error(
            "Network response was not ok, failed to fetch all projects"
          );
        }
        return response.json();
      } catch (error) {
        console.log(error);
      }
    },
    // search  ()
  },
});
