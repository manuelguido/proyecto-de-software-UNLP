import axios from 'axios'

import Instruments from '@/views/dashboard/instruments/Instruments'
import Instrument from '@/views/dashboard/instruments/Instrument'
import InstrumentNew from '@/views/dashboard/instruments/InstrumentNew'
import InstrumentEdit from '@/views/dashboard/instruments/InstrumentEdit'

const routes = [
  {
    path: '/instruments',
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
    path: '/instrument/:instrument_id',
    name: 'Instrument',
    component: Instrument,
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
    path: '/new/instrument',
    name: 'InstrumentNew',
    component: InstrumentNew,
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
    path: '/instrument/edit/:instrument_id',
    name: 'InstrumentEdit',
    component: InstrumentEdit,
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
