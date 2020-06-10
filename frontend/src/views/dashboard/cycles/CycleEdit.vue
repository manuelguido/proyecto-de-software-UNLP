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
        <form v-on:submit.prevent="updateCycle">
          <!-- Row -->
          <div class="row mt-3">
            <!-- Información del ciclo lectivo -->
            <div class="col-12 col-lg-6">
              <!-- Row -->
              <div class="row justify-content-end">
                <!-- Col 12 -->
                <div class="col-12">

                  <dashboard-title title="Informacion del ciclo lectivo"></dashboard-title>

                  <!-- Row -->
                  <div class="row">
                    <!-- Año -->
                    <div class="col-lg-6">
                      <mdb-input label="Año del ciclo" v-model="year" type="number" min="2000" max="2045" required />
                    </div>

                    <!-- Semestre -->
                    <div class="col-lg-6">
                      <div class="form-group">
                        <form-label name="Semestre"></form-label>
                        <select class="browser-default custom-select" v-model="semester_id" required>
                          <option selected disabled>Elegir</option>
                          <option v-for="s in semesters" :key="s.semester_id" :value="s.semester_id">{{s.name}}</option>
                        </select>
                      </div>
                    </div>
                    
                    <!-- Desde -->
                    <div class="col-lg-6">
                      <mdb-input label="Desde" v-model="date_from" type="date" required />
                    </div>

                    <!-- Hasta -->
                    <div class="col-lg-6">
                      <mdb-input label="Hasta" v-model="date_to" type="date" required />
                    </div>

                  </div>
                  <!-- Row -->
                </div>
                <!-- /.Col 12 -->

                <!-- Col 12 -->
                <div class="col-12 col-lg-5 mt-4">
                  <button type="submit" class="btn seed-btn-b btn-block waves-effect mx-0">Guardar</button>
                </div>
                <!-- /.Col 12 -->

              </div>
              <!-- /.Row -->
            </div>
            <!-- /.Información del ciclo lectivo -->
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
import formLabel from '@/components/Label'
import alert from '@/components/Alert'

export default {
  props: {
    cycle_id: Number
  },
  data () {
    return {
      pagetitle: 'Editar ciclo lectivo',
      messageData: {},
      // Form values for select
      semesters: {},
      // Cycle form information
      semester_id: '',
      year: '',
      date_from: '',
      date_to: ''
    }
  },
  created () {
    this.fetchFormData()
    this.fetchCycle()
  },
  components: {
    mdbInput,
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'form-label': formLabel,
    'alert': alert
  },
  methods: {
    fetchFormData () {
      const path = '/api/cycle/form_data'
      axios.get(path).then((res) => {
        this.semesters = res.data.semesters
      }).catch((error) => {
        this.fetchFormData()
        console.log(error)
      })
    },
    fetchCycle () {
      const path = '/api/cycle/' + this.cycle_id
      axios.get(path).then((res) => {
        this.semester_id = res.data.semester_id
        this.year = res.data.year
        this.date_from = res.data.date_from
        this.date_to = res.data.date_to
      }).catch((error) => {
        this.fetchCycle()
        console.log(error)
      })
    },
    updateCycle () {
      this.messageData = false
      const path = '/api/cycle/update'
      axios.post(path, {
        cycle_id: this.cycle_id,
        semester_id: this.semester_id,
        year: this.year,
        date_from: this.date_from,
        date_to: this.date_to
      }).then((res) => {
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
