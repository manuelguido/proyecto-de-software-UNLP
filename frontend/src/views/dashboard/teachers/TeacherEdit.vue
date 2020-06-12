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
        <form v-on:submit.prevent="updateTeacher">
          <!-- Row -->
          <div class="row mt-3">
            <!-- Backlink -->
            <div class="col-12 text-left">
              <back-link :url="returnPath" text="Docentes"></back-link>
            </div>
            <!-- /.BackLink -->
            <!-- Información del docente -->
            <div class="col-12 col-lg-6">
              <!-- Row -->
              <div class="row justify-content-end">
                <!-- Col 12 -->
                <div class="col-12">

                  <dashboard-title title="Informacion del docente"></dashboard-title>

                  <div class="row">
                    <!-- Nombre -->
                    <div class="col-lg-6">
                      <mdb-input label="Nombre" v-model="name" required />
                    </div>
                    <!-- Apellido -->
                    <div class="col-lg-6">
                      <mdb-input label="Apellido" v-model="lastname" required />
                    </div>

                    <!-- Tipo de documento -->
                    <div class="col-lg-6">
                      <div class="form-group">
                        <form-label name="Tipo de documento"></form-label>
                        <select class="browser-default custom-select" v-model="document_type_id" required>
                          <option selected disabled>Elegir</option>
                          <option v-for="d in document_types" :key="d.document_type_id" :value="d.document_type_id">{{d.name}}</option>
                        </select>
                      </div>
                    </div>
                    <!-- Numero de documento -->
                    <div class="col-lg-6">
                      <mdb-input label="Número de documento" v-model="document_number" type="number" :min="0" required />
                    </div>

                    <!-- Género -->
                    <div class="col-lg-6">
                      <div class="form-group">
                        <form-label name="Género"></form-label>
                        <select class="browser-default custom-select" v-model="gender_id" required>
                          <option selected disabled>Elegir</option>
                          <option v-for="g in genders" :key="g.gender_id" :value="g.gender_id">{{g.name}}</option>
                        </select>
                      </div>
                    </div>
                    <!-- Fecha de nacimiento -->
                    <div class="col-lg-6">
                      <mdb-input label="Fecha de nacimiento" v-model="birth_date" type="date" required />
                    </div>

                    <!-- Dirección -->
                    <div class="col-lg-6">
                      <mdb-input label="Dirección" v-model="address" required />
                    </div>
                    <!-- Teléfono -->
                    <div class="col-lg-6">
                      <mdb-input label="Teléfono" v-model="phone" type="number" :min="0" required />
                    </div>

                    <!-- Localidad -->
                    <div class="col-lg-6">
                      <div class="form-group">
                        <form-label name="Localidad"></form-label>
                        <select class="browser-default custom-select" v-model="location_id" required>
                          <option selected disabled>Elegir</option>
                          <option v-for="l in locations" :key="l.location_id" :value="l.location_id">{{l.name}}</option>
                        </select>
                      </div>
                    </div>

                  </div>
                </div>

                <!-- Col 12 -->
                <div class="col-12 col-lg-5 mt-4">
                  <button type="submit" class="btn seed-btn-b btn-block waves-effect mx-0">Actualizar</button>
                </div>
                <!-- /.Col 12 -->

              </div>
              <!-- /.Row -->
            </div>
            <!-- /.Información del docente -->
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
import backLink from '@/components/dashboard/buttons/BackLink'
import alert from '@/components/Alert'

export default {
  props: {
    teacher_id: Number
  },
  data () {
    return {
      pagetitle: 'Editar docente',
      returnPath: '/teachers',
      teacher: '',
      messageData: false,
      // Form values for select
      genders: {},
      document_types: {},
      locations: {},
      // Teacher form information
      name: '',
      lastname: '',
      document_type_id: '',
      document_number: '',
      gender_id: '',
      birth_date: '',
      address: '',
      phone: '',
      location_id: ''
    }
  },
  created () {
    this.fetchFormData()
    this.fetchTeacher()
  },
  components: {
    mdbInput,
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'form-label': formLabel,
    'back-link': backLink,
    'alert': alert
  },
  methods: {
    fetchFormData () {
      const path = '/api/teacher/form_data'
      axios.get(path).then((res) => {
        this.genders = res.data.genders
        this.document_types = res.data.document_types
        this.locations = res.data.locations
      }).catch((error) => {
        this.fetchFormData()
        console.log(error)
      })
    },
    fetchTeacher () {
      const path = '/api/teacher/' + this.teacher_id
      axios.get(path).then((res) => {
        this.teacher_id = res.data.teacher_id
        this.name = res.data.name
        this.lastname = res.data.lastname
        this.birth_date = res.data.birth_date
        this.neighborhood_id = res.data.neighborhood_id
        this.address = res.data.address
        this.gender_id = res.data.gender_id
        this.document_type_id = res.data.document_type_id
        this.document_number = res.data.document_number
        this.phone = res.data.phone
        this.location_id = res.data.location_id
      }).catch((error) => {
        this.fetchTeacher()
        console.log(error)
      })
    },
    updateTeacher () {
      this.message = ''
      const path = '/api/teacher/update'
      axios.post(path, {
        teacher_id: this.teacher_id,
        name: this.name,
        lastname: this.lastname,
        birth_date: this.birth_date,
        address: this.address,
        gender_id: this.gender_id,
        document_type_id: this.document_type_id,
        document_number: this.document_number,
        phone: this.phone,
        location_id: this.location_id
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
