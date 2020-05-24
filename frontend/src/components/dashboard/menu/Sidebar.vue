<template>
  <div id="panel-sidebar" class="mobile-hide">
    <div class="container px-4">
      <img id="sidebar-logo" class="uns" src="../../../assets/logo-green.png" />
      <ul class="list-group">
        <menu-item :item=home_link></menu-item>
        <menu-item v-on:click="panelSwitch" v-for="link in links" :key="link.name" :item=link></menu-item>
        <menu-item :item=logout_link></menu-item>
      </ul>
    </div>
  </div>
</template>

<script>
import menuItem from '@/components/dashboard/menu/Item'
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
  background: var(--color-a-light);
  box-shadow: 0 .07em .125em 0 rgba(0,0,0,.12) !important;
  box-shadow: none;
  width: 240px;
  left: 0;
  z-index: 1070;
}
#sidebar-logo {
  display: inline-block;
  margin: 0 auto 20px auto !important;
  width: 100%;
}
</style>
