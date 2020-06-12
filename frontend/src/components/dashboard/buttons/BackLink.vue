<template>
  <div class="mb-5">
    <span class="align-middle">
      <router-link :to="url" class="backlink btn seed-btn-b-light shadow-none seed-s-rounded m-0 p-3">
        <i class="fas fa-chevron-left color-b my-0"></i>
        <span v-if="text" class="color-b w600 ls03 ml-2 my-0">{{text}}</span>
        </router-link>
    </span>
  </div>
</template>

<script>
export default {
  props: {
    'url': String,
    'text': String
  }
}
</script>

<style scoped>
.backlink:hover {
  opacity: 0.85 !important;
  box-shadow: 0 .07em .325em 0 rgba(0,0,0,.09) !important;
}
</style>
