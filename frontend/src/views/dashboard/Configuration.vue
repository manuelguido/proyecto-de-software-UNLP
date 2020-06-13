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
        <form v-on:submit.prevent="updateConfiguration">
          <!-- Row -->
          <div class="row mt-3">
            <!-- Información de persona responsable -->
            <div class="col-12 col-lg-8">
              <dashboard-title title="Información del sitio"></dashboard-title>

              <!-- Row -->
              <div class="row">

                <!-- Activo/Inactivo -->
                <div class="col-12 col-lg-6 my-3">
                  <div class="form-group">
                    <form-label name="Activo / Inactivo"></form-label>
                    <select class="browser-default custom-select" v-model="active" required>
                      <option value="0">Inactivo</option>
                        <option value="1">Activo</option>
                      </select>
                  </div>
                </div>

                <!-- Titulo -->
                <div class="col-12 my-3">
                  <mdb-input label="Titulo" v-model="title" required />
                </div>

                <!-- Email -->
                <div class="col-12 my-3">
                  <mdb-input label="Email" v-model="email" required />
                </div>

                <!-- Descripción -->
                <div class="col-12 my-3">
                  <mdb-input label="Descripción del sitio" v-model="description" type="textarea" :rows="5"/>
                </div>

              </div>

              <!-- Row -->
              <div class="row justify-content-end">

                <!-- Col 12 -->
                <div class="col-12 col-lg-5 mt-4">
                  <button type="submit" class="btn seed-btn-a btn-block waves-effect mx-0">Guardar</button>
                </div>
                <!-- /.Col 12 -->

              </div>
              <!-- /.Row -->

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
import alert from '@/components/Alert'

export default {
  data () {
    return {
      pagetitle: 'Administración del sitio',
      messageData: '',
      active: '',
      title: '',
      email: '',
      description: ''
    }
  },
  created () {
    this.fetchData()
  },
  components: {
    mdbInput,
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'form-label': formLabel,
    'alert': alert
  },
  methods: {
    fetchData () {
      const path = '/api/configuration'
      axios.get(path).then((res) => {
        this.active = res.data[0].active
        this.title = res.data[0].title
        this.email = res.data[0].email
        this.description = res.data[0].description
      }).catch((error) => {
        this.fetchData()
        console.log(error)
      })
    },
    updateConfiguration () {
      this.messageData = ''
      const path = '/api/configuration/update'
      axios.post(path, {
        active: this.active,
        title: this.title,
        email: this.email,
        description: this.description
      }).then((res) => {
        this.messageData = res.data
      }).catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>
