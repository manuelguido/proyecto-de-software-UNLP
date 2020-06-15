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
            <back-link :url="returnPath" text="Docentes"></back-link>
          </div>
          <!-- /.BackLink -->
          <div class="col-12 col-lg-4 text-right pt-3">
            <router-link v-if="docente_update" :to="editPath" title="Editar"><i class="far fa-edit click-icon"></i></router-link>
            <!-- Form -->
            <form v-if="docente_destroy" v-on:submit.prevent="deleteTeacher" class="display-inline">
              <input class="display-none" value="{{teacher.teacher_id}}" v-model="teacher_id">
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
                    <h1 class="h5 w600 black-c">{{teacher.name}} {{teacher.lastname}}</h1>
                  </div>
                  <div class="col-12">
                    <p class="w600 my-2">Género: {{teacher.gender}}</p>
                    <p class="w600 my-2">Documento: {{teacher.document_type}} {{teacher.document_number}}</p>
                    <p class="w600 my-2">Teléfono: {{teacher.phone}}</p>
                    <p class="my-2">Fecha de nacimiento: {{teacher.birth_date | formatDateFull}}</p>
                    <p class="my-2">Localidad: {{teacher.location}}</p>
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
      pagetitle: 'Información del docente',
      returnPath: '/teachers',
      editPath: '/teacher/edit/' + this.teacher_id,
      teacher: '',
      confirmDeleteMsg: '¿Estás seguro de eliminar al docente? Esta accion no se puede deshacer',
      messageData: {},
      docente_update: false,
      docente_destroy: false
    }
  },
  created () {
    this.fetchUpdate()
    this.fetchDestroy()
    this.fetchData()
  },
  props: {
    teacher_id: Number
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
      const path = '/api/teacher/' + this.teacher_id
      axios.get(path).then((response) => {
        this.teacher = response.data
      }).catch((error) => {
        console.log(error)
        this.fetchData()
      })
    },
    fetchUpdate () {
      axios.get('/api/user/permission/docente_update').then((res) => {
        this.docente_update = res.data
      }).catch((error) => {
        console.log(error)
        this.fetchUpdate()
      })
    },
    fetchDestroy () {
      axios.get('/api/user/permission/docente_destroy').then((res) => {
        this.docente_destroy = res.data
      }).catch((error) => {
        console.log(error)
        this.fetchDestroy()
      })
    },
    deleteTeacher () {
      if (confirm(this.confirmDeleteMsg)) {
        const path = '/api/teacher/delete'
        axios.post(path, {
          teacher_id: this.teacher_id
        }).then((response) => {
          this.messageData = response.data
          setTimeout(function () {
            window.location.href = '/teachers'
          }, 800)
        }).catch((error) => {
          console.log(error)
        })
      }
    }
  }
}
</script>
