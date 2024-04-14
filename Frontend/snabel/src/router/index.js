import { createRouter, createWebHistory } from 'vue-router'
// import sliderComponent from '../components/sliderComponent.vue'
import lastProjectComponent from "../components/lastProjectComponent.vue";
// import projectDonationCards from "@/components/projectDonationCards.vue";

const routes = [
  {
    path: '/',
    component: () => import('../views/HomeView.vue'),
  },
  {
    path: '/search',
    component: () => import('../components/searchComponent.vue'),
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
  {
    path: '/:catchAll(.*)',
    component: () => import('../views/AboutView.vue'),
  
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
