<template>
  <router-link :to="item.url" class="py-3 card dashboard-item waves-effect w-100">
    <div class="card-body">
      <div class="media align-items-center">
        <div class="media-body text-center">
          <i :class="item.icon" class="fa-2x mb-4"></i>
          <h2 class="h6 w200 m-0">{{item.name}}</h2>
        </div>
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
  props: {
    item: null
  }
}
</script>

<style>
.dashboard-item {
  background: var(--white-a);
  transition: 0s all !important;
  box-shadow: 0 .07em .145em 0 rgba(0,0,0,.14) !important;
}
.dashboard-item:hover {
  background: var(--color-b-light);
  text-decoration: none !important;
  opacity: 0.7;
}
.dashboard-item h2 {
  color: var(--black-a);
}
.dashboard-item i {
  color: var(--black-d);
}
.dashboard-item:hover i,
.dashboard-item:hover h2 {
  color: var(--color-b);
}
</style>
