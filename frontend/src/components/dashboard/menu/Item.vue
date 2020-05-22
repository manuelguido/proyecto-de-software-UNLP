<template>
  <router-link :to="item.url" class="list-group-item px-4 py-2 waves-effect">
    <div class="md-v-line"></div><i :class="item.icon" class="mr-2"></i>{{ item.name }}
  </router-link>
</template>

<script>
export default {
  props: {
    'item': null
  }
}
</script>

<style scoped>
.list-group {
    padding: 0 1em;
}
.list-group-item {
    border-radius: 6.2px !important;
}
.list-group, .list-group-item {
    border: 0 none !important;
    background: none;
    color: var(--black-d);
    transition: 0.1s all !important;
}
.list-group-item:hover,
.list-group-item:active,
.list-group-item.active {
    background: var(--color-a);
    color: var(--white-a);
}
</style>
