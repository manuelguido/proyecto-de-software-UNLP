import axios from 'axios'

import Users from '@/views/dashboard/users/Users'
import User from '@/views/dashboard/users/User'
import UserNew from '@/views/dashboard/users/UserNew'
import UserEdit from '@/views/dashboard/users/UserEdit'

const routes = [
  {
    path: '/users',
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
    path: '/user/:user_id',
    name: 'User',
    component: User,
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
    path: '/new/user',
    name: 'UserNew',
    component: UserNew,
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
    path: '/user/edit/:user_id',
    name: 'UserEdit',
    component: UserEdit,
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
  }
]

export default routes
