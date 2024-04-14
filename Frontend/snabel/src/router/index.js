import { createRouter, createWebHistory } from "vue-router";
// import HomeView from '../views/HomeView.vue'
// import sliderComponent from '../components/sliderComponent.vue'
import lastProjectComponent from "../components/lastProjectComponent.vue";
// import projectDonationCards from "@/components/projectDonationCards.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: lastProjectComponent,
  },
  {
    path: "/about",
    name: "about",
    component: function () {
      return import(/* webpackChunkName: "about" */ "../views/AboutView.vue");
    },
  },
  {
    path: "/project",
    name: "projectView",
    component: lastProjectComponent,
  },
  {
    path: "/project/:id",
    name: "project",
    props: true,
    // component: projectDonationCards,
    component: function () {
      return import("../views/projectView.vue");
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
