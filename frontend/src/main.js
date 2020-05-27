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

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
