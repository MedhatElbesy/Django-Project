<template>
  <!-- <h1>hi</h1> -->
  <section class="comments-container">
    <div
      class="comment row align-baseline"
      v-for="comment in comments"
      :key="comment.id"
    >
      <div class="col-2">
        <img
          src="https://images.unsplash.com/photo-1500648735779-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60"
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
