<template>
  <mdb-navbar id="dashboard-navbar" class="fixed-top shadow-none px-3 uns" togglerClass="text-white bg-color-b" dark>
    <mdb-navbar-brand class="nav-brand">
      <span class="white-a w600 ls03 my-3">Panel</span>
    </mdb-navbar-brand>
    <mdb-navbar-toggler>
      <mdb-navbar-nav class="web-hide">
        <router-link to="/dashboard" class="nav-item web-hide">
          <span class="icon"><i class="fas fa-home mr-2"></i></span>Inicio
        </router-link>
        <router-link v-for="link in links" :key="link.name" :to="link.url" class="nav-item web-hide">
          <span class="icon"><i :class="link.icon" class="mx-auto"></i></span>{{link.name}}
        </router-link>
        <router-link to="/logout" class="nav-item web-hide">
          <span class="icon"><i class="fas fa-sign-out-alt mr-2"></i></span>Cerrar sesión
        </router-link>
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
  /* z-index: 10000; */
  border-bottom: 1px solid #e3e3e3;
  background: var(--color-a);
}
/* Dashboard container */
@media(min-width: 992px) {
  .nav-brand {
    margin-left: 275px !important;
  }
}

.nav-item {
  padding: .5em 1em;
  border-radius: 6.2px !important;
  border: 0 none !important;
  background: none;
  color: var(--white-a);
  transition: 0.1s all !important;
}
.nav-item i {
  color: var(--white-b);
}

.icon {
  display: inline-block;
  width: 34px !important;
  text-align: center !important;
}

.nav-item:hover,
.nav-item:active,
.nav-item.active {
  background: var(--color-d);
}

.nav-item.router-link-active,
.nav-item.router-link-exact-active {
  background: var(--color-a);
  color: var(--white-a);
}
.nav-item.router-link-active i,
.nav-item.router-link-exact-active i {
  color: var(--white-a);
}

</style>
