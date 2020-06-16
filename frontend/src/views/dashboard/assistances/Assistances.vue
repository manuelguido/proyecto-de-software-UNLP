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
          <div class="col-12">
            <dashboard-title title="Listado de clases"></dashboard-title>
          </div>
          <div class="col-12">
            <!-- Tabla de información -->
            <dashboard-table :columnas=columns :filas=rows></dashboard-table>
            <!-- Tabla de información -->
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
      pagetitle: 'Pasar asistencia',
      lessons: '',
      newAssistancePath: '/new/assistance/',
      asistencia_new: false,
      columns: [
        {
          label: 'Ciclo lectivo',
          field: 'cycle',
          sort: 'asc'
        },
        {
          label: 'Taller',
          field: 'workshop',
          sort: 'asc'
        },
        {
          label: 'Clase',
          field: 'workshop_type',
          sort: 'asc'
        },
        {
          label: 'Nivel',
          field: 'level',
          sort: 'asc'
        },
        {
          label: '',
          field: 'assistance'
        }
      ],
      rows: []
    }
  },
  created () {
    this.fetchNew()
    this.fetchData()
  },
  components: {
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'dashboard-table': dashboardTable
  },
  methods: {
    fetchData () {
      const path = '/api/lessons'
      axios.get(path).then((res) => {
        this.lessons = res.data
        this.loadLessons()
      }).catch((error) => {
        this.fetchData()
        console.log(error)
      })
    },
    // Data fetch for permissions
    fetchNew () {
      axios.get('/api/user/permission/asistencia_new').then((res) => {
        this.asistencia_new = res.data
      }).catch((error) => {
        this.fetchNew()
        console.log(error)
      })
    },
    addRow (lesson) {
      let newrow
      var varnew = '<p class="display-none">-</p>'
      if (this.asistencia_new) { varnew = '<a href="' + this.newAssistancePath + lesson.lesson_id + '" class="btn seed-btn-primary btn-sm seed-rounded"><i class="fas fa-plus mr-3"></i></i>Pasar asistencia</a>' }
      newrow = {
        cycle: lesson.year + ' ' + lesson.semester,
        workshop: lesson.workshop,
        workshop_type: lesson.workshop_type,
        level: lesson.level,
        assistance: varnew
      }
      this.rows.push(newrow)
    },
    loadLessons () {
      for (let i = 0; i < this.lessons.length; i++) {
        this.addRow(this.lessons[i])
      }
    }
  }
}
</script>
