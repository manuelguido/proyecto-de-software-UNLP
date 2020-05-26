import Vue from 'vue'
import axios from 'axios'
import Router from 'vue-router'
import Home from '@/views/Home'
import Login from '@/views/Login'
import Logout from '@/views/Logout'
import Dashboard from '@/views/Dashboard'
import Cores from '@/views/dashboard/Cores'
import Students from '@/views/dashboard/Students'
import Teachers from '@/views/dashboard/Teachers'
import Instruments from '@/views/dashboard/Instruments'
import Users from '@/views/dashboard/Users'

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
        const path = '/auth/authenticated'
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
        const path = '/auth/unauthenticate'
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
        const path = '/auth/authenticated'
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
    },
    {
      path: '/dashboard/cores',
      name: 'Cores',
      component: Cores,
      beforeEnter (to, from, next) {
        const path = '/auth/authenticated'
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
    },
    {
      path: '/dashboard/students',
      name: 'Students',
      component: Students,
      beforeEnter (to, from, next) {
        const path = '/auth/authenticated'
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
    },
    {
      path: '/dashboard/teachers',
      name: 'Teachers',
      component: Teachers,
      beforeEnter (to, from, next) {
        const path = '/auth/authenticated'
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
    },
    {
      path: '/dashboard/instruments',
      name: 'Instruments',
      component: Instruments,
      beforeEnter (to, from, next) {
        const path = '/auth/authenticated'
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
    },
    {
      path: '/dashboard/users',
      name: 'Users',
      component: Users,
      beforeEnter (to, from, next) {
        const path = '/auth/authenticated'
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
