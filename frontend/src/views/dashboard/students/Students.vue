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
            <dashboard-title title="Listado de estudiantes"></dashboard-title>
          </div>
          <div v-if="estudiante_new" class="col-12 col-md-4 text-md-right">
            <router-link :to="newStudentPath" class="btn btn-outline-success seed-rounded mx-0"><i class="fas fa-plus mr-3"></i>Nuevo estudiante</router-link>
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
      pagetitle: 'Estudiantes',
      students: '',
      showStudentPath: '/student/',
      newStudentPath: '/new/student',
      editStudentPath: '/student/edit/',
      // Permissions
      estudiante_new: false,
      estudiante_show: false,
      estudiante_update: false,
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
          label: 'Documento',
          field: 'document',
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
      const path = '/api/students'
      axios.get(path).then((respuesta) => {
        this.students = respuesta.data
        this.loadStudents()
      }).catch((error) => {
        console.log(error)
        this.fetchData()
      })
    },
    // Data fetch for permissions
    fetchNew () {
      axios.get('/api/user/permission/estudiante_new').then((res) => {
        this.estudiante_new = res.data
      }).catch((error) => {
        console.log(error)
        this.fetchNew()
      })
    },
    fetchShow () {
      axios.get('/api/user/permission/estudiante_show').then((res) => {
        this.estudiante_show = res.data
      }).catch((error) => {
        this.fetchShow()
        console.log(error)
      })
    },
    fetchUpdate () {
      axios.get('/api/user/permission/estudiante_update').then((res) => {
        this.estudiante_update = res.data
      }).catch((error) => {
        console.log(error)
        this.fetchUpdate()
      })
    },
    loadStudents () {
      let newrow = {}
      for (let i = 0; i < this.students.length; i++) {
        var varshow = '<p class="display-none">-</p>'
        var varedit = '<p class="display-none">-</p>'
        if (this.estudiante_show) { varshow = '<a href="' + this.showStudentPath + this.students[i].student_id + '" class="btn seed-btn-primary btn-sm seed-rounded"><i class="far fa-eye mr-3"></i>Ver</a>' }
        if (this.estudiante_update) { varedit = '<a href="' + this.editStudentPath + this.students[i].student_id + '" class="btn seed-btn-secondary btn-sm seed-rounded"><i class="fas fa-pencil-alt mr-3"></i>Editar</a>' }
        newrow = {
          lastname: this.students[i].lastname,
          name: this.students[i].name,
          document: this.students[i].document_type + ' ' + this.students[i].document_number,
          show: varshow,
          edit: varedit
        }
        this.rows.push(newrow)
      }
    }
  }
}
</script>
