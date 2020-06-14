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
            <back-link :url="returnPath" text="Clases"></back-link>
          </div>
          <!-- /.BackLink -->
          <div class="col-12 col-lg-4 text-right pt-3">
            <router-link :to="editPath" title="Editar"><i class="far fa-edit click-icon"></i></router-link>
            <!-- Form -->
            <form v-on:submit.prevent="deleteLesson" class="display-inline">
              <input class="display-none" v-model="lesson_id">
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
                    <h1 class="h5 w600 black-c">{{lesson.year}} {{lesson.semester}}</h1>
                  </div>
                  <div class="col-12">
                    <p class="w600 my-2">{{lesson.workshop}}</p>
                    <p class="w600 mt-2 mb-3">{{lesson.workshop_type}}</p>
                    <level-button :level="lesson.level"></level-button>
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
      pagetitle: 'Información de la clase',
      returnPath: '/lessons',
      editPath: '/lesson/edit/' + this.lesson_id,
      lesson: '',
      confirmDeleteMsg: '¿Estás seguro de eliminar la clase? Esta accion no se puede deshacer',
      messageData: {}
    }
  },
  created () {
    this.fetchData()
  },
  props: {
    lesson_id: Number
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
      const path = '/api/lesson/' + this.lesson_id
      axios.get(path).then((response) => {
        this.lesson = response.data
      }).catch((error) => {
        console.log(error)
        this.fetchData()
      })
    },
    deleteLesson () {
      if (confirm(this.confirmDeleteMsg)) {
        const path = '/api/lesson/delete'
        axios.post(path, {
          lesson_id: this.lesson_id
        }).then((response) => {
          this.messageData = response.data
          setTimeout(function () {
            window.location.href = '/lessons'
          }, 400)
        }).catch((error) => {
          console.log(error)
        })
      }
    }
  }
}
</script>
