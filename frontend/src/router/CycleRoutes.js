import axios from 'axios'

import Cycles from '@/views/dashboard/cycles/Cycles'


const routes = [
  {
    path: '/cycles',
    name: 'Cycles',
    component: Cycles,
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
