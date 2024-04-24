<template>
        <form
          @submit.prevent="onSubmit"
          @reset.prevent="onReset"
          style="width: 500px"
          enctype="multipart/form-data"
          action="http://127.0.0.1:8000/projects/"
          method="POST"
          class="w-75 m-auto my-5"
        >
        <h3 class="text-center my-5 color">Add New Project</h3>
          <div class="form-floating mb-3">
            <input
              type="text"
              class="form-control"
              id="input-title"
              v-model="form.title"
              required
              placeholder="Title"
            />
            <label for="input-title">Title</label>
          </div>

          <div class="form-floating mb-3">
            <textarea
              class="form-control"
              id="input-description"
              v-model="form.description"
              required
              placeholder="Description"
            ></textarea>
            <label for="input-description">Description</label>
          </div>

          <div class="form-floating mb-3">
            <input
              type="number"
              name="total_target"
              class="form-control"
              id="target"
              v-model="form.total_target"
              step="0.01"
              required
              placeholder="Target"
            />
            <label for="target">Target</label>
          </div>

          <div class="mb-3">
            <input
              type="file"
              name="images"
              class="form-control"
              id="input-images"
              multiple
              accept="image/*"
              @change="handleFileChange"
              required
            />
            <label for="input-images" class="form-label mt-1">images</label>
          </div>

          <div v-if="form.images.length > 0">
            <div
              class="mb-3"
              v-for="(image, index) in form.images"
              :key="index"
            >
              <img :src="image.preview" class="img-thumbnail" width="100" />
            </div>
          </div>
          <div class="mb-3">
            <input
              type="file"
              class="form-control"
              id="input-video"
              multiple
              accept=" video/*"
              placeholder="Video"
              @change="handleFileChange"
            />
            <label for="input-video" class="form-label mt-1">Video</label>
          </div>
          <div class="form-floating mb-3">
            <input
              type="date"
              name="deadline"
              format="yyyy-MM-dd"
              class="form-control"
              v-model="form.deadline"
              id="deadline"
              required
            />
            <label for="deadline">Deadline</label>
          </div>

          <!-- <div> -->
          <div class="form-group mb-3">
            <label for="category">Category</label>
            <select
              class="form-select"
              id="category"
              v-model="form.category"
              required
            >
              <option value="">Select Category</option>
              <option
                v-for="category in categories"
                :key="category.id"
                :value="category.id"
              >
                {{ category.name }}
              </option>
            </select>
          </div>

          <div class="form-group mb-3">
            <label>Tags</label><br />
            <div
              v-for="tag in tags"
              :key="tag.id"
              class="form-check form-check-inline"
            >
              <input
                type="checkbox"
                class="form-check-input"
                :id="tag.id"
                :value="tag.id"
                v-model="form.tags"
              />
              <label class="form-check-label" :for="'tag_' + tag.id">{{
                tag.name
              }}</label>
            </div>
          </div>
          <div class="actions text-center my-5">
            <button type="submit" class="btn btn-primary me-2">Add Project</button>
            <button type="reset" class="btn btn-danger">Reset</button>
          </div>
        </form>
</template>

<script>
export default {
  data() {
    return {
      categories: [], // initialize categories array
      tags: ["loading.."],
      form: {
        title: "",
        description: "",
        price: null,
        images: [],
        pictures: "",
        deadline: [],
        category: "", // store selected category ID here
        total_target: "",
        tags: [],
        user: 1,
      },
      show: true,
    };
  },
  mounted() {
    this.getTags();
    this.getCategories();
  },
  methods: {
    async getTags() {
      const response = await fetch("http://127.0.0.1:8000/tags/list");
      const data = await response.json();
      this.tags = data;
      // console.log(this.tags);
    },
    getCheckedCheckboxIds() {
      const checkboxes = document.querySelectorAll(
        'input[type="checkbox"]:checked'
      );
      const checkboxIds = [];

      checkboxes.forEach((checkbox) => {
        checkboxIds.push(checkbox.id);
      });
      console.log("Tags: ", checkboxIds);
      return checkboxIds;
    },
    async getCategories() {
      const response = await fetch("http://127.0.0.1:8000/categories/list");
      const data = await response.json();
      this.categories = data;
      this.category = data;
    },
    onSubmit() {
      // event.preventDefault();
      // alert(JSON.stringify(this.form));
      this.submitForm();
    },
    onReset(event) {
      event.preventDefault();
      // Reset our form values
      this.form.title = "";
      this.form.description = "";
      this.form.price = null;
      this.form.images = [];
      this.form.deadline = [];
      this.form.category = "";
      this.form.tags = [];
      this.form.total_target = "";
      this.form.user = 1;
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
    handleFileChange(event) {
      const files = event.target.files;
      this.form.images = Array.from(files);
      console.log(this.form);
    },
    async submitForm() {
      const formData = new FormData();

      // Append other form fields
      // append data
      formData.append("title", this.form.title);
      formData.append("description", this.form.description);
      // formData.append("price", this.form.price);
      formData.append("deadline", this.form.deadline);
      formData.append("category", this.form.category);
      // formData.append("tags", this.form.tags);
      formData.append("total_target", this.form.total_target);
      formData.append("user", this.form.user);
      for (let index = 0; index < this.form.images.length; index++) {
        formData.append("images", this.form.images[index]);
      }

      this.form.tags = this.getCheckedCheckboxIds();

      this.form.tags.forEach((tag) => {
        formData.append("tags", tag);
      });
      this.form.pictures = this.form.images[0];
      formData.append("pictures", this.form.pictures);
      
      const token = JSON.parse(sessionStorage.getItem("user")).token;

      const response = await fetch("http://127.0.0.1:8000/projects/", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
        method: "POST",
        body: formData,
      });
      if (response.ok) {
        alert("Project created successfully!");
      } else {
        console.log("************", this.form);
        alert("Failed to create project.");
      }
    },
  },
};
</script>

<style>

</style>