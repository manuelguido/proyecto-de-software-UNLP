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
        <!-- Form -->
        <form v-on:submit.prevent="createStudent">
          <!-- Row -->
          <div class="row mt-3 justify-content-end">
            <!-- Backlink -->
            <div class="col-12 text-left">
              <back-link :url="returnPath" text="Estudiantes"></back-link>
            </div>
            <!-- /.BackLink -->
            <!-- Información del estudiante -->
            <div class="col-12 col-lg-6 border-right">
              <dashboard-title title="Informacion del estudiante"></dashboard-title>
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

                <!-- Escuela -->
                <div class="col-lg-6">
                  <div class="form-group">
                    <form-label name="Escuela"></form-label>
                    <select class="browser-default custom-select" v-model="school_id" required>
                      <option selected disabled>Elegir</option>
                      <option v-for="s in schools" :key="s.school_id" :value="s.school_id">{{s.name}}</option>
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

                <!-- Barrio -->
                <div class="col-lg-6">
                  <div class="form-group">
                    <form-label name="Barrio"></form-label>
                    <select class="browser-default custom-select" v-model="neighborhood_id" required>
                      <option selected disabled>Elegir</option>
                      <option v-for="n in neighborhoods" :key="n.neighborhood_id" :value="n.neighborhood_id">{{n.name}}</option>
                    </select>
                  </div>
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

            <!-- Información de persona responsable -->
            <div class="col-12 col-lg-6">
              <dashboard-title title="Información de la persona responsable"></dashboard-title>
              <!-- Row -->
              <div class="row">
                <!-- Nombre -->
                <div class="col-lg-6">
                  <mdb-input label="Nombre" v-model="responsable_name" required />
                </div>
                <!-- Apellido -->
                <div class="col-lg-6">
                  <mdb-input label="Apellido" v-model="responsable_lastname" required />
                </div>

                <!-- Teléfono -->
                <div class="col-lg-6">
                  <mdb-input label="Teléfono" v-model="responsable_phone" type="number" :min="0" required />
                </div>
                <!-- Madre/Padre o Tutor -->
                <div class="col-lg-6">
                  <div class="form-group">
                    <form-label name="Madre?Padre/Tutor"></form-label>
                    <select class="browser-default custom-select" v-model="responsable_type_id" required>
                      <option selected disabled>Elegir</option>
                      <option v-for="r in responsable_types" :key="r.responsable_type_id" :value="r.responsable_type_id">{{r.name}}</option>
                    </select>
                  </div>
                </div>

              </div>
              <!-- /.Row -->
            </div>
            <!-- /.Información de persona responsable -->
            <div class="col-12 col-lg-4 mt-4">
              <button type="submit" class="btn seed-btn-a btn-block waves-effect mx-0">Guardar</button>
            </div>
          </div>
          <!-- Row -->
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
  data () {
    return {
      pagetitle: 'Cargar un nuevo estudiante',
      returnPath: '/students',
      student: '',
      messageData: {},
      // Form values for select
      neighborhoods: {},
      levels: {},
      genders: {},
      schools: {},
      document_types: {},
      locations: {},
      responsable_types: {},
      // Student form information
      name: '',
      lastname: '',
      document_type_id: '',
      document_number: '',
      gender_id: '',
      birth_date: '',
      school_id: '',
      level_id: '',
      address: '',
      phone: '',
      neighborhood_id: '',
      location_id: '',
      responsable_name: '',
      responsable_lastname: '',
      responsable_phone: '',
      responsable_type_id: ''
    }
  },
  mounted () {
    this.fetchFormData()
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
      const path = '/api/student/form_data'
      axios.get(path).then((res) => {
        this.neighborhoods = res.data.neighborhoods
        this.levels = res.data.levels
        this.genders = res.data.genders
        this.schools = res.data.schools
        this.document_types = res.data.document_types
        this.locations = res.data.locations
        this.responsable_types = res.data.responsable_types
      }).catch((error) => {
        this.fetchFormData()
        console.log(error)
      })
    },
    restoreValues () {
      this.name = ''
      this.lastname = ''
      this.document_type_id = ''
      this.document_number = ''
      this.gender_id = ''
      this.birth_date = ''
      this.school_id = ''
      this.level_id = ''
      this.address = ''
      this.phone = ''
      this.neighborhood_id = ''
      this.location_id = ''
      this.responsable_name = ''
      this.responsable_lastname = ''
      this.responsable_phone = ''
      this.responsable_type_id = ''
    },
    createStudent () {
      this.message = ''
      const path = '/api/student/create'
      axios.post(path, {
        name: this.name,
        lastname: this.lastname,
        birth_date: this.birth_date,
        neighborhood_id: this.neighborhood_id,
        level_id: this.level_id,
        address: this.address,
        gender_id: this.gender_id,
        school_id: this.school_id,
        document_type_id: this.document_type_id,
        document_number: this.document_number,
        phone: this.phone,
        location_id: this.location_id,
        responsable_name: this.responsable_name,
        responsable_lastname: this.responsable_lastname,
        responsable_phone: this.responsable_phone,
        responsable_type_id: this.responsable_type_id
      }).then((res) => {
        if (res.data.status === 'success') {
          this.restoreValues()
        }
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

<style scoped>
@media (min-width: 992px) {
  .border-right {
    border-right: 1px solid var(--white-d) !important;
  }
}
</style>
