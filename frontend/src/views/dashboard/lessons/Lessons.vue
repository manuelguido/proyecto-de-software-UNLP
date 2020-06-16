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
            <dashboard-title title="Listado de clases"></dashboard-title>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <router-link v-if="administrativo_new" :to="newLessonPath" class="btn btn-outline-success seed-rounded mx-0"><i class="fas fa-plus mr-3"></i>Nueva clase</router-link>
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
      pagetitle: 'Clases',
      lessons: '',
      showLessonSchedulesPath: '/lesson/',
      showLessonStudentsPath: '/lesson/students/',
      newLessonPath: '/new/lesson/',
      editLessonPath: '/lesson/edit/',
      // Permissions
      administrativo_new: false,
      administrativo_show: false,
      administrativo_update: false,
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
          field: 'schedules'
        },
        {
          label: '',
          field: 'students'
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
      const path = '/api/lessons'
      axios.get(path).then((res) => {
        this.lessons = res.data
        this.loadLessons()
      }).catch((error) => {
        console.log(error)
        this.fetchData()
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
    addRow (lesson) {
      var newrow
      var varschedules = '<p class="display-none">-</p>'
      var varstudents = '<p class="display-none">-</p>'
      var varedit = '<p class="display-none">-</p>'
      if (this.administrativo_show) {
        varschedules = '<a href="' + this.showLessonSchedulesPath + lesson.lesson_id + '" class="btn seed-btn-primary btn-sm seed-rounded"><i class="far fa-clock mr-3"></i>Horarios</a>'
        varstudents = '<a href="' + this.showLessonStudentsPath + lesson.lesson_id + '" class="btn seed-btn-primary btn-sm seed-rounded"><i class="fas fa-user mr-3"></i>Estudiantes</a>'
      }
      if (this.administrativo_update) { varedit = '<a href="' + this.editLessonPath + lesson.lesson_id + '" class="btn seed-btn-secondary btn-sm seed-rounded"><i class="fas fa-pencil-alt mr-3"></i>Editar</a>' }
      newrow = {
        cycle: lesson.year + ' ' + lesson.semester,
        workshop: lesson.workshop,
        workshop_type: lesson.workshop_type,
        level: lesson.level,
        schedules: varschedules,
        students: varstudents,
        edit: varedit
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
