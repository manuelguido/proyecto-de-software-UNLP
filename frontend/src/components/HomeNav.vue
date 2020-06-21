<template>
  <mdb-navbar id="home-navbar" class="py-2 fixed-top" dark>
    <router-link to="/">
      <img id="nav-logo" class="animated fadeIn" src="../assets/logo-white.png">
    </router-link>
    <mdb-navbar-toggler>
      <mdb-navbar-nav left>
        <router-link class="nav-link ml-lg-4" to="/">Programación</router-link>
        <router-link class="nav-link ml-lg-1" to="/">Novedades</router-link>
        <router-link class="nav-link mx-lg-1" to="/">Nuestras Orquestas</router-link>
        <router-link class="nav-link mx-lg-1" to="/">Elegí tu instrumento</router-link>
        <router-link class="nav-link mx-lg-1" to="/">Biblioteca</router-link>
        <router-link class="nav-link mx-lg-1" to="/">Contacto</router-link>
      </mdb-navbar-nav>
      <mdb-navbar-nav right>
        <router-link to="/"><i class="fas fa-search mr-4"></i></router-link>
        <router-link to="/"><i class="fas fa-bell mr-4"></i></router-link>
        <router-link v-if="to_login" to="/login"><i class="fas fa-user"></i></router-link>
      </mdb-navbar-nav>
    </mdb-navbar-toggler>
  </mdb-navbar>
</template>

<script>
import { mdbNavbar, mdbNavbarBrand, mdbNavbarToggler, mdbNavbarNav, mdbNavItem, mdbDropdown, mdbDropdownMenu, mdbDropdownToggle, mdbInput, mdbDropdownItem } from 'mdbvue'
export default {
  name: 'NavbarPage',
  components: {
    mdbNavbar,
    mdbNavbarBrand,
    mdbNavbarToggler,
    mdbNavbarNav,
    mdbNavItem,
    mdbDropdown,
    mdbDropdownMenu,
    mdbDropdownToggle,
    mdbDropdownItem,
    mdbInput
  },
  props: {
    to_login: Boolean
  }
}
</script>

<style scoped>
#home-navbar i, .nav-link {
  transition: 0.2s all !important;
}
@media (min-width: 1366px) {
  #home-navbar {
    padding-left: 200px;
    padding-right: 200px;
  }
}
#home-navbar {
  background: #023C6D !important;
}
#nav-logo {
  height: 48px;
}
.nav-link {
  text-transform: uppercase;
  color: #fff !important;
  font-size: 14px;
  font-weight: 600;
}
#home-navbar i {
  color: #fff;
}
#home-navbar i:hover {
  color: #999;
}
.nav-link:hover {
  color: #999 !important;
}
</style>
