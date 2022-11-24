import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProfileView from '../views/ProfileView.vue'
import LogInView from '../views/LogInView.vue'
import SignUpView from '../views/SignUpView.vue'
import SearchView from '../views/SearchView.vue'
import WatchLaterView from '../views/WatchLaterView.vue'
import MovieItemDetailView from '../views/MovieItemDetailView.vue'
import store from '@/store/index.js'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/Search/:keyWord',
    name: 'search',
    component: SearchView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'login',
    component: LogInView
  },
  {
    path: '/watchlater',
    name: 'watchlater',
    component: WatchLaterView,
    beforeEnter(to, from, next) {
      store.dispatch('getWishList')
      next()
    }
  },
  {
    path: '/movieitemdetail/:movieId',
    name: 'movieitemdetail',
    component: MovieItemDetailView
  },
  
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
