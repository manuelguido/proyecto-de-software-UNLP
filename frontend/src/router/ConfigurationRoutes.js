import axios from 'axios'

import Configuration from '@/views/dashboard/Configuration'

const routes = [
  {
    path: '/configuration',
    name: 'Configuration',
    component: Configuration,
    beforeEnter (to, from, next) {
      const path = '/auth/authenticated/configuration_all'
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
