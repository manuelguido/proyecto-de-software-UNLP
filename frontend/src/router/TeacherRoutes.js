import axios from 'axios'

import Teachers from '@/views/dashboard/teachers/Teachers'
import Teacher from '@/views/dashboard/teachers/Teacher'
import TeacherNew from '@/views/dashboard/teachers/TeacherNew'
import TeacherEdit from '@/views/dashboard/teachers/TeacherEdit'

const routes = [
  {
    path: '/teachers',
    name: 'Teachers',
    component: Teachers,
    beforeEnter (to, from, next) {
      const path = '/auth/authenticated/docente_index'
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
    path: '/teacher/:teacher_id',
    name: 'Teacher',
    component: Teacher,
    props: true,
    beforeEnter (to, from, next) {
      const path = '/auth/authenticated/docente_show'
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
    path: '/new/teacher',
    name: 'TeacherNew',
    component: TeacherNew,
    beforeEnter (to, from, next) {
      const path = '/auth/authenticated/docente_mew'
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
    path: '/teacher/edit/:teacher_id',
    name: 'TeacherEdit',
    component: TeacherEdit,
    props: true,
    beforeEnter (to, from, next) {
      const path = '/auth/authenticated/docente_update'
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
