<template>
<div>
  <!-- Contenido Principal -->
    <main class="panel">
      <!-- Row-->
      <div class="row m-0 p-0">
        <!-- Menu-->
        <aside id="panel-menu" class="p-0 uns mobile-hide">
          <div id="panel-menu-inner" class="p-0 panel-menu navbar-light pt-5">
            <a href="/dashboard" class="btn btn-primary my-3 mx-0"><i class="fas fa-home mr-3"></i>Inicio</a>
            <ul class="list-group list-group-flush text-left">
              <menu-item v-for="link in links" :key="link.name" :item=link></menu-item>
            </ul>
            <hr>
            <ul class="list-group list-group-flush text-left">
              <menu-item :item=logout_link></menu-item>
            </ul>
          </div>
        </aside>
        <!-- /.Menu -->

        <!-- Columna full width -->
        <div id="panel-content" class="col p-0">
          <navbar title="Dashboard" :links="links"></navbar>
          <!-- Container Fluid -->
          <div class="container-fluid w-100 p-xl-5 p-4 m-0 text-left">
            <slot></slot>
          </div>
          <!-- /.Container Fluid -->
        </div>
      <!--/.Columna full width -->
    </div>
    <!-- /.Row-->
  </main>
  <!-- /Main -->
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
      const path = '/user/routes'
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
@media (min-width: 702px) {#panel-menu { min-height: 100vh;}}
@media (min-width: 992px) {.panel-logo {display: block !important;}}
.panel {
    background: #fff;
}
.nav-link-panel , .nav-link-nombre {
    color: var(--black-a) !important;
    font-weight: 500;
}
.nav-link-panel {
    font-size: 1.2em;
}
.nav-link-nombre {
    font-size: .9em;
}
#panel-menu {
    z-index: 10;
    border-radius: 0;
    background: #f0f3fa;
}
.panel-banner {
    background: #f0f3fa;
}
.navbar-static-top {
    margin-bottom: 0px;
}
.panel-logo {
    margin: 25px auto;
    width: 35%;
    display: none;
}
.panel-main {
    background: #e6e6e4;
    height: 100%;
}
.panel-main .container-fluid {
    margin: 0 auto;
    padding-top: 10vh;
}

.subItem {
    display: none;
}
.icon-rounded {
    padding: 10px;
    margin-right: 4px;
    border-radius: 50px;
}
.full-height {
    height: 100% !important;
}
.navbar-brand {
    color: #444 !important;
    cursor: default !important;
}
.btn-note-detail {
    background: #7ed4c9;
    font-weight: bold;
}
.alert-fixed {
    position: fixed;
    bottom: 9vh;
    top: auto;
    left: 3vw;;
    right: 3vw;
    z-index:9999;
}

.page-buttons {
    display: inline-block !important;
}
#bigmapid {
    height: 60vh;
    width: 100%;
}
#minmapid {
    height: 65vh;
    width: 100%;
}

th, td {
    padding-bottom: 10px !important;
    padding-top: 10px !important;
}
.table-selected {
    background: rgba(44, 118, 149, 0.5) !important;
}
.table-select {
    transition: 0.08s all !important;
}
.table-select:hover {
    background: rgba(44, 118, 149, 0.6) !important;
}
.table-select:active {
    background: rgba(44, 118, 149, 0.8) !important;
}

.instrumento {
    max-height: 300px;
    max-width: 200px;
}
</style>
