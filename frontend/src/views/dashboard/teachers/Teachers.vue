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
            <dashboard-title title="Listado de docentes"></dashboard-title>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <router-link v-if="docente_new" :to="newTeacherPath" class="btn btn-outline-success seed-rounded mx-0"><i class="fas fa-plus mr-3"></i>Nuevo docente</router-link>
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
      pagetitle: 'Docentes',
      teachers: '',
      showTeacherPath: '/teacher/',
      newTeacherPath: '/new/teacher',
      editTeacherPath: '/teacher/edit/',
      docente_show: false,
      docente_new: false,
      docente_update: false,
      columns: [
        {
          label: 'Apellido',
          field: 'lastname',
          sort: 'asc'
        },
        {
          label: 'Nombre',
          field: 'name',
          sort: 'asc'
        },
        {
          label: 'Teléfono',
          field: 'phone',
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
      const path = '/api/teachers'
      axios.get(path).then((respuesta) => {
        this.teachers = respuesta.data
        this.loadTeachers()
      }).catch((error) => {
        this.fetchData()
        console.log(error)
      })
    },
    // Data fetch for permissions
    fetchNew () {
      axios.get('/api/user/permission/docente_new').then((res) => {
        this.docente_new = res.data
      }).catch((error) => {
        this.fetchNew()
        console.log(error)
      })
    },
    fetchShow () {
      axios.get('/api/user/permission/docente_show').then((res) => {
        this.docente_show = res.data
      }).catch((error) => {
        this.fetchShow()
        console.log(error)
      })
    },
    fetchUpdate () {
      axios.get('/api/user/permission/docente_update').then((res) => {
        this.docente_update = res.data
      }).catch((error) => {
        this.fetchUpdate()
        console.log(error)
      })
    },
    loadTeachers () {
      let newrow = {}
      for (let i = 0; i < this.teachers.length; i++) {
        var varshow = '<p class="display-none">-</p>'
        var varedit = '<p class="display-none">-</p>'

        if (this.docente_show) { varshow = '<a href="' + this.showTeacherPath + this.teachers[i].teacher_id + '" class="btn seed-btn-primary btn-sm seed-rounded"><i class="far fa-eye mr-3"></i>Ver</a>' }
        if (this.docente_update) { varedit = '<a href="' + this.editTeacherPath + this.teachers[i].teacher_id + '" class="btn seed-btn-secondary btn-sm seed-rounded"><i class="fas fa-pencil-alt mr-3"></i>Editar</a>' }
        newrow = {
          lastname: this.teachers[i].lastname,
          name: this.teachers[i].name,
          phone: this.teachers[i].phone,
          show: varshow,
          edit: varedit
        }
        this.rows.push(newrow)
      }
    }
  }
}
</script>
