import { defineStore } from "pinia";

export const useTagStore = defineStore("tag", {
  state: () => ({
    baseURL: `http://localhost:8000`,
    tags: [],
  }),
  actions: {
    async fetchTags() {
      try {
        let response = await fetch(`${this.baseURL}/tags/list`, {
          method:"GET",
          headers: {
            "Content-Type":"application/json",
          }
        });
        if (!response.ok) {
          throw new Error("Failed To Fetch tags");
        }
        this.tags = await response.json();
      } catch(error) {
        return error;
      }
    },
  },
});
