import Vue from 'vue'
import Router from 'vue-router'

import MainRoutes from '@/router/MainRoutes'
import AssistanceRoutes from '@/router/AssistanceRoutes'
import CoreRoutes from '@/router/CoreRoutes'
import StudentRoutes from '@/router/StudentRoutes'
import TeacherRoutes from '@/router/TeacherRoutes'
import InstrumentRoutes from '@/router/InstrumentRoutes'
import CycleRoutes from '@/router/CycleRoutes'
import WorkshopRoutes from '@/router/WorkshopRoutes'
import LessonRoutes from '@/router/LessonRoutes'
import UserRoutes from '@/router/UserRoutes'
import ConfigurationRoutes from '@/router/ConfigurationRoutes'

Vue.use(Router)

var allRoutes = []
allRoutes = allRoutes.concat(
  MainRoutes,
  AssistanceRoutes,
  CoreRoutes,
  StudentRoutes,
  TeacherRoutes,
  InstrumentRoutes,
  CycleRoutes,
  WorkshopRoutes,
  LessonRoutes,
  UserRoutes,
  ConfigurationRoutes
)

const routes = allRoutes

export default new Router({
  mode: 'history',
  routes
})
