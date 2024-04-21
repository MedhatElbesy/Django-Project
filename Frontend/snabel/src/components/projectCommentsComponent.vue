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
        <button
          data-bs-toggle="modal"
          data-bs-target="#reportModal"
          data-bs-objectType="comment"
          :data-bs-id="comment.user"
          class="text-danger btn report-flag float-end"
        >
          <i class="fa-solid fa-flag report-flag"></i>
        </button>
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
    <br />
    <br />
    <!-- project rating of 5 stars -->
    <h5 class="h5">Rate this project from 1 to 5 stars!</h5>
    <form action="" class="form w-50 mx-auto d-flex justify-content-between">
      <input
        class="form-control visually-hidden"
        type="radio"
        name="rating"
        id="rating1"
        value="1"
      />
      <label class="star" for="1"><i class="far fa-star"></i></label>
      <input
        class="form-control visually-hidden"
        type="radio"
        name="rating"
        id="2"
        value="2"
      />
      <label class="star" for="2"><i class="far fa-star"></i></label>
      <input
        class="form-control visually-hidden"
        type="radio"
        name="rating"
        id="3"
        value="3"
      />
      <label class="star" for="3"><i class="far fa-star"></i></label>
      <input
        class="form-control visually-hidden"
        type="radio"
        name="rating"
        id="4"
        value="4"
      />
      <label class="star" for="4"><i class="far fa-star"></i></label>
      <input
        class="form-control visually-hidden"
        type="radio"
        name="rating"
        id="5"
        value="5"
      />
      <label class="star" for="5"><i class="far fa-star"></i></label>
      <br />
    </form>
    <button class="my-2 btn btn-success text-light" @click="submitRating">
      Rate this project!
    </button>
  </section>
</template>

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

    async function submitRating() {
      const rating = document.querySelector(
        "input[name='rating']:checked"
      ).value;
      alert("rating" + rating);
      const id = projectID.value;

      const response = await fetch("http://localhost:8000/ratings/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user: 1,
          rating: rating,
          project: id,
        }),
      });
      if (response.ok) {
        const data = await response.json();
        console.log(data);
        window.location.reload();
      }
    }

    async function reportComment() {
      fetch(`http://localhost:8000/reports/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          object_id: this.comment.id,
          content_object: "comment",
        }),
      });
    }

    return { comments, handleSubmit, submitRating, reportComment, projectID };
  },
  mounted() {
    const stars = document.querySelectorAll(".star");

    stars.forEach((star) => {
      star.addEventListener("click", function () {
        stars.forEach((star) => {
          star.classList.remove("clicked");
          star.previousSibling.checked = false;
        });
        const rating = parseInt(star.previousSibling.value);
        for (let index = 0; index < rating; index++) {
          stars[index].classList.add("clicked");
        }
        // Mark input as checked for the clicked star
        star.previousElementSibling.checked = true;
        console.log(star.previousElementSibling);
      });
    });
  },
};
</script>
<style>
.visually-hidden {
  position: absolute;
  clip: rect(1px, 1px, 1px, 1px);
  padding: 0;
  border: 0;
  height: 1px;
  width: 1px;
  overflow: hidden;
}
.star {
  font-size: 24px;
  cursor: pointer;
  color: #ccc;
  transition: color 0.3s;
}
.report-flag il {
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  font-size: large;
}
.report-flag:hover {
  color: #ea5252;
}

.clicked {
  color: yellow; /* Color of clicked stars and preceding stars */
}
</style>
