import { createRouter, createWebHistory } from 'vue-router'
import Login from "@/components/Login.vue"
import Room from "@/components/chat/Room.vue"
const routes = [{
        path: '/',
        name: 'home',
        component: Login
    },
    {
        path: '/room/',
        name: 'room',
        component: Room
    },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    // }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router