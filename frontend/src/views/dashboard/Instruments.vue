<template>
  <div>
    <dashboard>
      <template v-slot:page_title>
        {{page_title}}
      </template>
      <!-- Content -->
      <template v-slot:dashboard_content>
        <div class="row">
          <div class="col-12 col-xl-6">
            <dashboard-title title="Al"></dashboard-title>
          </div>
        </div>
      </template>
    </dashboard>
  </div>
</template>

<script>
import Dashboard from '@/views/Dashboard'

export default {
  data () {
    return {
      page_title: 'Instrumentos',
      instrument_path: '/dashboard/instruments/',
      columns: [
        {
          label: 'Instrumento',
          field: 'instrument',
          sort: 'asc'
        }
      ],
      rows: []
    }
  },
  components: {
    'dashboard': Dashboard
  }
}
</script>
