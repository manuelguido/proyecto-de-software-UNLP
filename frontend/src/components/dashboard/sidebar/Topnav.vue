<template>
  <mdb-navbar id="topnav" class="shadow-none m-0" dark>
    <mdb-navbar-brand>
      <span class="white-a w300 ls02 my-3">Manuel</span>
    </mdb-navbar-brand>
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
  }
}
</script>

<style scoped>
#topnav {
  border-bottom: 1px solid #e3e3e3;
  background: #008ad6;
}
</style>
