import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
// import sliderComponent from '../components/sliderComponent.vue'
// import lastProjectComponent from '../components/lastProjectComponent.vue'
import RegisterComponent from "../components/Auth/RegisterComponent.vue";
import LoginComponent from "@/components/Auth/LoginComponent.vue";
import ForgetPasswordComponent from "@/components/Auth/ForgetPasswordComponent.vue";

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/search',
        name: 'search',
        component: ()=>import('../components/searchComponent.vue')
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
        component: RegisterComponent,
    },
    {
        path: '/login',
        name: 'Login',
<<<<<<< HEAD
        component: LoginComponent,
    },
    {
        path: '/:cathcAll(.*)',
        component: ()=> import('../views/AboutView.vue'),
=======
        component: LoginComponent
    },
    {
        path: '/forget-password',
        name: 'ForgetPassword',
        component: ForgetPasswordComponent
>>>>>>> b73d5deeb54e0e2ed0b7b7408f1458ab5982efd1
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
