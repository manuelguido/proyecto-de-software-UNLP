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
        this.getCores()
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
  },
  mounted () {
    let recaptchaScript = document.createElement('style')
    recaptchaScript.setAttribute('rel', 'stylesheet')
    recaptchaScript.setAttribute('href', 'https://unpkg.com/leaflet@1.6.0/dist/leaflet.css')
    recaptchaScript.setAttribute('integrity', 'sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ==')
    recaptchaScript.setAttribute('crossorigin', '')
    document.head.appendChild(recaptchaScript)

    recaptchaScript = document.createElement('script')
    recaptchaScript.setAttribute('src', 'https://unpkg.com/leaflet@1.6.0/dist/leaflet.js')
    recaptchaScript.setAttribute('integrity', 'sha512-gZwIG9x3wUXg2hdXF6+rVkLF/0Vi9U8D2Ntg4Ga5I5BZpVkVxlJWbSQtXPSiUTtC0TjtGOmxa1AJPuV0CPthew==')
    recaptchaScript.setAttribute('crossorigin', '')
    document.head.appendChild(recaptchaScript)
  }
}
</script>
