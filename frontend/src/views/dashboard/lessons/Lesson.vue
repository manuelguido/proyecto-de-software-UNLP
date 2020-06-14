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
            <back-link :url="returnPath" text="Clases"></back-link>
          </div>
        </div>
        <!-- /.Edition row -->
        <!-- Information row -->
        <div class="row my-3">
          <div class="col-12 col-xl-8">
            <div class="card">
              <!-- Header -->
              <div class="card-header">
                <div class="row">
                  <div class="col-9">
                    <!-- Titulo -->
                    <h1 class="h6 w600 black-c my-0">{{lesson.year}} - {{lesson.semester}}</h1>
                  </div>
                  <div class="col-3 text-right">
                    <!-- Edicion -->
                    <router-link :to="editPath" title="Editar"><i class="far fa-edit click-icon"></i></router-link>
                    <!-- Form -->
                    <form v-on:submit.prevent="deleteLesson" class="display-inline">
                      <input class="display-none" v-model="lesson_id">
                      <button type="submit" class="bg-none b-0" title="Eliminar"><i class="fas fa-trash click-icon"></i></button>
                    </form>
                  </div>
                </div>
              </div>
              <!-- Header -->
              <div class="card-body">
                <p class="mb-3 black-c">{{lesson.workshop}} ({{lesson.workshop_type}})</p>
                <level-button :level="lesson.level"></level-button>
              </div>
            </div>
          </div>
          <div class="col-12 col-xl-8 pt-5 mt-5">
            <dashboard-title title="Agregar un horario a la clase"></dashboard-title>
            <!-- Form for adding a schedule -->
            <form v-on:submit.prevent="addSchedule">
              <div class="row justify-content-end">

                <!-- Núcleo -->
                <div class="col-12 col-md-6 mb-2">
                  <div class="form-group">
                    <form-label name="Núcleo"></form-label>
                    <select class="browser-default custom-select" v-model="new_core_id" required>
                      <option value="0" selected disabled>Elegir</option>
                      <option v-for="c in cores" :key="c.core_id" :value="c.core_id">{{c.name}}</option>
                    </select>
                  </div>
                </div>

                <!-- Día -->
                <div class="col-12 col-md-6 mb-2">
                  <div class="form-group">
                    <form-label name="Día"></form-label>
                    <select class="browser-default custom-select" v-model="new_day_id" required>
                      <option value="0" selected disabled>Elegir</option>
                      <option v-for="d in days" :key="d.day_id" :value="d.day_id">{{d.name}}</option>
                    </select>
                  </div>
                </div>

                <!-- Desde hasta -->
                <div class="col-12 col-md-6 mb-2">
                  <form-label name="Desde"></form-label>
                  <input class="form-control" v-model="new_hour_from" type="time" required>
                </div>
                <div class="col-12 col-md-6 mb-2">
                  <form-label name="Hasta"></form-label>
                  <input class="form-control" v-model="new_hour_to" type="time" required>
                </div>

                <!-- /.Información de persona responsable -->
                <div class="col-12 col-lg-5 mt-4">
                  <button type="submit" class="btn seed-btn-a btn-block waves-effect mx-0">Agregar</button>
                </div>

              </div>
            </form>

            <dashboard-title title="Listado de horarios" class="mt-5"></dashboard-title>
            <table class="table">
              <thead>
                <tr>
                  <th v-for="c in columns" :key="c.field" scope="col">{{c.label}}</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="r in schedules" :key="r.schedule_id">
                  <td scope="row">{{r.core}}</td>
                  <td>{{r.day}}</td>
                  <td>
                    De: {{r.hour_from}} hs<br>
                    A: &nbsp; {{r.hour_to}} hs
                  </td>
                  <td class="text-right">
                    <form v-on:submit.prevent="removeSchedule(r.schedule_id)" class="display-inline">
                      <button type="submit" class="btn btn-danger btn-sm seed-rounded" title="Eliminar">
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
      pagetitle: 'Información de la clase y horarios',
      returnPath: '/lessons',
      editPath: '/lesson/edit/' + this.lesson_id,
      lesson: '',
      schedules: {},
      cores: {},
      days: {},
      // Form data
      new_core_id: 0,
      new_day_id: 0,
      new_hour_from: '',
      new_hour_to: '',
      confirmDeleteMsg: '¿Estás seguro de eliminar la clase? Esta accion no se puede deshacer',
      messageData: {},
      // Table data
      columns: [
        {
          label: 'Núcleo',
          field: 'core',
          sort: 'asc'
        },
        {
          label: 'Día',
          field: 'day',
          sort: 'asc'
        },
        {
          label: 'Horario',
          field: 'schedule'
        },
        {
          label: '',
          field: 'delete'
        }
      ]
    }
  },
  created () {
    this.fetchData()
    this.fetchFormData()
    this.fetchSchedules()
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
        console.log(error)
        this.fetchData()
      })
    },
    fetchSchedules () {
      const path = '/api/schedules/' + this.lesson_id
      axios.get(path).then((res) => {
        this.schedules = res.data
      }).catch((error) => {
        console.log(error)
        this.fetchData()
      })
    },
    fetchFormData () {
      const path = '/api/schedule/form_data'
      axios.get(path).then((res) => {
        this.cores = res.data.cores
        this.days = res.data.days
      }).catch((error) => {
        this.fetchFormData()
        console.log(error)
      })
    },
    addRow (schedule) {
      this.schedules.push(schedule)
    },
    deleteLesson () {
      if (confirm(this.confirmDeleteMsg)) {
        const path = '/api/lesson/delete'
        axios.post(path, {
          lesson_id: this.lesson_id
        }).then((res) => {
          this.messageData = res.data
          setTimeout(function () {
            window.location.href = '/lessons'
          }, 400)
        }).catch((error) => {
          console.log(error)
        })
      }
    },
    restoreValues () {
      this.new_core_id = 0
      this.new_day_id = 0
      this.new_hour_from = ''
      this.new_hour_to = ''
    },
    addSchedule () {
      this.messageData = false
      const path = '/api/schedule/add'
      axios.post(path, {
        lesson_id: this.lesson_id,
        core_id: this.new_core_id,
        day_id: this.new_day_id,
        hour_from: this.new_hour_from,
        hour_to: this.new_hour_to
      }).then((res) => {
        if (res.data.status === 'success') {
          this.restoreValues()
          this.addRow(res.data.new_schedule)
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
    removeSchedule (scheduleId) {
      this.messageData = false
      const path = '/api/schedule/remove'
      axios.post(path, {
        schedule_id: scheduleId
      }).then((res) => {
        if (res.data.status === 'success') {
          this.fetchSchedules()
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
</script>
