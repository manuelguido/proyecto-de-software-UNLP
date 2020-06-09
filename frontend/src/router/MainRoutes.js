import axios from 'axios'

import Home from '@/views/Home'
import Login from '@/views/Login'
import Logout from '@/views/Logout'
import Dashboard from '@/views/Dashboard'

const routes = [
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
          localStorage.clear() // Deletes all local storage
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
  }
]

export default routes
