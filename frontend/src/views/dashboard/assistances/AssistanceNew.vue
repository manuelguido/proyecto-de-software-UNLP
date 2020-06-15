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
            <back-link :url="returnPath" text="Asistencias"></back-link>
          </div>
        </div>
        <!-- /.Edition row -->
        <!-- Row -->
        <div class="row my-3">
          <!-- Col 8 -->
          <div class="col-12 col-xl-8">
            <!-- Card -->
            <div class="card">
              <!-- Header -->
              <div class="card-header">
                <h1 class="h6 w600 black-c my-0">{{lesson.year}} - {{lesson.semester}}</h1>
              </div>
              <!-- Body -->
              <div class="card-body">
                <p class="mb-3 black-c">{{lesson.workshop}} ({{lesson.workshop_type}})</p>
                <level-button :level="lesson.level"></level-button>
              </div>
            </div>
            <!-- /.Card -->
          </div>
          <!-- /.Col 8 -->

          <!-- Col 12 -->
          <div class="col-12 col-xl-8 pt-5 mt-5">
            <dashboard-title title="Informacion para pasar asistencia"></dashboard-title>
            <!-- Form for adding a schedule -->
            <form v-on:submit.prevent="fetchStudents">
              <!-- Row -->
              <div class="row justify-content-end">
                <!-- Docente -->
                <div class="col-12 col-lg-6 mb-2">
                  <div class="form-group">
                    <form-label name="Docente que pasa asistencia"></form-label>
                    <select class="browser-default custom-select" v-model="new_teacher_id" required>
                      <option value="0" selected disabled>Elegir</option>
                      <option v-for="t in teachers" :key="t.teacher_id" :value="t.teacher_id">
                        {{t.name}} {{t.lastname}} ({{t.document_type}} {{t.document_number}})
                      </option>
                    </select>
                  </div>
                </div>
                <!-- Fecha de nacimiento -->
                <div class="col-12 col-lg-6">
                  <mdb-input label="Fecha" v-model="new_date" type="date" required />
                </div>
                <!-- Horario -->
                <div class="col-12 mb-2">
                  <div class="form-group">
                    <form-label name="Horario de la clase"></form-label>
                    <select class="browser-default custom-select" v-model="new_schedule_id" required>
                      <option value="0" selected disabled>Elegir</option>
                      <option v-for="s in schedules" :key="s.schedule_id" :value="s.schedule_id">
                        {{s.day}} ({{s.hour_from}} - {{s.hour_to}}), en: {{s.core}}
                      </option>
                    </select>
                  </div>
                </div>
                <!-- /.Button -->
                <div class="col-12 col-lg-5 mt-4">
                  <button type="submit" class="btn seed-btn-a btn-block waves-effect mx-0">Buscar</button>
                </div>
              </div>
              <!-- /.Row -->
            </form>
            <!-- /.Form -->

            <dashboard-title title="Listado de alumnos de la clase" class="mt-5"></dashboard-title>
            <table class="table">
              <thead>
                <tr>
                  <th v-for="c in columnsStudents" :key="c.field" scope="col">{{c.label}}</th>
                </tr>
              </thead>
              <tbody>
                <!-- Listado de estudiantes a pasar asistencia -->
                <tr v-for="s in students" :key="s.student_id">
                  <td scope="row">{{s.name}} {{s.lastname}}</td>
                  <td>{{s.document_type}} {{s.document_number}}</td>
                  <td class="text-right">
                    <form v-on:submit.prevent="addAssistance(s.student_id, 1)" class="display-inline p-0 m-0">
                      <button type="submit" class="btn btn-success btn-sm seed-rounded m-0">
                        <i class="fas fa-check mr-3"></i>Presente
                      </button>
                    </form>
                  </td>
                  <td class="text-right">
                    <form v-on:submit.prevent="addAssistance(s.student_id, 0)" class="display-inline p-0 m-0">
                      <button type="submit" class="btn btn-warning btn-sm seed-rounded m-0">
                        <i class="fas fa-minus mr-3"></i>Ausente
                      </button>
                    </form>
                  </td>
                </tr>
                <!-- /.Listado de estudiantes a pasar asistencia -->
              </tbody>
            </table>

          </div>
          <div class="col-12 mt-5">
            <dashboard-title title="Historial de asistencias"></dashboard-title>
            <!-- Tabla de información de asistencias -->
            <dashboard-table :columnas=columns :filas=rows></dashboard-table>
            <!-- Tabla de información de asistencias -->
          </div>
        </div>
        <!-- /.Information row -->
      </template>
    </dashboard>
  </div>
</template>

