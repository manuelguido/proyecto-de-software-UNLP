<template>
  <div>
    <dashboard>
      <!-- Title -->
      <template v-slot:page_title>
        {{pagetitle}}
      </template>
      <!-- Content -->
      <template v-slot:dashboard_content>
        <alert :message=messageData></alert>
        <!-- Form -->
        <form v-on:submit.prevent="updateLesson">
          <!-- Row -->
          <div class="row mt-3">
            <!-- Información de la clase -->
            <div class="col-12 col-lg-6">
              <!-- Row -->
              <div class="row justify-content-end">

                <!-- Backlink -->
                <div class="col-12 text-left">
                  <back-link :url="returnPath" text="Clases"></back-link>
                </div>

                <!-- Col 12 -->
                <div class="col-12">

                  <dashboard-title title="Informacion de la clase"></dashboard-title>

                  <div class="row">
                    <!-- Nivel -->
                    <div class="col-lg-12">
                      <div class="form-group">
                        <form-label name="Taller a elegir"></form-label>
                        <select class="browser-default custom-select" v-model="cycle_workshop_id" required>
                          <option selected disabled>Elegir</option>
                          <option v-for="c in cycle_workshops" :key="c.cycle_workshop_id" :value="c.cycle_workshop_id">{{c.year}} {{c.semester}} - {{c.name}}</option>
                        </select>
                      </div>
                    </div>

                    <!-- Nivel -->
                    <div class="col-lg-6">
                      <div class="form-group">
                        <form-label name="Tipo de taller"></form-label>
                        <select class="browser-default custom-select" v-model="workshop_type_id" required>
                          <option selected disabled>Elegir</option>
                          <option v-for="w in workshop_types" :key="w.workshop_type_id" :value="w.workshop_type_id">{{w.name}}</option>
                        </select>
                      </div>
                    </div>

                    <!-- Nivel -->
                    <div class="col-lg-6">
                      <div class="form-group">
                        <form-label name="Nivel"></form-label>
                        <select class="browser-default custom-select" v-model="level_id" required>
                          <option selected disabled>Elegir</option>
                          <option v-for="l in levels" :key="l.level_id" :value="l.level_id">{{l.name}}</option>
                        </select>
                      </div>
                    </div>

                  </div>
                </div>

                <!-- Col 12 -->
                <div class="col-12 col-lg-5 mt-4">
                  <button type="submit" class="btn seed-btn-a btn-block waves-effect mx-0">Actualizar</button>
                </div>
                <!-- /.Col 12 -->

              </div>
              <!-- /.Row -->
            </div>
            <!-- /.Información de la clase -->
          </div>
          <!-- /.Row -->
        </form>
        <!-- /.Form -->
      </template>
    </dashboard>
  </div>
</template>

<script>
import axios from 'axios'
import { mdbInput } from 'mdbvue'
import Dashboard from '@/views/Dashboard'
import dashboardTitle from '@/components/dashboard/Title'
import backLink from '@/components/dashboard/buttons/BackLink'
import formLabel from '@/components/Label'
import alert from '@/components/Alert'

export default {
  props: {
    lesson_id: Number
  },
  data () {
    return {
      pagetitle: 'Editar clase',
      returnPath: '/lessons',
      messageData: {},
      // Form values for select
      cycle_workshops: {},
      workshop_types: {},
      levels: {},
      // Lesson form information
      cycle_workshop_id: '',
      workshop_type_id: '',
      level_id: ''
    }
  },
  created () {
    this.fetchFormData()
    this.fetchLesson()
  },
  components: {
    mdbInput,
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'back-link': backLink,
    'form-label': formLabel,
    'alert': alert
  },
  methods: {
    fetchFormData () {
      const path = '/api/lesson/form_data'
      axios.get(path).then((res) => {
        this.cycle_workshops = res.data.cycle_workshops
        this.workshop_types = res.data.workshop_types
        this.levels = res.data.levels
      }).catch((error) => {
        this.fetchFormData()
        console.log(error)
      })
    },
    fetchLesson () {
      const path = '/api/lesson/' + this.lesson_id
      axios.get(path).then((res) => {
        this.lesson_id = res.data.lesson_id
        this.cycle_workshop_id = res.data.cycle_workshop_id
        this.workshop_type_id = res.data.workshop_type_id
        this.level_id = res.data.level_id
      }).catch((error) => {
        this.fetchLesson()
        console.log(error)
      })
    },
    updateLesson () {
      this.messageData = ''
      const path = '/api/lesson/update'
      axios.post(path, {
        lesson_id: this.lesson_id,
        cycle_workshop_id: this.cycle_workshop_id,
        workshop_type_id: this.workshop_type_id,
        level_id: this.level_id
      }).then((res) => {
        this.messageData = res.data
        var $this = this
        setTimeout(function () {
          $this.messageData = false
          console.log($this.messageData)
        }, 4000)
      }).catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>
