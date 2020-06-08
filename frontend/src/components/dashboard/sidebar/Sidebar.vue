<template>
  <div id="panel-sidebar" class="mobile-hide pt-5">
    <div class="container">
      <img id="sidebar-logo" class="uns" src="../../../assets/logo-green-empty.png" />
      <ul class="list-group">
        <menu-item :item=home_link></menu-item>
        <menu-item v-on:click="panelSwitch" v-for="link in links" :key="link.name" :item=link></menu-item>
        <menu-item :item=logout_link @onclick=con></menu-item>
      </ul>
    </div>
  </div>
</template>

<script>
import menuItem from '@/components/dashboard/sidebar/Item'
export default {
  name: 'ItemGroup',
  props: {
    links: ''
  },
  data () {
    return {
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
    'menu-item': menuItem
  }
}
</script>

<style scoped>
#panel-sidebar {
  height: 100vh !important;
  position: fixed;
  background: var(--white-a) !important;
  box-shadow: 0 .07em .125em 0 rgba(0,0,0,.11) !important;
  box-shadow: none;
  width: 270px;
  left: 0;
  z-index: 1070;
}
#sidebar-logo {
  display: block;
  margin: 40px auto 30px auto !important;
  width: 80%;
}
</style>
