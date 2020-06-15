import axios from 'axios'

import Assistances from '@/views/dashboard/assistances/Assistances'
import AssistanceNew from '@/views/dashboard/assistances/AssistanceNew'

const routes = [
  {
    path: '/assistances',
    name: 'Assistances',
    component: Assistances,
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
    path: '/new/assistance/:lesson_id',
    name: 'AssistanceNew',
    component: AssistanceNew,
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
  // {
  //   path: '/new/lesson',
  //   name: 'LessonNew',
  //   component: LessonNew,
  //   beforeEnter (to, from, next) {
  //     const path = '/auth/authenticated'
  //     axios.get(path).then((respuesta) => {
  //       if (respuesta.data.authenticated) {
  //         next()
  //       } else {
  //         next({ name: 'Login' })
  //       }
  //     }).catch((error) => {
  //       console.log(error)
  //     })
  //   }
  // },
  // {
  //   path: '/lesson/edit/:lesson_id',
  //   name: 'LessonEdit',
  //   component: LessonEdit,
  //   props: true,
  //   beforeEnter (to, from, next) {
  //     const path = '/auth/authenticated'
  //     axios.get(path).then((respuesta) => {
  //       if (respuesta.data.authenticated) {
  //         next()
  //       } else {
  //         next({ name: 'Login' })
  //       }
  //     }).catch((error) => {
  //       console.log(error)
  //     })
  //   }
]

export default routes
