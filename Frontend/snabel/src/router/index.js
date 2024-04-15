import { createRouter, createWebHistory } from "vue-router";
// import sliderComponent from '../components/sliderComponent.vue'
// import lastProjectComponent from '../components/lastProjectComponent.vue'
import RegisterComponent from "../components/Auth/RegisterComponent.vue";
import LoginComponent from "@/components/Auth/LoginComponent.vue";
import ForgetPasswordComponent from "@/components/Auth/ForgetPasswordComponent.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component:  () => import("../views/HomeView.vue"),
  },
  {
    path: "/search",
    name: "search",
    component: () => import("../components/searchComponent.vue"),
  },
  {
    path: "/about",
    name: "about",
    component:  () => import("../views/AboutView.vue")
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
    path: "/projectTest/:id",
    name: "ProjectTest",
    component: () => import("../views/projectView.vue"),
    props: true,
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
