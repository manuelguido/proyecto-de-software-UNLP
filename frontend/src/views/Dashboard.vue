<template>
  <div class="container-fluid">
    <navbar :links="routes"></navbar>
    <div class="row justify-content-center">
      <!-- Sidebar -->
      <sidebar :links="routes"></sidebar>
      <!-- /.Sidebar -->
      <!-- Panel content -->
      <div id="dashboard-container" class="col">
        <!-- All content -->
        <div id="dashboard-content" class="container-fluid mt-5 py-5 px-1 px-lg-5 w-100">
          <div class="row justify-content-center">
            <div class="col-12 col-lg-12">
              <div class="p-lg-4">
                <div class="p-lg-4">

                  <!-- Titulo -->
                  <h1 class="h3 w600 color-a mb-2">
                    <slot name="page_title">
                      Inicio
                      {{page_title}}
                    </slot>
                  </h1>
                  <hr class="mb-5 white-d">
                  <!-- /.Titulo -->

                  <!-- Contenido -->
                  <slot name="dashboard_content">
                    <!-- Loading Spinner -->
                    <div v-if="loading" class="d-flex justify-content-center mb-4">
                      <div class="spinner-border color-c" role="status">
                        <span class="sr-only">Loading...</span>
                      </div>
                    </div>
                    <!-- /.Loading Spinner -->
                    <div v-else-if=user_has_role>
                      <div class="row">
                        <div class="col-12">
                          <h1 class="h5 black-b w600 mb-4">Bienvenido nuevamente {{user.name}}</h1>
                          <h2 class="h6 black-c w600 mb-5">Aquí tienes algunos accesos directos</h2>
                        </div>
                      </div>
                      <dashboard-items :items="routes"></dashboard-items>
                    </div>
                    <div v-else>
                      <no-role-message></no-role-message>
                    </div>
                  </slot>
                  <!-- /.Contenido -->
                </div>
              </div>
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
import dashboardTitle from '@/components/dashboard/Title'

export default {
  name: 'Dashboard',
  components: {
    'sidebar': sidebar,
    'navbar': navbar,
    'dashboard-items': dashboardItems,
    'dashboard-title': dashboardTitle,
    'no-role-message': noRoleMessage
  },
  data () {
    return {
      user: {},
      routes: null,
      loading: true,
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
        this.loading = false
      }).catch((error) => {
        this.getUserRoutes()
        console.log(error + 'Retring')
      })
    },
    getUserData: function () {
      const path = '/api/user/profile'
      axios.get(path).then((res) => {
        this.user = res.data
        localStorage.setItem('user', JSON.stringify(this.user))
        this.loading = false
      }).catch((error) => {
        this.getUserData()
        console.log(error + 'Retring')
      })
    },
    userHasRole: function () {
      const path = '/api/user/has_role'
      axios.get(path).then((res) => {
        this.user_has_role = res.data.status // Boolean
        localStorage.setItem('role', JSON.stringify(res.data))
        this.loading = false
      }).catch((error) => {
        this.userHasRole()
        console.log(error)
      })
    }
  },
  mounted () {
    if (localStorage.role) {
      var loc = localStorage.getItem('role')
      var result = JSON.parse(loc)
      this.user_has_role = result.status
      this.loading = false
    } else {
      this.userHasRole()
    }
    // Obtener rutas del usuario
    if (localStorage.routes) {
      var routes = localStorage.getItem('routes')
      this.routes = JSON.parse(routes)
    } else {
      this.getUserRoutes()
    }
    if (localStorage.user) {
      this.user = JSON.parse(localStorage.getItem('user'))
    } else {
      this.getUserData()
    }
  }
}
</script>

<style>
#dashboard-container {
  min-height: 100vh;
  background: #fff;
}
@media(min-width: 1500px) {
  #dashboard-container {
    margin-right: 275px !important;
  }
}
/* Dashboard container */
@media(min-width: 992px) {
  #dashboard-container {
    margin-left: 275px !important;
  }
}
.dashboard-card {
  box-shadow: 0 .07em .125em 0 rgba(0,0,0,.11) !important;
}
</style>
