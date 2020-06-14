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
            <router-link :to="newLessonPath" class="btn btn-outline-success seed-rounded mx-0"><i class="fas fa-plus mr-3"></i>Nueva clase</router-link>
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
      newLessonPath: '/new/lesson/',
      editLessonPath: '/lesson/edit/',
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
      const path = '/api/lessons'
      axios.get(path).then((res) => {
        this.lessons = res.data
        this.loadLessons()
      }).catch((error) => {
        console.log(error)
        this.fetchData()
      })
    },
    addRow (lesson) {
      var newrow = {
        cycle: lesson.year + ' ' + lesson.semester,
        workshop: lesson.workshop,
        workshop_type: lesson.workshop_type,
        level: lesson.level,
        schedules: '<a href="' + this.showLessonSchedulesPath + lesson.lesson_id + '" class="btn seed-btn-primary btn-sm seed-rounded"><i class="far fa-clock mr-3"></i>Horarios</a>',
        edit: '<a href="' + this.editLessonPath + lesson.lesson_id + '" class="btn seed-btn-secondary btn-sm seed-rounded"><i class="fas fa-pencil-alt mr-3"></i>Editar</a>'
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
