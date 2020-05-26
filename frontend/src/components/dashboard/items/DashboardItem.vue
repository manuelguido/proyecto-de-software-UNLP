<template>
  <router-link :to="item.url" class="py-2 card dashboard-item w-100">
    <div class="card-body">
      <div class="media align-items-center">
        <div class="media-body">
          <h2 class="h5 w200 m-0"><i :class="item.icon" class="mr-3"></i>{{item.name}}</h2>
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
  background: var(--color-a-light);
}
.dashboard-item:hover {
  background: var(--color-a);
  text-decoration: none !important;
  opacity: 0.7;
}
.dashboard-item h2 {
  color: var(--black-c);
}
.dashboard-item i {
  color: var(--color-a);
}
.dashboard-item:hover i, .dashboard-item:hover h2 {
  color: var(--white-a);
}
</style>
