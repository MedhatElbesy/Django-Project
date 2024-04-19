<template>
  <!-- <h1>hi</h1> -->
  <section class="comments-container">
    <div
      class="comment row d-flex align-baseline my-2"
      v-for="comment in comments"
      :key="comment.id"
    >
      <div class="col-2">
        <!-- use user image here -->
        <img
          class="d-block mx-auto my-2"
          style="width: 50px; height: 50px; border-radius: 50%"
          src="https://upload.wikimedia.org/wikipedia/en/b/b1/Portrait_placeholder.png"
          alt=""
        />
      </div>
      <div class="col-10">
        <h3>{{ comment.user_name }}</h3>
        <p>{{ comment.comment }}</p>
      </div>
    </div>
    <form @submit.prevent class="form">
      <label class="form-label" for="comment"
        >Say something about this project!</label
      >
      <br />
      <input class="form-control" type="text" name="comment" id="comment" />
      <input
        class="form-control"
        type="hidden"
        name="projec"
        id="project"
        :value="projectID"
      />

      <br />
      <input
        class="btn btn-success text-light"
        type="submit"
        value="Submit"
        @click="handleSubmit"
      />
    </form>
  </section>
</template>

<!-- <script>
import { ref, watchEffect, inject } from "vue";
export default {
  data() {
    return {
      comments: [],
    };
  },
  methods: {
    async handleSubmit() {
      const comment = document.querySelector("#comment").innerText;
      const project = document.querySelector("input[name='project']").value;
      const response = await fetch("http://localhost:8000/comments/create/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          comment: comment,
          project: project,
        }),
      });
      if (response.ok) {
        const data = await response.json();
        console.log(data);
      }
      window.location.reload();
    },
  },
  setup() {
    const projectStore = inject("projectStore");
    const projectID = ref(null);
    console.log("from child ", projectID);
    watchEffect(() => {
      projectID.value = projectStore.projectID;
    });
    // getting id from url
    const currentProjectID = projectID;
    try {
      return { projectID: currentProjectID };
    } catch (error) {
      alert("here");
      console.error("Failed to fetch project data:", error);
      return { project: null, projectID: currentProjectID };
    }
  },
  computed: {},
  async created() {
    // const store = useProjectStore();
    // const currentProjectID = store.projectID;
    const response = await fetch("http://localhost:8000/comments/project/1");
    console.log("**************************************************");
    console.log(response);
    if (response.ok) {
      const data = await response.json();
      this.comments = data;
      console.log(data);
    }
  },
  mounted() {},
  watch: {},
  components: {},
  props: {},
  emits: {},
};
</script> -->
<script>
import { ref, watchEffect, inject } from "vue";

export default {
  setup() {
    const comments = ref([]);
    const projectStore = inject("projectStore");
    const projectID = ref(null);
    watchEffect(() => {
      projectID.value = projectStore.projectID;
      fetchComments(projectID.value);
    });

    async function fetchComments(id) {
      try {
        const response = await fetch(
          `http://localhost:8000/comments/project/${id}`
        );
        if (response.ok) {
          const data = await response.json();
          comments.value = data;
        }
      } catch (error) {
        console.error("Failed to fetch project data:", error);
      }
    }

    async function handleSubmit() {
      const comment = document.querySelector("#comment").value;
      const id = projectID.value;

      const response = await fetch("http://localhost:8000/comments/create/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user: 1,
          comment: comment,
          project: id,
        }),
      });
      if (response.ok) {
        const data = await response.json();
        console.log(data);
        window.location.reload();
      }
    }

    return { comments, handleSubmit, projectID };
  },
};
</script>

<style></style>
