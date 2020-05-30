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
            <v-map :places="cores"></v-map>
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
      cores: '',
      sub_path: '/dashboard/core/',
      columns: [
        {
          label: 'Núcleo',
          field: 'name',
          sort: 'asc'
        },
        {
          label: 'Dirección',
          field: 'address',
          sort: 'asc'
        },
        {
          label: 'Teléfono',
          field: 'phone',
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
    getCores () {
      const path = '/api/cores'
      axios.get(path).then((respuesta) => {
        this.cores = respuesta.data
        this.loadCores()
      }).catch((error) => {
        console.log(error)
      })
    },
    loadCores () {
      let newrow = {}
      for (let i = 0; i < this.cores.length; i++) {
        newrow = {name: this.cores[i].name, address: this.cores[i].address, phone: this.cores[i].phone}
        this.rows.push(newrow)
      }
    }
  },
  created () {
    this.getCores()
  }
}
</script>
