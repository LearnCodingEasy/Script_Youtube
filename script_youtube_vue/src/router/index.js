import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

// Authentication
import LoginView from '../views/Authentication/Login.vue'

// Script
import ScriptCreate from '../views/Script/Script_Create.vue'
import ScriptList from '../views/Script/Scripts_List.vue'

// Account
import ProfileView from '../views/Account/Profile.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    // Authentication [ Login ]
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    // Account [ Profile ]
    {
      path: '/profile/:id',
      name: 'profile',
      component: ProfileView,
      meta: {
        requireLogin: true
      }
    },
    // Script []
    {
      path: '/ScriptCreate',
      name: 'Script_Create',
      component: ScriptCreate,
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/ScriptList',
      name: 'ScriptList',
      component: ScriptList,
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
