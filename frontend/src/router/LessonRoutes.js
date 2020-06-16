import axios from 'axios'

import Lessons from '@/views/dashboard/lessons/Lessons'
import Lesson from '@/views/dashboard/lessons/Lesson'
import LessonNew from '@/views/dashboard/lessons/LessonNew'
import LessonEdit from '@/views/dashboard/lessons/LessonEdit'
import LessonStudents from '@/views/dashboard/lessons/LessonStudents'

const routes = [
  {
    path: '/lessons',
    name: 'Lessons',
    component: Lessons,
    beforeEnter (to, from, next) {
      const path = '/auth/authenticated/administrativo_index'
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
    path: '/lesson/:lesson_id',
    name: 'Lesson',
    component: Lesson,
    props: true,
    beforeEnter (to, from, next) {
      const path = '/auth/authenticated/administrativo_show'
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
    path: '/new/lesson',
    name: 'LessonNew',
    component: LessonNew,
    beforeEnter (to, from, next) {
      const path = '/auth/authenticated/administrativo_new'
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
    path: '/lesson/edit/:lesson_id',
    name: 'LessonEdit',
    component: LessonEdit,
    props: true,
    beforeEnter (to, from, next) {
      const path = '/auth/authenticated/administrativo_update'
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
    path: '/lesson/students/:lesson_id',
    name: 'LessonStudents',
    component: LessonStudents,
    props: true,
    beforeEnter (to, from, next) {
      const path = '/auth/authenticated/administrativo_new'
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
