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
          <div class="col-12 col-md-4 text-md-right">
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
      showStudentPath: '/dashboard/student/',
      newStudentPath: '/dashboard/new/student',
      editStudentPath: '/dashboard/student/edit/',
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
      const path = '/api/students'
      axios.get(path).then((respuesta) => {
        this.students = respuesta.data
        this.loadStudents()
      }).catch((error) => {
        console.log(error)
        this.fetchData()
      })
    },
    loadStudents () {
      let newrow = {}
      for (let i = 0; i < this.students.length; i++) {
        newrow = {
          lastname: this.students[i].lastname,
          name: this.students[i].name,
          document: this.students[i].document_type + ' ' + this.students[i].document_number,
          show: '<a href="' + this.showStudentPath + this.students[i].student_id + '" class="btn btn-primary btn-sm seed-rounded"><i class="far fa-eye mr-3"></i>Ver</a>',
          edit: '<a href="' + this.editStudentPath + this.students[i].student_id + '" class="btn btn-primary btn-sm seed-rounded"><i class="far fa-edit mr-3"></i>Editar</a>'
        }
        this.rows.push(newrow)
      }
    }
  }
}
</script>
