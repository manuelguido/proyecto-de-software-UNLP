import axios from 'axios'

import Cores from '@/views/dashboard/cores/Cores'

const routes = [
  {
    path: '/cores',
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
  }
]

export default routes
