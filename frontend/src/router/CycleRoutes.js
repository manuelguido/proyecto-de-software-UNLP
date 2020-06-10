import axios from 'axios'

import Cycles from '@/views/dashboard/cycles/Cycles'
import Cycle from '@/views/dashboard/cycles/Cycle'
import CycleNew from '@/views/dashboard/cycles/CycleNew'
import CycleEdit from '@/views/dashboard/cycles/CycleEdit'

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
  },
  {
    path: '/cycle/:cycle_id',
    name: 'Cycle',
    component: Cycle,
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
    path: '/new/cycle',
    name: 'CycleNew',
    component: CycleNew,
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
    path: '/cycle/edit/:cycle_id',
    name: 'CycleEdit',
    component: CycleEdit,
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
