<template>
  <div>
    <dashboard>
      <!-- Title -->
      <template v-slot:page_title>
        {{pagetitle}}
      </template>
      <!-- Content -->
      <template v-slot:dashboard_content>
        <alert :message="messageData"></alert>
        <!-- Edition row -->
        <div class="row">
          <!-- Backlink -->
          <div class="col-12 text-left">
            <back-link :url="returnPath" text="Horarios de clase"></back-link>
          </div>
        </div>
        <!-- /.Edition row -->
        <!-- Information row -->
        <div class="row my-3">
          <div class="col-12 col-xl-8">

            <div class="card">
              <!-- Header -->
              <div class="card-header">
                <h1 class="h6 w600 black-c my-0">{{lesson.year}} - {{lesson.semester}}</h1>
              </div>
              <!-- Header -->
              <div class="card-body">
                <p class="mb-3 black-c">{{lesson.workshop}} ({{lesson.workshop_type}})</p>
                <level-button :level="lesson.level"></level-button>
              </div>
            </div>

          </div>
          <div class="col-12 col-xl-8 pt-5 mt-5">
            <dashboard-title title="Agregar un estudiante a la clase"></dashboard-title>
            <!-- Form for adding a schedule -->
            <form v-on:submit.prevent="addStudent">
              <div class="row justify-content-end">

                <!-- Núcleo -->
                <div class="col-12 mb-2">
                  <div class="form-group">
                    <form-label name="Estudiante"></form-label>
                    <select class="browser-default custom-select" v-model="new_student_id" required>
                      <option value="0" selected disabled>Elegir</option>
                      <option v-for="s in students" :key="s.student_id" :value="s.student_id">
                        {{s.name}} {{s.lastname}} ({{s.document_type}} {{s.document_number}})
                      </option>
                    </select>
                  </div>
                </div>

                <!-- /.Información de persona responsable -->
                <div class="col-12 col-lg-5 mt-4">
                  <button type="submit" class="btn seed-btn-a btn-block waves-effect mx-0">Asignar</button>
                </div>

              </div>
            </form>

            <dashboard-title title="Listado de alumnos" class="mt-5"></dashboard-title>
            <table class="table">
              <thead>
                <tr>
                  <th v-for="c in columns" :key="c.field" scope="col">{{c.label}}</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="s in lesson_students" :key="s.student_id">
                  <td scope="row">{{s.name}} {{s.lastname}}</td>
                  <td>{{s.document_type}} {{s.document_number}}</td>
                  <td class="text-right">
                    <form v-on:submit.prevent="removeStudent(s.student_id)" class="display-inline p-0 m-0">
                      <button type="submit" class="btn btn-danger btn-sm seed-rounded m-0" title="Eliminar">
                        <i class="fas fa-times"></i>
                      </button>
                    </form>
                  </td>
                </tr>
              </tbody>
            </table>

          </div>
        </div>
        <!-- /.Information row -->
      </template>
    </dashboard>
  </div>
</template>

<script>
import axios from 'axios'
import Dashboard from '@/views/Dashboard'
import dashboardTitle from '@/components/dashboard/Title'
import levelButton from '@/components/dashboard/buttons/LevelButton'
import dashboardTable from '@/components/dashboard/Table'
import backLink from '@/components/dashboard/buttons/BackLink'
import formLabel from '@/components/Label'
import alert from '@/components/Alert'

export default {
  data () {
    return {
      pagetitle: 'Estudiantes asignados a la clase',
      returnPath: '/lesson/' + this.lesson_id,
      lesson: '',
      students: {},
      lesson_students: {},
      // Form data
      new_student_id: 0,
      confirmDeleteMsg: '¿Estás seguro de eliminar el alumno? Esta accion no se puede deshacer',
      messageData: {},
      // Table data
      columns: [
        {
          label: 'Nombre y apellido',
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
          field: 'delete'
        }
      ]
    }
  },
  mounted () {
    this.fetchData()
    this.fetchLessonStudents()
    this.fetchSchedules()
    this.fetchStudents()
  },
  props: {
    lesson_id: Number
  },
  components: {
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'dashboard-table': dashboardTable,
    'level-button': levelButton,
    'form-label': formLabel,
    'back-link': backLink,
    'alert': alert
  },
  methods: {
    fetchData () {
      const path = '/api/lesson/' + this.lesson_id
      axios.get(path).then((res) => {
        this.lesson = res.data
      }).catch((error) => {
        this.fetchData()
        console.log(error)
      })
    },
    fetchLessonStudents () {
      const path = '/api/lesson/students/' + this.lesson_id
      axios.get(path).then((res) => {
        this.lesson_students = res.data
      }).catch((error) => {
        this.fetchLessonStudents()
        console.log(error)
      })
    },
    fetchSchedules () {
      const path = '/api/schedules/' + this.lesson_id
      axios.get(path).then((res) => {
        this.schedules = res.data
      }).catch((error) => {
        this.fetchSchedules()
        console.log(error)
      })
    },
    fetchStudents () {
      const path = '/api/students'
      axios.get(path).then((res) => {
        this.students = res.data
      }).catch((error) => {
        this.fetchStudents()
        console.log(error)
      })
    },
    restoreValues () {
      this.new_student_id = 0
    },
    addStudent () {
      this.messageData = false
      const path = '/api/lesson/student/add'
      axios.post(path, {
        lesson_id: this.lesson_id,
        student_id: this.new_student_id
      }).then((res) => {
        if (res.data.status === 'success') {
          this.restoreValues()
          this.fetchLessonStudents()
        }
        this.messageData = res.data
        var $this = this
        setTimeout(function () {
          $this.messageData = false
        }, 4000)
      }).catch((error) => {
        console.log(error)
      })
    },
    removeStudent (studentId) {
      this.messageData = false
      if (confirm(this.confirmDeleteMsg)) {
        const path = '/api/lesson/student/remove'
        axios.post(path, {
          lesson_id: this.lesson_id,
          student_id: studentId
        }).then((res) => {
          if (res.data.status === 'success') {
            this.fetchLessonStudents()
          }
          this.messageData = res.data
          var $this = this
          setTimeout(function () {
            $this.messageData = false
          }, 4000)
        }).catch((error) => {
          console.log(error)
        })
      }
    }
  }
}
</script>
