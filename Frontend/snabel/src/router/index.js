import { createRouter, createWebHistory } from "vue-router";
// import sliderComponent from '../components/sliderComponent.vue'
// import lastProjectComponent from '../components/lastProjectComponent.vue'
import RegisterComponent from "../components/Auth/RegisterComponent2.vue";
import LoginComponent from "@/components/Auth/LoginComponent2.vue";
import ForgetPasswordComponent from "@/components/Auth/ForgetPasswordComponent2.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("../views/HomeView.vue"),
  },
  {
    path: "/search",
    name: "search",
    component: () => import("../components/searchComponent.vue"),
  },
  {
    path: "/about",
    name: "about",
    component: () => import("../views/AboutView.vue"),
  },
  {
    path: "/register",
    name: "Register",
    component: RegisterComponent,
  },
  {
    path: "/login",
    name: "Login",
    component: LoginComponent,
  },
  {
    path: "/forget-password",
    name: "ForgetPassword",
    component: ForgetPasswordComponent,
  },
  {
    path: "/payment",
    name: "payment",
    component: () => import("../views/projectPayment.vue"),
  },
  {
    path: "/projects/:id",
    name: "ProjectTest",
    component: () => import("../views/projectView.vue"),
    props: true,
  },
  {
    path: "/addProject",
    name: "AddProject",
    component: () => import("../components/addProjectComponent.vue"),
  },
  {
    path: "/:cathcAll(.*)",
    component: () => import("../views/AboutView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
