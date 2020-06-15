import '@fortawesome/fontawesome-free/css/all.min.css'
import 'bootstrap-css-only/css/bootstrap.min.css'
import 'mdbvue/lib/css/mdb.min.css'
// Leaflet
import { LMap, LTileLayer, LMarker } from 'vue2-leaflet'
import 'leaflet/dist/leaflet.css'
// Moment JS
import moment from 'moment'
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'

// Leaflet components
Vue.component('l-map', LMap)
Vue.component('l-tile-layer', LTileLayer)
Vue.component('l-marker', LMarker)

Vue.config.productionTip = false

// Date filters
Vue.filter('formatDate', function (value) {
  if (value) {
    moment.locale('es')
    return moment(String(value)).format('L')
  }
})
Vue.filter('formatDateFull', function (value) {
  if (value) {
    moment.locale('es')
    return moment(String(value)).format('LL')
  }
})
Vue.filter('formatDateForm', function (value) {
  if (value) {
    moment.locale('en')
    return moment().subtract(10, 'days').calendar() // 05/23/2020
  }
})

var permissions
var loaded = false

Vue.mixin({
  mounted: function () {
    if (!loaded) {
      if (localStorage.permissions) {
        var perm = localStorage.getItem('permissions')
        permissions = JSON.parse(perm)
      } else {
        const path = '/api/user/permissions'
        axios.get(path).then((res) => {
          localStorage.setItem('permissions', JSON.stringify(res.data))
        }).catch((error) => {
          console.log(error + ' => error loading permissions. Retrying.')
          axios.get(path).then((res) => {
            localStorage.setItem('permissions', JSON.stringify(res.data))
          })
        })
      }
      console.log(permissions)
      loaded = true
    }
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
