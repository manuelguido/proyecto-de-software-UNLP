<template>
  <div class="row">
    <div class="col-12">
      <div class="row">
        <div v-for="item in items" :key="item.name" class="col-6 col-lg-3 mb-4">
          <item :item="item"></item>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import dashboardItem from '@/components/dashboard/items/DashboardItem'
export default {
  components: {
    'item': dashboardItem
  },
  props: {
    items: null
  }
}
</script>

<style scoped>
.item-card {
  box-shadow: 0 2px 5px 0 rgba(0,0,0,0.16),0 2px 10px 0 rgba(0,0,0,0.12) !important;
}
.item-card:hover {
  opacity: 0.8;
}
</style>
