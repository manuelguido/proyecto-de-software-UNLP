<template>
  <mdb-navbar id="dashboard-navbar" class="fixed-top shadow-none bg-color-b" dark>
    <mdb-navbar-brand>
      <span class="h5 white-a w600 ls03 my-1">Panel</span>
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
    links: null
  }
}
</script>

<style scoped>
#dashboard-navbar {
  z-index: 10000;
}
/* @media(min-width: 992px) {
  #dashboard-navbar {
    padding-left: 240px !important;
  }
} */
/* @media(max-width: 992px) {
  #dashboard-navbar {
    padding-left: 20px !important;
    padding-right: 20px !important;
  }
} */
.nav-item {
  padding: .5em 1em;
  background: var(--color-a-light);
}
.nav-item {
  border-radius: 6.2px !important;
  border: 0 none !important;
  background: none;
  color: var(--white-a);
  transition: 0.1s all !important;
}
.nav-item:hover,
.nav-item:active,
.nav-item.active {
  background: var(--color-a-light);
  color: var(--white-a);
}
</style>
