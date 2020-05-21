<template>
  <a :href="item.url" class="list-group-item panel-item waves-effect pl-4 py-2">
    <i :class="item.icon" class="mr-3"></i>{{ item.name }}
  </a>
</template>

<script>
export default {
  props: {
    'item': null
  }
}
</script>

<style scoped>
.panel-item {
  background: none;
  border: 0 none;
  border-top-right-radius: 50px !important;
  border-bottom-right-radius: 50px !important;
  margin-right: 1.1em;
  color: var(--black-a);
}
.panel-item, .panel-item * {
  transition: 0.22s all !important;
}
.panel-item:hover {
  color: var(--seed-primary-dark);
  background: var(--black-d);
}
.panel-item i {
  color: var(--black-c);
}
.panel-item:hover i {
  color: var(--seed-primary-dark);
}
</style>
