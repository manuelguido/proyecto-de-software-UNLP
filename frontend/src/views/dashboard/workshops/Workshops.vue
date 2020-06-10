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
            <router-link :to="assignamentPath" class="btn btn-outline-secondary seed-rounded mx-0"><i class="fas fa-plus mr-3"></i>Asignación de talleres</router-link>
            <router-link :to="newWorkshopPath" class="btn btn-outline-success seed-rounded mx-0"><i class="fas fa-plus mr-3"></i>Nuevo taller</router-link>
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
      assignamentPath: '/workshop_cycles/',
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
      const path = '/api/workshops'
      axios.get(path).then((res) => {
        this.workshops = res.data
        this.loadWorkshops()
      }).catch((error) => {
        console.log(error)
        this.fetchData()
      })
    },
    loadWorkshops () {
      let newrow = {}
      for (let i = 0; i < this.workshops.length; i++) {
        newrow = {
          name: this.workshops[i].name,
          short_name: this.workshops[i].short_name,
          show: '<a href="' + this.showWorkshopPath + this.workshops[i].workshop_id + '" class="btn seed-btn-b btn-sm seed-rounded"><i class="far fa-eye mr-3"></i>Ver</a>',
          edit: '<a href="' + this.editWorkshopPath + this.workshops[i].workshop_id + '" class="btn seed-btn-b btn-sm seed-rounded"><i class="far fa-edit mr-3"></i>Editar</a>'
        }
        this.rows.push(newrow)
      }
    }
  }
}
</script>
