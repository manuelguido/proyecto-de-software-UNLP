<template>
  <div class="container-fluid">
    <div class="row justify-content-center">
      <!-- Sidebar -->
      <sidebar :links="routes"></sidebar>
      <!-- /.Sidebar -->
      <!-- Panel content -->
      <div id="dashboard-container" class="col">
        <navbar :links="routes"></navbar>
        <!-- All content -->
        <div id="dashboard-content" class="container-fluid mt-5 py-5 px-lg-5 px-3 w-100">
          <div class="row">
            <div class="col-12">
              <h1 class="h4 w600 black-c m-0">
                <slot name="page_title">
                  Inicio
                  {{page_title}}
                </slot>
              </h1>
              <hr class="mt-1 mb-5">
            </div>
          </div>
          <slot name="dashboard_content">
            <dashboard-items :items="routes"></dashboard-items>
          </slot>
        </div>
      </div>
      <!-- /.Panel content -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import sidebar from '@/components/dashboard/menu/Sidebar'
import navbar from '@/components/dashboard/Navbar'
import dashboardItems from '@/components/dashboard/items/DashboardItems'

export default {
  name: 'Dashboard',
  components: {
    'sidebar': sidebar,
    'navbar': navbar,
    'dashboard-items': dashboardItems
  },
  data () {
    return {
      routes: ''
    }
  },
  methods: {
    getUserRoutes: function () {
      const path = '/api/user/routes'
      axios.get(path).then((res) => {
        this.routes = res.data
        localStorage.setItem('routes', JSON.stringify(this.routes))
      }).catch((error) => {
        console.log(error)
      })
    }
  },
  mounted () {
    if (localStorage.routes) {
      var routes = localStorage.getItem('routes')
      this.routes = JSON.parse(routes)
    } else {
      this.getUserRoutes()
    }
  }
}
</script>

<style scoped>
/* Dashboard container */
@media(min-width: 992px) {
  #dashboard-container {
    padding-left: 240px !important;
  }
}
</style>
