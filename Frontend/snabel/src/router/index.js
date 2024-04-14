import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
// import sliderComponent from '../components/sliderComponent.vue'
// import lastProjectComponent from '../components/lastProjectComponent.vue'
import RegisterComponent from "../components/Auth/RegisterComponent.vue";
import LoginComponent from "@/components/Auth/LoginComponent.vue";

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: function () {
            return import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
        }
    },
    {
        path: '/register',
        name: 'Register',
        component: RegisterComponent
    },
    {
        path: '/login',
        name: 'Login',
        component: LoginComponent
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
