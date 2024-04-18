<template>
  <div class="row g-0 auth-page bg-light">
    <article class="col-lg-4 p-lg-5 p-3">
      <figure class="mb-lg-5 mb-3">
        <router-link to="/"
          ><img src="../assets/logo.png" width="50px" alt="Snabel Logo"
        /></router-link>
      </figure>
      <div class="welcome">
        <span class="text-color">Welcome To Snable</span>
        <h3 class="color">Always Remember:</h3>
        <p class="ayat">
          <strong
            lang="ar"
            title="Never will you attain the good [reward] until you spend [in the way of Allah] from that which you love. And whatever you spend - indeed, Allah is Knowing of it."
            >لَن تَنَالُوا الْبِرَّ حَتَّىٰ تُنفِقُوا مِمَّا تُحِبُّونَ ۚ
            <br />وَمَا تُنفِقُوا مِن شَيْءٍ فَإِنَّ اللَّهَ بِهِ عَلِيمٌ<br
          /></strong>
          <em class="text-color">Surah Al Imran: 92</em>
        </p>
      </div>
    </article>
    <article
      class="login d-flex flex-wrap align-content-center justify-content-center shadow col-lg-8"
      style="height: 100vh"
    >
      <!-- <form
        class="w-75 m-auto mt-5"
        enctype="multipart/form-data"
        @submit.prevent="registerUser"
      ></form> -->
      <div>
        <form
          @submit.prevent="onSubmit"
          @reset.prevent="onReset"
          style="width: 500px"
          enctype="multipart/form-data"
          class="mx-auto"
        >
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

          <div v-if="form.images.length > 0">
            <div
              class="mb-3"
              v-for="(image, index) in form.images"
              :key="index"
            >
              <img :src="image.preview" class="img-thumbnail" width="100" />
            </div>
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
                :id="'tag_' + tag.id"
                :value="tag.id"
                v-model="form.tags"
              />
              <label class="form-check-label" :for="'tag_' + tag.id">{{
                tag.name
              }}</label>
            </div>
          </div>
          <button type="submit" class="btn btn-primary me-2">Submit</button>
          <button type="reset" class="btn btn-danger">Reset</button>
        </form>
      </div>
    </article>
  </div>
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
      console.log(this.tags);
    },
    async getCategories() {
      const response = await fetch("http://127.0.0.1:8000/categories/list");
      const data = await response.json();
      this.categories = data;
      this.category = data;
    },
    onSubmit(event) {
      event.preventDefault();
      alert(JSON.stringify(this.form));
      this.submitForm();
    },
    onReset(event) {
      event.preventDefault();
      // Reset our form values
      this.form.title = "";
      this.form.description = "";
      this.form.price = null;
      this.form.images = [];
      // this.form.pictures = this.form.images[0];
      this.form.deadline = [];
      this.form.category = "";
      this.form.tags = [];
      this.form.total_target = "";
      this.form.user = 1;
      // Trick to reset/clear native browser form validation state
      // Trick to reset/clear native browser form validation state
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
    submitForm() {
      const formData = new FormData();

      // Append other form fields
      // formData.append("title", this.project.title);
      // formData.append("description", this.project.description);
      // formData.append("status", this.project.status);
      // Append other form fields
      formData.append("title", this.form.title);
      formData.append("description", this.form.description);
      formData.append("price", this.form.price);
      formData.append("deadline", this.form.deadline);
      formData.append("category", this.form.category);
      formData.append("tags", this.form.tags);
      formData.append("total_target", this.form.total_target);
      formData.append("user", this.form.user);
      formData.append("pictures", this.form.images[0]);

      // Append images
      this.form.images.forEach((file, index) => {
        formData.append(`images_${index}`, file);
      });

      const response = fetch("http://127.0.0.1:8000/projects/", {
        method: "POST",
        body: formData,
      });
      if (response.ok) {
        alert("Project created successfully!");
      } else {
        console.log(response);
        alert("Failed to create project.");
      }

      if (response.ok) {
        alert("Project created successfully!");
      } else {
        alert("Failed to create project.");
      }
    },
  },
};
</script>

<style scoped>
.welcome {
  padding-top: 28px;
}
h3 {
  margin-bottom: 24px;
}
.ayat {
  text-align: center;
  direction: rtl;
  padding-bottom: 40px;
  font-weight: bold;
  color: var(--mainTextColor);
  letter-spacing: 2px;
  word-spacing: 3px;
  font-family: "Reem Kufi", sans-serif;
}
em {
  font-size: 12px;
}
.login {
  border-top-left-radius: 52px;
  background-color: #fff;
}
.signin {
  text-align: right;
}
.submit {
  position: fixed;
  right: 0;
  bottom: 0;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: flex-end;
  background-color: #fff;
  padding: 25px;
  border-top: 1px solid #e2e2e2;
}
form input {
  color: var(--mainColor);
}
form input:focus {
  caret-color: var(--mainColor);
  color: var(--mainTextColor);
}
form label {
  color: var(--mainColor);
}
.icon {
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  color: var(--mainColor);
}
.social {
  padding-bottom: 150px;
}
.social p::before {
  content: "";
  position: absolute;
  height: 1px;
  width: 40%;
  top: 50%;
  left: 3%;
  transform: translateY(50%);
  border: 1px solid #8f8f8f48;
}
.social p::after {
  content: "";
  position: absolute;
  height: 1px;
  width: 40%;
  top: 50%;
  right: 3%;
  transform: translateY(50%);
  border: 1px solid #8f8f8f48;
}
.social-platforms a {
  color: #fff;
  border-radius: 8px;
  display: inline-block;
}
.social-platforms i {
  padding: 12px;
  width: 40px;
}
.social-platforms span {
  padding: 12px;
  width: 200px;
  display: inline-block;
  border-radius: 8px;
}
.social-platforms li:first-child a {
  background-color: #c53329;
}
.social-platforms li:first-child span {
  background-color: #f44235;
  border-left: 1px solid #e76464;
}
.social-platforms li:last-child a {
  background-color: #3a5998;
}
.social-platforms li:last-child span {
  background-color: #243b68;
  border-left: 1px solid #4666a7;
}

@media screen and (max-width: 992px) {
  .login {
    border-top-right-radius: 52px;
  }
}
@media screen and (max-width: 576px) {
  form {
    width: 100% !important;
    padding-right: 16px;
    padding-left: 16px;
  }
  .submit {
    position: static;
    justify-content: center;
  }
  .social {
    padding-bottom: 0;
  }
}
</style>

<!-- <script>
import { useAuthenticationStore } from "../stores/auth";
export default {
  name: "LoginComponent",
  data: () => ({
    authenticationStore: useAuthenticationStore(),
    user: {
      username: "",
      password: "",
    },
    errorMessages: {},
    successMessages: "",
  }),
};
</script> -->
