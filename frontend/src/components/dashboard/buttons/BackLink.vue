<template>
    <router-link :to="url" class="seed-link"><i class="fas fa-chevron-left mr-2"></i>{{text}}</router-link>
</template>

<script>
export default {
  props: ['url', 'text']
}
</script>
