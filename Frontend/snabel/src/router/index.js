import { createRouter, createWebHistory } from "vue-router";
import RegisterComponent from "../components/Auth/RegisterComponent.vue";
import LoginComponent from "@/components/Auth/LoginComponent.vue";
import ForgetPasswordComponent from "@/components/Auth/ForgetPasswordComponent.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("../views/HomeView.vue"),
  },
  {
    path: "/search",
    name: "search",
    component: () => import("../views/searchView.vue"),
  },
  {
    path: "/about",
    name: "about",
    component: () => import("../views/AboutView.vue"),
  },
  {
    path: "/register",
    name: "register",
    component: RegisterComponent,
    beforeEnter: (to, from, next) => {
      if (!sessionStorage.getItem('user')) {
        next();
      } else {
        next({ name: 'home' });
      }
    }
  },
  {
    path: "/login",
    name: "login",
    component: LoginComponent,
    beforeEnter: (to, from, next) => {
      if (!sessionStorage.getItem('user')) {
        next();
      } else {
        next({ name: 'home' });
      }
    }
  },
  {
    path: "/forget-password",
    name: "forgetPassword",
    component: ForgetPasswordComponent,
    beforeEnter: (to, from, next) => {
      if (!sessionStorage.getItem('user')) {
        next();
      } else {
        next({ name: 'home' });
      }
    }
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
    path: "/profile",
    name: "profile",
    component: () => import("@/components/Auth/ProfileComponent.vue"),
    beforeEnter: (to, from, next) => {
      if (sessionStorage.getItem('user')) {
        next();
      } else {
        next({ name: 'login' });
      }
    }
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
