import Vue from 'vue'
import axios from 'axios'
import Router from 'vue-router'
// Home Page
import Home from '@/views/Home'
// Auth
import Login from '@/views/Login'
import Logout from '@/views/Logout'
// Dashboard
import Dashboard from '@/views/Dashboard'
// Cores
import Cores from '@/views/dashboard/cores/Cores'
// Students
import Students from '@/views/dashboard/students/Students'
import Student from '@/views/dashboard/students/Student'
import StudentNew from '@/views/dashboard/students/StudentNew'
import StudentEdit from '@/views/dashboard/students/StudentEdit'
// Teachers
import Teachers from '@/views/dashboard/teachers/Teachers'
import Teacher from '@/views/dashboard/teachers/Teacher'
import TeacherNew from '@/views/dashboard/teachers/TeacherNew'
import TeacherEdit from '@/views/dashboard/teachers/TeacherEdit'
// Instruments
import Instruments from '@/views/dashboard/instruments/Instruments'
import Instrument from '@/views/dashboard/instruments/Instrument'
import InstrumentNew from '@/views/dashboard/instruments/InstrumentNew'
import InstrumentEdit from '@/views/dashboard/instruments/InstrumentEdit'
// Users
import Users from '@/views/dashboard/users/Users'
import User from '@/views/dashboard/users/User'
import UserNew from '@/views/dashboard/users/UserNew'
import UserEdit from '@/views/dashboard/users/UserEdit'
// Configuration
import Configuration from '@/views/dashboard/Configuration'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      beforeEnter (to, from, next) {
        const path = '/auth/authenticated'
        axios.get(path).then((respuesta) => {
          if (!respuesta.data.authenticated) {
            next()
          } else {
            next({ name: 'Dashboard' })
          }
        }).catch((error) => {
          console.log(error)
        })
      }
    },
    {
      path: '/logout',
      name: 'Logout',
      component: Logout,
      beforeEnter (to, from, next) {
        const path = '/auth/unauthenticate'
        axios.get(path).then((respuesta) => {
          if (respuesta.data.success) {
            localStorage.clear() // Deletes all local storage
            next()
          } else {
            next({ name: 'Dashboard' })
          }
        }).catch((error) => {
          console.log(error)
        })
      }
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard,
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
      path: '/dashboard/cores',
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
    },
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
    {
      path: '/dashboard/teachers',
      name: 'Teachers',
      component: Teachers,
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
      path: '/dashboard/teacher/:teacher_id',
      name: 'Teacher',
      component: Teacher,
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
      path: '/dashboard/teacher/new',
      name: 'TeacherNew',
      component: TeacherNew,
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
      path: '/dashboard/teacher/edit/:teacher_id',
      name: 'TeacherEdit',
      component: TeacherEdit,
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
      path: '/dashboard/instruments',
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
      path: '/dashboard/instrument/:student_id',
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
      path: '/dashboard/instrument/new',
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
      path: '/dashboard/instrument/edit/:instrument_id',
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
    },
    {
      path: '/dashboard/users',
      name: 'Users',
      component: Users,
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
      path: '/dashboard/user/:user_id',
      name: 'User',
      component: User,
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
      path: '/dashboard/user/new',
      name: 'UserNew',
      component: UserNew,
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
      path: '/dashboard/user/edit/:user_id',
      name: 'UserEdit',
      component: UserEdit,
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
      path: '/dashboard/configuration',
      name: 'Configuration',
      component: Configuration,
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
})
