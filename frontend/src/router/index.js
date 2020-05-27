import Vue from 'vue'
import axios from 'axios'
import Router from 'vue-router'
// Home Page
import Home from '@/views/Home'
// Auth
import Login from '@/views/Login'
import Logout from '@/views/Logout'
// Dashboard
import Dashboard from '@/views/Dashboard'
// Cores
import Cores from '@/views/dashboard/cores/Cores'
// Students
import Students from '@/views/dashboard/students/Students'
import Student from '@/views/dashboard/students/Student'
// Teachers
import Teachers from '@/views/dashboard/teachers/Teachers'
// Instruments
import Instruments from '@/views/dashboard/instruments/Instruments'
// Users
import Users from '@/views/dashboard/users/Users'
// Configuration
import Configuration from '@/views/dashboard/Configuration'

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
      path: '/dashboard/student/:student_id',
      name: 'Student',
      component: Student,
      props: true,
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
    },
    {
      path: '/dashboard/configuration',
      name: 'Configuration',
      component: Configuration,
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
