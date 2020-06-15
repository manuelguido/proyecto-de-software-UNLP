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
            <router-link v-if="instrumento_new" :to="newInstrumentPath" class="btn btn-outline-success seed-rounded mx-0"><i class="fas fa-plus mr-3"></i>Nuevo instrumento</router-link>
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
      showInstrumentPath: '/instrument/',
      newInstrumentPath: '/new/instrument',
      editInstrumentPath: '/instrument/edit/',
      // Permissions
      instrumento_new: false,
      instrumento_show: false,
      instrumento_update: false,
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
          label: '',
          field: 'show'
        },
        {
          label: '',
          field: 'edit'
        }
      ],
      rows: []
    }
  },
  mounted () {
    this.fetchNew()
    this.fetchShow()
    this.fetchUpdate()
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
    // Data fetch for permissions
    fetchNew () {
      axios.get('/api/user/permission/instrumento_new').then((res) => {
        this.instrumento_new = res.data
      }).catch((error) => {
        console.log(error)
        this.fetchNew()
      })
    },
    fetchShow () {
      axios.get('/api/user/permission/instrumento_show').then((res) => {
        this.instrumento_show = res.data
      }).catch((error) => {
        console.log(error)
        this.fetchShow()
      })
    },
    fetchUpdate () {
      axios.get('/api/user/permission/instrumento_update').then((res) => {
        this.instrumento_update = res.data
      }).catch((error) => {
        console.log(error)
        this.fetchUpdate()
      })
    },
    loadInstruments () {
      let newrow = {}
      var varshow
      var varedit
      for (let i = 0; i < this.instruments.length; i++) {
        varshow = '<p class="display-none">-</p>'
        varedit = '<p class="display-none">-</p>'
        if (this.instrumento_show) { varshow = '<a href="' + this.showInstrumentPath + this.instruments[i].instrument_id + '" class="btn seed-btn-primary btn-sm seed-rounded"><i class="far fa-eye mr-3"></i>Ver</a>' }
        if (this.instrumento_update) { varedit = '<a href="' + this.editInstrumentPath + this.instruments[i].instrument_id + '" class="btn seed-btn-secondary btn-sm seed-rounded"><i class="fas fa-pencil-alt mr-3"></i>Editar</a>' }
        newrow = {
          name: this.instruments[i].name,
          code: this.instruments[i].code,
          type: this.instruments[i].type,
          show: varshow,
          edit: varedit
        }
        this.rows.push(newrow)
      }
    }
  }
}
</script>
