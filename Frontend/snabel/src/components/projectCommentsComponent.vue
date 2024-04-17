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
  </section>
</template>

<script>
// import { useProjectStore } from "@/stores/project";
export default {
  data() {
    return {
      comments: [],
    };
  },
  methods: {},
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
</script>

<style></style>
