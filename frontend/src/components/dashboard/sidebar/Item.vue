<template>
  <router-link :to="item.url" class="list-group-item px-3 py-2 waves-effect">
    <span class="icon"><i :class="item.icon" class="mx-auto"></i></span>
    {{ item.name }}
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
.icon {
  display: inline-block;
  width: 34px !important;
  text-align: center !important;
}
.list-group-item {
  border: 0 none !important;
  background: none;
  transition: 0s all !important;
  font-size: 16px;
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
  background: var(--color-c);
}

.list-group-item.router-link-active i,
.list-group-item.router-link-exact-active i {
  color: var(--white-a);
}

.list-group-item.router-link-active,
.list-group-item.router-link-exact-active {
  background: var(--color-a);
  color: var(--white-a);
}
</style>
