import { createRouter, createWebHistory } from "vue-router";
// import RegisterComponent from "../components/Auth/RegisterComponent.vue";
// import LoginComponent from "@/components/Auth/LoginComponent.vue";
import authComponent from "@/components/Auth/AuthinticationComponent.vue";
import ForgetPasswordComponent from "@/components/Auth/ForgetPasswordComponent.vue";
import ResetPasswordComponent from "@/components/Auth/ResetPasswordComponent.vue";
import ProfileComponent from "@/components/Auth/ProfileComponent.vue";

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
    // component: RegisterComponent,
    component: authComponent,
    beforeEnter: (to, from, next) => {
      if (!sessionStorage.getItem("user")) {
        next();
      } else {
        next({ name: "home" });
      }
    },
  },
  {
    path: "/login",
    name: "login",
    // component: LoginComponent,
    component: authComponent,
    beforeEnter: (to, from, next) => {
      if (!sessionStorage.getItem("user")) {
        next();
      } else {
        next({ name: "home" });
      }
    },
  },
  {
    path: "/forget-password",
    name: "forgetPassword",
    component: ForgetPasswordComponent,
    beforeEnter: (to, from, next) => {
      if (!sessionStorage.getItem("user")) {
        next();
      } else {
        next({ name: "home" });
      }
    },
  },
  {
    path: "/reset_password",
    name: "ResetPassword",
    component: ResetPasswordComponent,
  },
  {
    path: "/profile",
    name: "profile",
    component: ProfileComponent,
    beforeEnter: (to, from, next) => {
      if (sessionStorage.getItem("user")) {
        next();
      } else {
        next({ name: "home" });
      }
    },
    meta: { requiresAuth: true }, // Authentication requires
  },
  {
    path: "/payment",
    name: "payment",
    component: () => import("../views/projectPayment.vue"),
    beforeEnter: (to, from, next) => {
      if (!sessionStorage.getItem("user")) {
        next();
      } else {
        next({ name: "home" });
      }
    },
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
    beforeEnter: (to, from, next) => {
      if (sessionStorage.getItem('user')) {
        next();
      } else {
        next({ name: 'login' });
      }
    }
  },
  {
    path: "/profile",
    name: "profile",
    component: () => import("@/components/Auth/ProfileComponent.vue"),
    beforeEnter: (to, from, next) => {
      if (sessionStorage.getItem("user")) {
        next();
      } else {
        next({ name: "login" });
      }
    },
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
