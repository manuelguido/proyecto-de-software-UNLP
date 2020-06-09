import axios from 'axios'

import Workshops from '@/views/dashboard/workshops/Workshops'

const routes = [
  {
    path: '/workshops',
    name: 'Workshops',
    component: Workshops,
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
