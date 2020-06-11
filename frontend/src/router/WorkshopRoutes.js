import axios from 'axios'

import Workshops from '@/views/dashboard/workshops/Workshops'
import Workshop from '@/views/dashboard/workshops/Workshop'
import WorkshopNew from '@/views/dashboard/workshops/WorkshopNew'
import WorkshopEdit from '@/views/dashboard/workshops/WorkshopEdit'
import CycleWorkshops from '@/views/dashboard/workshops/CycleWorkshops'
import WorkshopUnassign from '@/views/dashboard/workshops/WorkshopUnassign'

const routes = [
  {
    path: '/workshops',
    name: 'Workshops',
    component: Workshops,
    beforeEnter (to, from, next) {
      const path = '/auth/authenticated'
      axios.get(path).then((res) => {
        if (res.data.authenticated) {
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
    path: '/workshop/:workshop_id',
    name: 'Workshop',
    component: Workshop,
    props: true,
    beforeEnter (to, from, next) {
      const path = '/auth/authenticated'
      axios.get(path).then((res) => {
        if (res.data.authenticated) {
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
    path: '/new/workshop',
    name: 'WorkshopNew',
    component: WorkshopNew,
    beforeEnter (to, from, next) {
      const path = '/auth/authenticated'
      axios.get(path).then((res) => {
        if (res.data.authenticated) {
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
    path: '/workshop/edit/:workshop_id',
    name: 'WorkshopEdit',
    component: WorkshopEdit,
    props: true,
    beforeEnter (to, from, next) {
      const path = '/auth/authenticated'
      axios.get(path).then((res) => {
        if (res.data.authenticated) {
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
    path: '/cycle_workshops',
    name: 'CycleWorkshops',
    component: CycleWorkshops,
    beforeEnter (to, from, next) {
      const path = '/auth/authenticated'
      axios.get(path).then((res) => {
        if (res.data.authenticated) {
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
    path: '/unassign/workshop/:cycle_workshop_id',
    name: 'WorkshopUnassign',
    component: WorkshopUnassign,
    props: true,
    beforeEnter (to, from, next) {
      const path = '/auth/authenticated'
      axios.get(path).then((res) => {
        if (res.data.authenticated) {
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
