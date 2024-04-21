import { createRouter, createWebHistory } from "vue-router";
// import sliderComponent from '../components/sliderComponent.vue'
// import lastProjectComponent from '../components/lastProjectComponent.vue'
// import RegisterComponent from "@/components/Auth/RegisterComponent.vue";
// import LoginComponent from "@/components/Auth/LoginComponent.vue";
import ForgetPasswordComponent from "@/components/Auth/ForgetPasswordComponent2.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("../views/HomeView.vue"),
  },
  {
    path: "/search",
    name: "Search",
    component: () => import("../views/searchView.vue"),
  },
  {
    path: "/about",
    name: "About",
    component: () => import("../views/AboutView.vue"),
  },
  {
    path: "/register",
    name: "Register",
    // component: RegisterComponent,
    component: () => import("@/components/Auth/AuthinticationComponent.vue"),
    
  },
  {
    path: "/login",
    name: "Login",
    // component: LoginComponent,
    component: () => import("@/components/Auth/AuthinticationComponent.vue"),
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
    path: "/error",
    name: "error",
    component: () => import("../components/errors/errorComponent.vue"),
  },
  {
    path: "/:cathcAll(.*)",
    component: () => import("../views/AboutView.vue"),
  },
  {
    path:"/contactus",
    name:"contactus",
    component:()=> import("../components/contactUsComponents.vue")
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
