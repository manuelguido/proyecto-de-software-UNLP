<template>
  <mdb-navbar class="dashboard-navbar shadow-none" light>
    <mdb-navbar-brand class="brand black-c">{{title}}</mdb-navbar-brand>
    <mdb-navbar-toggler>
      <mdb-navbar-nav class="web-hide text-left">
        <mdb-nav-item v-for="link in links" :key="link.name" :href="link.url" class="black-c"><i :class="link.icon" class="mr-2 black-d"></i>{{link.name}}</mdb-nav-item>
      </mdb-navbar-nav>
    </mdb-navbar-toggler>
  </mdb-navbar>
</template>

<script>
import { mdbNavbar, mdbNavbarBrand, mdbNavbarToggler, mdbNavbarNav, mdbNavItem, mdbDropdown, mdbDropdownMenu, mdbDropdownToggle, mdbInput, mdbDropdownItem } from 'mdbvue'
export default {
  name: 'NavbarPage',
  props: {
    title: String,
    links: null
  },
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
.dashboard-navbar {
  background-color: #f0f3fa;
}
.brand {
  font-size: .7em !important;
  font-weight: 400 !important;
}
</style>
