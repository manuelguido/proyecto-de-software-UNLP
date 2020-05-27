<template>
  <mdb-navbar class="bg-white py-3 px-5" light>
    <router-link class="navbar-brand w600" to="/">
      Escuela Orquesta Berisso
    </router-link>
    <mdb-navbar-toggler>
      <mdb-navbar-nav right>
        <router-link v-if="to_login" to="login" class="my-0 btn btn-primary seed-rounded"><i class="fas fa-sign-in-alt mr-3"></i>Iniciar Sesión</router-link>
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
