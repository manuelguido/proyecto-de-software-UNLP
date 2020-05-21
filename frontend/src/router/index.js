import Vue from 'vue'
import axios from 'axios'
import Router from 'vue-router'
import Home from '@/views/Home'
import Login from '@/views/Login'
import Logout from '@/views/Logout'
import Dashboard from '@/views/Dashboard'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      beforeEnter (to, from, next) {
        const path = '/user/authenticated'
        axios.get(path).then((respuesta) => {
          if (!respuesta.data.authenticated) {
            next()
          } else {
            next({ name: 'Dashboard' })
          }
        }).catch((error) => {
          console.log(error)
        })
      }
    },
    {
      path: '/logout',
      name: 'Logout',
      component: Logout,
      beforeEnter (to, from, next) {
        const path = '/user/unauthenticate'
        axios.get(path).then((respuesta) => {
          if (respuesta.data.success) {
            next()
          } else {
            next({ name: 'Dashboard' })
          }
        }).catch((error) => {
          console.log(error)
        })
      }
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard,
      beforeEnter (to, from, next) {
        const path = '/user/authenticated'
        axios.get(path).then((respuesta) => {
          if (respuesta.data.authenticated) {
            next()
          } else {
            next({ name: 'Login' })
          }
        }).catch((error) => {
          console.log(error)
        })
      }
    }
  ]
})
