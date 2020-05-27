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
          <div class="col-12 col-xl-8">
            <dashboard-title title="Listado de estudiantes"></dashboard-title>
            <dashboard-table
              :columnas=columns
              :filas=rows
            ></dashboard-table>
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

export default {
  data () {
    return {
      pagetitle: 'Estudiantes',
      students: '',
      showpath: '/dashboard/student/',
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
      })
    },
    loadStudents () {
      let newrow = {}
      for (let i = 0; i < this.students.length; i++) {
        newrow = {
          lastname: this.students[i].lastname,
          name: this.students[i].name,
          document: this.students[i].document_type + ' ' + this.students[i].document_number,
          show: '<a href="' + this.showpath + this.students[i].student_id + '" class="btn btn-primary btn-sm seed-rounded"><i class="far fa-eye mr-3"></i>Ver</a>'
        }
        this.rows.push(newrow)
      }
    }
  }
}
</script>
