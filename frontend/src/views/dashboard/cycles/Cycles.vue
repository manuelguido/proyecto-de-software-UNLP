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
          <div class="col-12 col-md-6">
            <dashboard-title title="Listado de ciclos lectivos"></dashboard-title>
          </div>
          <div class="col-12 col-md-6 text-md-right">
            <router-link v-if="administrativo_new" :to="newCyclePath" class="btn btn-outline-success seed-rounded mx-0"><i class="fas fa-plus mr-3"></i>Nuevo ciclo lectivo</router-link>
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
import moment from 'moment'

export default {
  data () {
    return {
      pagetitle: 'Ciclos lectivos',
      cycles: '',
      showCyclePath: '/cycle/',
      newCyclePath: '/new/cycle/',
      editCyclePath: '/cycle/edit/',
      // Permissions
      administrativo_new: false,
      administrativo_show: false,
      administrativo_update: false,
      columns: [
        {
          label: 'Año',
          field: 'year',
          sort: 'asc'
        },
        {
          label: 'Semestre',
          field: 'semester',
          sort: 'asc'
        },
        {
          label: 'Período',
          field: 'period'
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
      const path = '/api/cycles'
      axios.get(path).then((res) => {
        this.cycles = res.data
        this.loadCycles()
      }).catch((error) => {
        this.fetchData()
        console.log(error)
      })
    },
    // Data fetch for permissions
    fetchNew () {
      axios.get('/api/user/permission/administrativo_new').then((res) => {
        this.administrativo_new = res.data
      }).catch((error) => {
        this.fetchNew()
        console.log(error)
      })
    },
    fetchShow () {
      axios.get('/api/user/permission/administrativo_show').then((res) => {
        this.administrativo_show = res.data
      }).catch((error) => {
        this.fetchShow()
        console.log(error)
      })
    },
    fetchUpdate () {
      axios.get('/api/user/permission/administrativo_update').then((res) => {
        this.administrativo_update = res.data
      }).catch((error) => {
        this.fetchUpdate()
        console.log(error)
      })
    },
    dateFormat (value) {
      moment.locale('es')
      return moment(String(value)).format('ll')
    },
    loadCycles () {
      let newrow = {}
      var varshow
      var varedit
      for (let i = 0; i < this.cycles.length; i++) {
        varshow = '<p class="display-none">-</p>'
        varedit = '<p class="display-none">-</p>'
        if (this.administrativo_show) { varshow = '<a href="' + this.showCyclePath + this.cycles[i].cycle_id + '" class="btn seed-btn-primary btn-sm seed-rounded"><i class="far fa-eye mr-3"></i>Ver</a>' }
        if (this.administrativo_update) { varedit = '<a href="' + this.editCyclePath + this.cycles[i].cycle_id + '" class="btn seed-btn-secondary btn-sm seed-rounded"><i class="fas fa-pencil-alt mr-3"></i>Editar</a>' }
        newrow = {
          semester: this.cycles[i].semester,
          year: this.cycles[i].year,
          period: 'Desde: ' + this.dateFormat(this.cycles[i].date_from) + '<br>Hasta: &nbsp;' + this.dateFormat(this.cycles[i].date_to),
          show: varshow,
          edit: varedit
        }
        this.rows.push(newrow)
      }
    }
  }
}
</script>
