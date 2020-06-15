<template>
  <mdb-navbar id="topnav" class="shadow-none m-0 uns" dark>
    <mdb-navbar-brand>
      <span v-if="user" class="h6 white-a w400 ls02 my-3"><i class="fas fa-user-alt mr-2 white-c"></i>{{user.name}} {{user.lastname}}</span>
      <div v-else-if="loading" class="spinner-border color-c my-0" role="status">
        <span class="sr-only">Loading...</span>
      </div>
    </mdb-navbar-brand>
  </mdb-navbar>
</template>

<script>
import axios from 'axios'
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
  data () {
    return {
      user: false,
      loading: true
    }
  },
  methods: {
    // Obtener las rutas del usuario
    getUserData: function () {
      const path = '/api/user/profile'
      axios.get(path).then((res) => {
        this.user = res.data
        localStorage.setItem('user', JSON.stringify(this.user))
        this.loading = false
      }).catch((error) => {
        console.log(error + 'Retring')
        this.getUserData()
      })
    }
  },
  mounted () {
    if (localStorage.user) {
      var loc = localStorage.getItem('user')
      var result = JSON.parse(loc)
      this.user = result
      this.loading = false
    } else {
      this.getUserData()
    }
  }
}
</script>

<style scoped>
#topnav {
  border-bottom: 1px solid #e3e3e3;
  background: #008ad6;
}
</style>
