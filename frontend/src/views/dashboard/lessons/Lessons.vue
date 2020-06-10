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
            <dashboard-title title="Listado de ciclos lectivos"></dashboard-title>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <router-link :to="newCyclePath" class="btn btn-outline-success seed-rounded mx-0"><i class="fas fa-plus mr-3"></i>Nuevo ciclo lectivo</router-link>
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
      pagetitle: 'Ciclos lectivos',
      cycles: '',
      showCyclePath: '/cycle/',
      newCyclePath: '/new/cycle/',
      editCyclePath: '/cycle/edit/',
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
      const path = '/api/cycles'
      axios.get(path).then((res) => {
        this.cycles = res.data
        this.loadCycles()
      }).catch((error) => {
        console.log(error)
        this.fetchData()
      })
    },
    loadCycles () {
      let newrow = {}
      for (let i = 0; i < this.cycles.length; i++) {
        newrow = {
          semester: this.cycles[i].semester,
          year: this.cycles[i].year,
          period: 'Desde: ' + this.cycles[i].date_from + ', hasta: ' + this.cycles[i].date_to,
          show: '<a href="' + this.showCyclePath + this.cycles[i].cycle_id + '" class="btn seed-btn-b btn-sm seed-rounded"><i class="far fa-eye mr-3"></i>Ver</a>',
          edit: '<a href="' + this.editCyclePath + this.cycles[i].cycle_id + '" class="btn seed-btn-b btn-sm seed-rounded"><i class="far fa-edit mr-3"></i>Editar</a>'
        }
        this.rows.push(newrow)
      }
    }
  }
}
</script>
