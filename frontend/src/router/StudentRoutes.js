import axios from 'axios'
// Students
import Students from '@/views/dashboard/students/Students'
import Student from '@/views/dashboard/students/Student'
import StudentNew from '@/views/dashboard/students/StudentNew'
import StudentEdit from '@/views/dashboard/students/StudentEdit'

const routes = [
  {
    path: '/dashboard/students',
    name: 'Students',
    component: Students,
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
    path: '/dashboard/student/:student_id',
    name: 'Student',
    component: Student,
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
    path: '/dashboard/new/student',
    name: 'StudentNew',
    component: StudentNew,
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
    path: '/dashboard/student/edit/:student_id',
    name: 'StudentEdit',
    component: StudentEdit,
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
]

export default routes