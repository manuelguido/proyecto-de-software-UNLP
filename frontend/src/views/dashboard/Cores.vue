<template>
  <div>
    <dashboard>
      <!-- Title -->
      <template v-slot:page_title>
        {{page_title}}
      </template>
      <!-- Content -->
      <template v-slot:dashboard_content>
        <div class="row">
          <div class="col-12 col-xl-6">
            <dashboard-title title="Listado de núcleos"></dashboard-title>
            <dashboard-table
              :columnas=columns
              :filas=rows
            ></dashboard-table>
          </div>
          <div class="col-12 col-xl-6">
            <dashboard-title title="Ubicación"></dashboard-title>
            <v-map :places="nucleos"></v-map>
          </div>
        </div>
      </template>
    </dashboard>
  </div>
</template>

<script>
import axios from 'axios'
import Dashboard from '@/views/Dashboard'
import dashboardTitle from '@/components/dashboard/Title'
import dashboardTable from '@/components/dashboard/Table'
import vMap from '@/components/dashboard/Map'

export default {
  data () {
    return {
      page_title: 'Núcleos',
      nucleos: '',
      nucleo_path: '/dashboard/nucleo/',
      columns: [
        {
          label: 'Núcleo',
          field: 'nombre',
          sort: 'asc'
        },
        {
          label: 'Dirección',
          field: 'direccion',
          sort: 'asc'
        },
        {
          label: 'Teléfono',
          field: 'telefono',
          sort: 'asc'
        }
      ],
      rows: []
    }
  },
  components: {
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'v-map': vMap,
    'dashboard-table': dashboardTable
  },
  methods: {
    getNucleos () {
      const path = '/api/nucleos'
      axios.get(path).then((respuesta) => {
        this.nucleos = respuesta.data
        this.loadNucleos()
      })
        .catch((error) => {
          console.log(error)
        })
    },
    loadNucleos () {
      let nuevo = {}
      for (let i = 0; i < this.nucleos.length; i++) {
        nuevo = {nombre: this.nucleos[i].nombre, direccion: this.nucleos[i].direccion, telefono: this.nucleos[i].telefono}
        this.rows.push(nuevo)
      }
    }
  },
  created () {
    this.getNucleos()
  }
}
</script>
