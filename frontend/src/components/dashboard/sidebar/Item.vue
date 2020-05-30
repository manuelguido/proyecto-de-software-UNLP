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
  transition: 0s all !important;
}
.list-group, .list-group-item {
  border: 0 none !important;
  background: none;
  transition: 0s all !important;
}
.list-group-item {
  font-size: 18px;
  font-weight: 400;
  border-radius: 50px !important;
  color: var(--black-a);
}
.list-group-item i {
  color: var(--black-d);
}
.list-group-item:hover,
.list-group-item:active,
.list-group-item.active {
  background: var(--color-b);
  color: var(--white-a);
}
.list-group-item:hover i,
.list-group-item:active i,
.list-group-item.active i {
  color: var(--white-a);
}
</style>
