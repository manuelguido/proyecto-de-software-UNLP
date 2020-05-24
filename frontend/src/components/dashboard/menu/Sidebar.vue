<template>
  <div class="panel-sidebar mobile-hide">
    <!--Header-->
    <div class="mb-2 navbar shadow-none">
      <p class="navbar-brand black-d w600">Dashboard</p>
    </div>
    <div class="container py-1 px-4">
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
