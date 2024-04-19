import { defineStore } from "pinia";

export const useCategoryStore = defineStore("category", {
  state: () => ({
    baseURL: `http://localhost:8000`,
    categories: [],
  }),
  actions: {
    async fetchCategories() {
      try {
        let response = await fetch(`${this.baseURL}/categories/list`, {
          method:"GET",
          headers: {
            "Content-Type":"application/json",
          }
        });
        if (!response.ok) {
          throw new Error("Failed To Fetch Categories");
        }
        this.categories = await response.json();
      } catch(error) {
        return error;
      }
    },
  },
});
