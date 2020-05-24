<template slot-scope="page_title">
  <div class="container-fluid">
    <div class="row justify-content-center">
      <!-- Sidebar -->
      <sidebar :links="links"></sidebar>
      <!-- /.Sidebar -->
      <!-- Panel content -->
      <div id="dashboard-container" class="col px-0">
        <navbar :page_title="page_title" :links="links"></navbar>
        <!-- All content -->
        <div id="dashboard-content" class="mt-5 py-5 px-xl-5 px-3 w-100">
          <slot name="dashboard_content"></slot>
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
export default {
  name: 'Dashboard',
  components: {
    'sidebar': sidebar,
    'navbar': navbar
  },
  data () {
    return {
      links: ''
    }
  },
  methods: {
    getRoutes: function () {
      const path = '/api/user/routes'
      axios.get(path).then((respuesta) => {
        this.links = respuesta.data
      })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created () {
    this.getRoutes()
  }
}
</script>

<style scoped>
/* Sidebar */
.panel-sidebar {
  height: 100vh !important;
  position: fixed;
  background: var(--color-a-light);
  box-shadow: 0 .07em .125em 0 rgba(0,0,0,.12) !important;
  box-shadow: none;
  width: 240px;
  left: 0;
  z-index: 1070;
}
/* Panel container */
@media(min-width: 992px) {
  #dashboard-container {
    padding-left: 240px !important;
  }
}
/*Header*/
.panel-header {
  background: var(--color-a-light);
}
.panel-header .breadcrumb {
  margin: 0 !important;
  background: none;
}
.panel-header .breadcrumb * {
  color: var(--black-a);
}
.panel-header #panel-title {
  font-size: 1.14em;
  color: var(--color-a);
  font-weight: 600;
  letter-spacing: 1px;
}
.panel-header .active {
  color: var(--color-a) !important;
}
</style>
