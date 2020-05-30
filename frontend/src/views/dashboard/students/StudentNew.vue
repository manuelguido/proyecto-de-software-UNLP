<template>
  <div>
    <dashboard>
      <!-- Title -->
      <template v-slot:page_title>
        {{pagetitle}}
      </template>
      <!-- Content -->
      <template v-slot:dashboard_content>
        <div class="row mt-3">
          <div class="col-12">
            Crear nuevo estudiante
          </div>
        </div>
      </template>
    </dashboard>
  </div>
</template>

<script>
// import axios from 'axios'
import Dashboard from '@/views/Dashboard'
import dashboardTitle from '@/components/dashboard/Title'

export default {
  data () {
    return {
      pagetitle: 'Nuevo estudiante',
      student: ''
    }
  },
  components: {
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle
  },
  methods: {
    createStudent () {
      console.log('descartar')
    }
  }
}
</script>
