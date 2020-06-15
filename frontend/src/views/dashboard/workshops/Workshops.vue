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
          <div class="col-12 col-md-5">
            <dashboard-title title="Listado de talleres"></dashboard-title>
          </div>
          <div class="col-12 col-md-7 text-md-right">
            <router-link v-if="administrativo_new" :to="assignamentPath" class="btn btn-outline-secondary seed-rounded mx-0"><i class="fas fa-plus mr-3"></i>Asignación de talleres</router-link>
            <router-link v-if="administrativo_new" :to="newWorkshopPath" class="btn btn-outline-success seed-rounded mx-0"><i class="fas fa-plus mr-3"></i>Nuevo taller</router-link>
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
      pagetitle: 'Talleres',
      workshops: '',
      showWorkshopPath: '/workshop/',
      newWorkshopPath: '/new/workshop',
      editWorkshopPath: '/workshop/edit/',
      assignamentPath: '/cycle_workshops/',
      // Permissions
      administrativo_new: false,
      administrativo_show: false,
      administrativo_update: false,
      columns: [
        {
          label: 'Nombre',
          field: 'name',
          sort: 'asc'
        },
        {
          label: 'Nombre corto',
          field: 'short_name',
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
      const path = '/api/workshops'
      axios.get(path).then((res) => {
        this.workshops = res.data
        this.loadWorkshops()
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
    loadWorkshops () {
      let newrow = {}
      var varshow
      var varedit
      for (let i = 0; i < this.workshops.length; i++) {
        varshow = '<p class="display-none">-</p>'
        varedit = '<p class="display-none">-</p>'
        if (this.administrativo_show) { varshow = '<a href="' + this.showWorkshopPath + this.workshops[i].workshop_id + '" class="btn seed-btn-primary btn-sm seed-rounded"><i class="far fa-eye mr-3"></i>Ver</a>' }
        if (this.administrativo_update) { varedit = '<a href="' + this.editWorkshopPath + this.workshops[i].workshop_id + '" class="btn seed-btn-secondary btn-sm seed-rounded"><i class="fas fa-pencil-alt mr-3"></i>Editar</a>' }
        newrow = {
          name: this.workshops[i].name,
          short_name: this.workshops[i].short_name,
          show: varshow,
          edit: varedit
        }
        this.rows.push(newrow)
      }
    }
  }
}
</script>
