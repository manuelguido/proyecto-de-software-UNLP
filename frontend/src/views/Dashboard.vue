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
          <div class="row justify-content-center">
            <div class="col-12 col-lg-11">
              <h1 class="h3 w600 color-b mb-2">
                <slot name="page_title">
                  Inicio
                  {{page_title}}
                </slot>
              </h1>
              <hr class="mb-5 white-d">
              <slot name="dashboard_content">
                <div v-if=user_has_role>
                  <dashboard-items :items="routes"></dashboard-items>
                </div>
                <div v-else>
                  <no-role-message></no-role-message>
                </div>
              </slot>
            </div>
          </div>
        </div>
      </div>
      <!-- /.Panel content -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import sidebar from '@/components/dashboard/sidebar/Sidebar'
import navbar from '@/components/dashboard/Navbar'
import dashboardItems from '@/components/dashboard/items/DashboardItems'
import noRoleMessage from '@/components/dashboard/NoRoleMessage'

export default {
  name: 'Dashboard',
  components: {
    'sidebar': sidebar,
    'navbar': navbar,
    'dashboard-items': dashboardItems,
    'no-role-message': noRoleMessage
  },
  data () {
    return {
      routes: null,
      user_has_role: false
    }
  },
  methods: {
    // Obtener las rutas del usuario
    getUserRoutes: function () {
      const path = '/api/user/routes'
      axios.get(path).then((res) => {
        this.routes = res.data
        localStorage.setItem('routes', JSON.stringify(this.routes))
      }).catch((error) => {
        console.log(error)
      })
    },
    // Obtener si el usuario tiene al menos un rol
    userHasRole: function () {
      const path = '/api/user/has_role'
      axios.get(path).then((res) => {
        this.user_has_role = res.data.role_status // Boolean
      }).catch((error) => {
        console.log(error)
      })
    }
  },
  mounted () {
    this.userHasRole()
    // Obtener rutas del usuario
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
    padding-left: 260px !important;
  }
}
</style>
