<template>
  <div>
    <dashboard>
      <!-- Title -->
      <template v-slot:page_title>
        {{pagetitle}}
      </template>
      <!-- Content -->
      <template v-slot:dashboard_content>
        <div class="row">
          <!-- /.Table Col -->
          <div class="col-12 col-md-8">
            <dashboard-title title="Listado de instrumentos"></dashboard-title>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <router-link :to="newInstrumentPath" class="btn btn-outline-success seed-rounded mx-0"><i class="fas fa-plus mr-3"></i>Nuevo instrumento</router-link>
          </div>
          <div class="col-12">
            <dashboard-table
              :columnas=columns
              :filas=rows
            ></dashboard-table>
          </div>
          <!-- /.Table Col -->
        </div>
      </template>
      <!-- /.Content -->
    </dashboard>
  </div>
</template>

<script>
import axios from 'axios'
import Dashboard from '@/views/Dashboard'
import dashboardTitle from '@/components/dashboard/Title'
import dashboardTable from '@/components/dashboard/Table'

export default {
  data () {
    return {
      pagetitle: 'Instrumentos',
      instruments: '',
      showInstrumentPath: '/dashboard/instrument/',
      newInstrumentPath: '/dashboard/new/instrument',
      editInstrumentPath: '/dashboard/instrument/edit/',
      columns: [
        {
          label: 'Nombre',
          field: 'name',
          sort: 'asc'
        },
        {
          label: 'Código',
          field: 'code',
          sort: 'asc'
        },
        {
          label: 'Tipo',
          field: 'type',
          sort: 'asc'
        },
        {
          label: 'Ver',
          field: 'show'
        },
        {
          label: 'Editar',
          field: 'edit'
        }
      ],
      rows: []
    }
  },
  created () {
    this.fetchData()
  },
  components: {
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'dashboard-table': dashboardTable
  },
  methods: {
    fetchData () {
      const path = '/api/instruments'
      axios.get(path).then((res) => {
        this.instruments = res.data
        this.loadInstruments()
      }).catch((error) => {
        console.log(error)
        this.fetchData()
      })
    },
    loadInstruments () {
      let newrow = {}
      for (let i = 0; i < this.instruments.length; i++) {
        newrow = {
          name: this.instruments[i].name,
          code: this.instruments[i].code,
          type: this.instruments[i].type,
          show: '<a href="' + this.showInstrumentPath + this.instruments[i].instrument_id + '" class="btn seed-btn-b btn-sm seed-rounded"><i class="far fa-eye mr-3"></i>Ver</a>',
          edit: '<a href="' + this.editInstrumentPath + this.instruments[i].instrument_id + '" class="btn seed-btn-b btn-sm seed-rounded"><i class="far fa-edit mr-3"></i>Editar</a>'
        }
        this.rows.push(newrow)
      }
    }
  }
}
</script>
