<template>
  <div id="panel-sidebar" class="mobile-hide p-0">
    <topnav></topnav>
    <div class="container">
      <img id="sidebar-logo" class="uns" src="../../../assets/logo.png" />
      <ul class="list-group px-2">
        <menu-item :item=home_link></menu-item>
        <menu-item v-on:click="panelSwitch" v-for="link in links" :key="link.name" :item=link></menu-item>
        <menu-item :item=logout_link @onclick=con></menu-item>
      </ul>
    </div>
  </div>
</template>

<script>
import menuItem from '@/components/dashboard/sidebar/Item'
import topnav from '@/components/dashboard/sidebar/Topnav'

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
    'menu-item': menuItem,
    'topnav': topnav
  }
}
</script>

<style scoped>
#panel-sidebar {
  height: 100vh !important;
  position: fixed;
  background: var(--white-a) !important;
  box-shadow: 0 .07em .225em 0 rgba(0,0,0,.15) !important;
  box-shadow: none;
  width: 275px;
  left: 0;
  z-index: 1070;
}
#sidebar-logo {
  display: block;
  margin: 15px auto !important;
  width: 70%;
}
.list-group {
  padding: 0 .2em;
  border: 0 none !important;
  background: none;
  transition: 0s all !important;
}
</style>
