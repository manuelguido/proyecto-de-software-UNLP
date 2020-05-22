<template>
  <div class="container-fluid">
    <div class="row justify-content-center">
        <!-- Left panel menu -->
        <div class="panel-sidebar mobile-hide">
            <!--Header-->
            <div class="mb-2 navbar shadow-none">
              <p class="navbar-brand black-d w600">Dashboard</p>
            </div>
            <!--/.Header -->
            <div class="container py-1 px-4">
                <ul class="list-group">
                  <menu-item :item=home_link></menu-item>
                  <menu-item v-for="link in links" :key="link.name" :item=link></menu-item>
                  <menu-item :item=logout_link></menu-item>
                </ul>
            </div>
        </div>
        <!-- /.Left panel menu -->

        <!-- Panel content -->
        <div id="panel-container" class="col px-0">
            <navbar title="Dashboard" :links="links"></navbar>
            <!-- All content -->
            <div class="p-3 p-lg-5 w-100">
                <slot></slot>
            </div>
        </div>
        <!-- /.Panel content -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import navbar from '@/components/dashboard/Navbar'
import menuItem from '@/components/dashboard/menu/Item'
export default {
  name: 'Main',
  data () {
    return {
      links: '',
      user: null,
      home_link: {
        'name': 'Inicio',
        'url': '/dashboard',
        'icon': 'fas fa-home'
      },
      logout_link: {
        'name': 'Cerrar sesión',
        'url': '/logout',
        'icon': 'fas fa-sign-out-alt'
      }
    }
  },
  components: {
    'navbar': navbar,
    'menu-item': menuItem
  },
  methods: {
    getRoutes () {
      const path = '/api/user/routes'
      axios.get(path).then((respuesta) => {
        this.links = respuesta.data
      })
        .catch((error) => {
          console.log(error)
        })
    }
    // getUser () {
    //   const path = '/api/user/profile'
    //   axios.get(path).then((respuesta) => {
    //     this.user = respuesta.data
    //   })
    //     .catch((error) => {
    //       console.log(error)
    //     })
    // }
  },
  created () {
    this.getRoutes()
    // this.getUser()
  }
}
</script>

<style scoped>
/* Sidebar */
.panel-sidebar {
    height: 100vh !important;
    position: fixed;
    background: var(--color-a-light);
    /* box-shadow: 0 .07em .125em 0 rgba(0,0,0,.15) !important; */
    box-shadow: none;
    width: 240px;
    left: 0;
    z-index: 1070;
}
/* Panel container */
@media(min-width: 992px) {
    #panel-container {
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
