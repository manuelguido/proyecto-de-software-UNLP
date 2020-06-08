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
        <form v-on:submit.prevent="createTeacher">
          <!-- Row -->
          <div class="row mt-3">
            <!-- Información del docente -->
            <div class="col-12 col-lg-6">
              <!-- Row -->
              <div class="row justify-content-end">
                <!-- Col 12 -->
                <div class="col-12">

                  <dashboard-title title="Informacion del docente"></dashboard-title>

                  <!-- Row -->
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
import alert from '@/components/Alert'

export default {
  data () {
    return {
      pagetitle: 'Cargar un nuevo docente',
      teacher: '',
      messageData: {},
      // Form values for select
      locations: {},
      genders: {},
      document_types: {},
      // Docente form information
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
    restoreValues () {
      this.name = ''
      this.lastname = ''
      this.document_type_id = ''
      this.document_number = ''
      this.gender_id = ''
      this.birth_date = ''
      this.address = ''
      this.phone = ''
      this.location_id = ''
    },
    createTeacher () {
      this.message = ''
      const path = '/api/teacher/create'
      axios.post(path, {
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
