import '@fortawesome/fontawesome-free/css/all.min.css'
import 'bootstrap-css-only/css/bootstrap.min.css'
import 'mdbvue/lib/css/mdb.min.css'

import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ComponentA from './components/Card.vue'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  components: {
    'component-a': ComponentA,
  },
  render: h => h(App)
}).$mount('#app')
