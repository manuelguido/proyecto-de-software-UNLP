<template>
  <label class="custom-label black-d w400 ls04 mb-1">
    {{name}}
  </label>
</template>

<script>
export default {
  props: {
    name: String
  }
}
</script>

<style scoped>
.custom-label {
  font-size: 13px;
}
</style>
