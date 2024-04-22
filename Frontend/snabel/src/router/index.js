import { createRouter, createWebHistory } from "vue-router";
// import sliderComponent from '../components/sliderComponent.vue'
// import lastProjectComponent from '../components/lastProjectComponent.vue'
import RegisterComponent from "../components/Auth/RegisterComponent.vue";
import LoginComponent from "@/components/Auth/LoginComponent.vue";
import ForgetPasswordComponent from "@/components/Auth/ForgetPasswordComponent.vue";
import ProfileComponent from "@/components/Auth/ProfileComponent.vue";
import ResetPasswordComponent from "@/components/Auth/ResetPasswordComponent.vue";
import AboutView from "@/views/AboutView.vue";
// import {useAuthenticationStore} from "@/stores/auth";

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
    component: AboutView,
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
    path: "/forget_password",
    name: "ForgetPassword",
    component: ForgetPasswordComponent,
  },
  {
    path: "/reset_password",
    name: "ResetPassword",
    component: ResetPasswordComponent,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileComponent,
    meta: { requiresAuth: true } // Authentication requires
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
    component: () => import("../views/NotFound.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
