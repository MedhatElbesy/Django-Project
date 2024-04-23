// v1 before refractor
// import { defineStore } from "pinia";

// export const useProjectStore = defineStore("project", {
//   state: () => ({
//     baseURL: `http://localhost:8000`,
//     projectData: null,
//     projectID: null,
//     loaded: false,
//     error: null,
//   }),
//   actions: {
//     async fetchProjectData() {
//       let response;
//       try {
//         let id = this.projectID;
//         response = await fetch(`${this.baseURL}/projects/${id}`);
//         // response = await fetch(`${this.baseURL}/projects/`);

//         if (!response.ok) {
//           throw new Error(
//             "Network response was not ok, failed to fetch project data"
//           );
//         }
//         this.projectData = await response.json();
//       } catch (error) {
//         this.error = error.message;
//         console.error(error);
//       } finally {
//         this.loaded = true;
//         // eslint-disable-next-line no-unsafe-finally
//         return this.projectData;
//       }
//     },
//     setProjectID(projectID) {
//       this.projectID = projectID;
//     },

//     async fetchProjectPayment() {
//       try {
//         const response = await fetch(
//           `${this.baseURL}/payment/listByProject/${this.projectID}`
//         );
//         if (!response.ok) {
//           throw new Error(
//             "Network response was not ok, failed to fetch project payment"
//           );
//         }
//         return response.json();
//       } catch (error) {
//         console.log(error);
//       }
//     },
//     // ...
//     // top rated project
//     //last five Project /latest
//     async topRated() {
//       try {
//         const response = await fetch(`${this.baseURL}/ratings`);
//         if (!response.ok) {
//           throw new Error(
//             "Network response was not ok, failed to fetch highest rated"
//           );
//         }
//         return response.json();
//       } catch (error) {
//         console.log(error);
//       }
//     },
//     async latest() {
//       try {
//         const response = await fetch(`${this.baseURL}/projects/latest`);
//         if (!response.ok) {
//           throw new Error(
//             "Network response was not ok, failed to fetch project payment"
//           );
//         }
//         return response.json();
//       } catch (error) {
//         console.log(error);
//       }
//     },

//     // all project
//     async allProject() {
//       try {
//         const response = await fetch(`${this.baseURL}/projects/`);
//         if (!response.ok) {
//           throw new Error(
//             "Network response was not ok, failed to fetch all projects"
//           );
//         }
//         return response.json();
//       } catch (error) {
//         console.log(error);
//       }
//     },
//     // search  ()
//   },
// });
import { defineStore } from "pinia";

export const useProjectStore = defineStore("project", {
  state: () => ({
    baseURL: `http://localhost:8000`,
    projectData: {},
    projectID: null,
    loaded: false,
    error: null,
  }),
  actions: {
    async fetchProjectData() {
      try {
        // let id = this.projectID;
        this.projectID = 1;
        const response = await fetch(
          `${this.baseURL}/projects/${this.projectID}`
        );
        if (!response.ok) {
          throw new Error("Failed to fetch project data");
        }
        this.projectData = await response.json();
        return this.projectData;
      } catch (error) {
        this.error = error.message;
        console.error(error);
        throw error;
      } finally {
        this.loaded = true;
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
          throw new Error("Failed to fetch project payment");
        }
        return response.json();
      } catch (error) {
        console.log(error);
        throw error;
      }
    },
    async topRated() {
      try {
        const response = await fetch(`${this.baseURL}/ratings`);
        if (!response.ok) {
          throw new Error("Failed to fetch highest rated");
        }
        return response.json();
      } catch (error) {
        console.log(error);
        throw error;
      }
    },
    async latest() {
      try {
        const response = await fetch(`${this.baseURL}/projects/latest`);
        if (!response.ok) {
          throw new Error("Failed to fetch latest projects");
        }
        return response.json();
      } catch (error) {
        console.log(error);
        throw error;
      }
    },
    async allProject() {
      try {
        const response = await fetch(`${this.baseURL}/projects/`);
        if (!response.ok) {
          throw new Error("Failed to fetch all projects");
        }
        return response.json();
      } catch (error) {
        console.log(error);
        throw error;
      }
    },
  },
});
