import Vue from 'vue'
import axios from 'axios'
import Router from 'vue-router'

import FullRoutes from '@/router/StudentRoutes'
import StudentRoutes from '@/router/FullRoutes'

Vue.use(Router)

var allRoutes = []
allRoutes = allRoutes.concat(
  FullRoutes,
  StudentRoutes
)

const routes = allRoutes

export default new Router({
  mode: 'history',
  routes
})