<script>
import axios from 'axios'
import { mdbInput } from 'mdbvue'
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
      pagetitle: 'Tomar asistencia para la clase',
      returnPath: '/assistances/',
      lesson: '',
      // Assistances data
      students: {},
      // Big table data
      assistances: {},
      // Form data
      teachers: {},
      schedules: {},
      // Form data
      new_teacher_id: 0,
      new_schedule_id: 0,
      new_date: new Date().toISOString().slice(0, 10),
      new_student_id: 0,
      // Messages
      confirmDeleteMsg: '¿Estás seguro de eliminar esta asistencia? Esta accion no se puede deshacer',
      messageData: {},
      // Table data
      columnsStudents: [
        {
          label: 'Estudiante',
          field: 'student',
          sort: 'asc'
        },
        {
          label: 'Documento',
          field: 'document',
          sort: 'asc'
        },
        {
          label: '',
          field: 'assistance'
        },
        {
          label: '',
          field: 'unassistance'
        }
      ],
      columns: [
        {
          label: 'Fecha',
          field: 'date',
          sort: 'asc'
        },
        {
          label: 'Horario',
          field: 'schedule'
        },
        {
          label: 'Estudiante',
          field: 'student'
        },
        {
          label: 'Documento',
          field: 'document'
        },
        {
          label: '',
          field: 'present'
        },
        {
          label: 'Pasó asistencia',
          field: 'teacher'
        }
      ],
      rows: []
    }
  },
  mounted () {
    this.fetchLesson()
    this.fetchSchedules()
    this.fetchTeachers()
    this.fetchAllAssistances()
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
    'alert': alert,
    mdbInput
  },
  methods: {
    fetchLesson () {
      const path = '/api/lesson/' + this.lesson_id
      axios.get(path).then((res) => {
        this.lesson = res.data
      }).catch((error) => {
        console.log(error)
        // this.fetchLesson()
      })
    },
    fetchStudents () {
      const path = '/api/lesson/students/assistance'
      axios.post(path, {
        lesson_id: this.lesson_id,
        schedule_id: this.new_schedule_id,
        date: this.new_date
      }).then((res) => {
        this.students = res.data
        console.log(res.data)
      }).catch((error) => {
        console.log(error)
        // this.fetchStudents()
      })
    },
    fetchSchedules () {
      const path = '/api/schedules/' + this.lesson_id
      axios.get(path).then((res) => {
        this.schedules = res.data
      }).catch((error) => {
        console.log(error)
        // this.fetchSchedules()
      })
    },
    fetchTeachers () {
      const path = '/api/teachers'
      axios.get(path).then((res) => {
        this.teachers = res.data
      }).catch((error) => {
        // this.fetchStudents()
        console.log(error)
      })
    },
    fetchAllAssistances () {
      const path = '/api/assistances/' + this.lesson_id
      axios.get(path).then((res) => {
        this.assistances = res.data
        this.loadAllAssistances()
      }).catch((error) => {
        console.log(error)
      })
    },
    addRow (assistance) {
      var btnclass
      var presente
      var newrow = {}
      if (assistance.present) {
        btnclass = 'success'
        presente = 'PRESENTE'
      } else {
        btnclass = 'warning'
        presente = 'AUSENTE'
      }
      newrow = {
        date: assistance.date,
        schedule: assistance.day + ' (' + assistance.hour_from + ' ' + assistance.hour_to + '), en: ' + assistance.core,
        student: assistance.name + ' ' + assistance.lastname,
        document: assistance.document_type + ' ' + assistance.document_number,
        present: '<span class="btn btn-sm seed-rounded shadow-none c-default w600 m-0 btn-seed-' + btnclass + '">' + presente + '</span>',
        teacher: assistance.teacher_name + ' ' + assistance.teacher_lastname
      }
      this.rows.push(newrow)
    },
    loadAllAssistances () {
      for (let i = 0; i < this.assistances.length; i++) {
        this.addRow(this.assistances[i])
      }
    },
    addAssistance (studentId, newPresent) {
      this.messageData = false
      const path = '/api/assistance/add'
      axios.post(path, {
        lesson_id: this.lesson_id,
        teacher_id: this.new_teacher_id,
        student_id: studentId,
        schedule_id: this.new_schedule_id,
        date: this.new_date,
        present: newPresent
      }).then((res) => {
        this.fetchStudents()
        this.messageData = res.data
        this.loadAllAssistances()
        var $this = this
        setTimeout(function () {
          $this.messageData = false
        }, 4000)
      }).catch((error) => {
        console.log(error)
      })
    },
    removeAssistance (studentId) {
      this.messageData = false
      if (confirm(this.confirmDeleteMsg)) {
        const path = '/api/assistance/remove'
        axios.post(path, {
          lesson_id: this.lesson_id,
          student_id: studentId
        }).then((res) => {
          if (res.data.status === 'success') {
            this.fetchStudents()
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
