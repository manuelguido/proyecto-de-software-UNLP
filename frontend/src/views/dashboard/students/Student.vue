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
          <div class="col-12 col-lg-3 text-left">
            <back-link :url="returnPath" text="Estudiantes"></back-link>
          </div>
          <!-- /.BackLink -->
          <div class="col-12 col-lg-4 text-right pt-3">
            <router-link :to="editPath" title="Editar"><i class="far fa-edit click-icon"></i></router-link>
            <!-- Form -->
            <form v-on:submit.prevent="deleteStudent" class="display-inline">
              <input class="display-none" value="{{student.student_id}}" v-model="student_id">
              <button type="submit" class="bg-none b-0" title="Eliminar"><i class="fas fa-trash click-icon"></i></button>
            </form>
          </div>
        </div>
        <!-- /.Edition row -->
        <!-- Information row -->
        <div class="row mt-3">
          <div class="col-12 col-lg-7">
            <div class="card seed-shadow seed-s-rounded">
              <div class="card-body">
                <div class="row">
                  <div class="col-12 col-xl-8">
                    <h1 class="h5 w600 black-c">{{student.name}} {{student.lastname}}</h1>
                  </div>
                  <div class="col-12 col-xl-4 text-xl-right">
                    <level-button :level="student.level"></level-button>
                  </div>
                  <div class="col-12">
                    <p class="w600 my-2">Género: {{student.gender}}</p>
                    <p class="w600 my-2">Documento: {{student.document_type}} {{student.document_number}}</p>
                    <p class="w600 my-2">Teléfono: {{student.phone}}</p>
                    <p class="my-2">Fecha de nacimiento: {{student.birth_date | formatDateFull}}</p>
                    <p class="my-2">Barrio: {{student.neighborhood}}</p>
                    <p class="my-2">Escuela: {{student.school}}</p>
                  </div>
                </div>
              </div>
            </div>
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
import backLink from '@/components/dashboard/buttons/BackLink'
import alert from '@/components/Alert'

export default {
  data () {
    return {
      pagetitle: 'Información del estudiante',
      returnPath: '/students',
      editPath: '/student/edit/' + this.student_id,
      student: '',
      confirmDeleteMsg: '¿Estás seguro de eliminar al estudiante? Esta accion no se puede deshacer',
      messageData: {}
    }
  },
  created () {
    this.fetchData()
  },
  props: {
    student_id: Number
  },
  components: {
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'level-button': levelButton,
    'back-link': backLink,
    'alert': alert
  },
  methods: {
    fetchData () {
      const path = '/api/student/' + this.student_id
      axios.get(path).then((response) => {
        this.student = response.data
      }).catch((error) => {
        console.log(error)
        this.fetchData()
      })
    },
    deleteStudent () {
      if (confirm(this.confirmDeleteMsg)) {
        const path = '/api/student/delete'
        axios.post(path, {
          student_id: this.student_id
        }).then((response) => {
          this.messageData = response.data
          setTimeout(function () {
            window.location.href = '/students'
          }, 800)
        }).catch((error) => {
          console.log(error)
        })
      }
    }
  }
}
</script>
