<template>
  <mdb-navbar id="dashboard-navbar" class="fixed-top shadow-none bg-color-a-light" light>
    <mdb-navbar-brand class="w600 ml-lg-5">
      <p class="color-a my-0">Escuela Orquesta Berisso</p>
    </mdb-navbar-brand>
    <mdb-navbar-toggler class="web-hide color-a">
      <mdb-navbar-nav class="web-hide">
        <router-link to="/dashboard" class="nav-item web-hide"><i class="fas fa-home mr-2"></i>Inicio</router-link>
        <router-link v-for="link in links" :key="link.name" :to="link.url" class="nav-item web-hide"><i :class="link.icon" class="mr-2"></i>{{link.name}}</router-link>
        <router-link to="/logout" class="nav-item web-hide"><i class="fas fa-sign-out-alt mr-2"></i>Cerrar sesión</router-link>
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
    links: null,
    page_title: String
  }
}
</script>

<style scoped>
#dashboard-navbar {
  box-shadow: 0 .07em .125em 0 rgba(0,0,0,.12) !important;
}
@media(min-width: 992px) {
  #dashboard-navbar {
    padding-left: 240px !important;
  }
}
@media(max-width: 992px) {
  #dashboard-navbar {
    padding-left: 20px !important;
    padding-right: 20px !important;
  }
}
.nav-item {
  padding: .5em 1em;
  background: var(--color-a-light);
}
.nav-item {
  border-radius: 6.2px !important;
  border: 0 none !important;
  background: none;
  color: var(--color-a);
  transition: 0.1s all !important;
}
.nav-item:hover,
.nav-item:active,
.nav-item.active {
  background: var(--color-a);
  color: var(--white-a);
}
</style>
