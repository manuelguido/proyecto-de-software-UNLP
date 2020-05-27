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
            Un poco de data de Configuración
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
      page_title: 'Configuración del sitio'
    }
  },
  components: {
    'dashboard': Dashboard
  }
}
</script>
