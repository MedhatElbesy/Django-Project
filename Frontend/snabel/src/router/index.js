import { createRouter, createWebHistory } from 'vue-router'
// import sliderComponent from '../components/sliderComponent.vue'

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
    path: '/:catchAll(.*)',
    component: () => import('../views/AboutView.vue'),

  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router