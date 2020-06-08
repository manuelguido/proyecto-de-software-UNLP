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
        <form v-on:submit.prevent="updateInstrument">
          <!-- Row -->
          <div class="row mt-3">
            <!-- Información del instrumento -->
            <div class="col-12 col-lg-6">
              <!-- Row -->
              <div class="row justify-content-end">
                <!-- Col 12 -->
                <div class="col-12">

                  <dashboard-title title="Informacion del instrumento"></dashboard-title>

                  <!-- Row -->
                  <div class="row">
                    <!-- Nombre -->
                    <div class="col-12">
                      <mdb-input label="Nombre" v-model="name" required />
                    </div>
                    <!-- Código -->
                    <div class="col-lg-6">
                      <mdb-input label="Código" v-model="code" required />
                    </div>

                    <!-- Tipo de instrumento -->
                    <div class="col-lg-6">
                      <div class="form-group">
                        <form-label name="Tipo de instrumento"></form-label>
                        <select class="browser-default custom-select" v-model="instrument_type_id" required>
                          <option disabled selected>Elegir</option>
                          <option v-for="i in instrument_types" :key="i.instrument_type_id" :value="i.instrument_type_id">{{i.name}}</option>
                        </select>
                      </div>
                    </div>

                    <div class="col-12 mt-5">
                      <dashboard-title title="Imagen del instrumento"></dashboard-title>
                    </div>
                    <!-- Imagen -->
                    <div class="col-lg-6">
                      <div class="input-group">
                        <div class="input-group-prepend">
                          <span class="input-group-text" id="image-span"><i class="fas fa-image"></i></span>
                        </div>
                        <div class="custom-file">
                          <input type="file" id="image" name="image" class="custom-file-input" aria-describedby="image-span" required >
                          <label class="custom-file-label" for="image">Elegir imagen</label>
                        </div>
                      </div>
                    </div>
                    <!-- /.Imagen -->

                  </div>
                  <!-- /.Row -->

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
            <!-- /.Información del instrumento -->
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
    instrument_id: Number
  },
  data () {
    return {
      pagetitle: 'Editar instrumento',
      instrument: '',
      messageData: false,
      // Form values for select
      instrument_types: {},
      // Docente form information
      name: '',
      code: '',
      instrument_type_id: ''
    }
  },
  created () {
    this.fetchFormData()
    this.fetchInstrument()
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
      const path = '/api/instrument/form_data'
      axios.get(path).then((res) => {
        this.instrument_types = res.data.instrument_types
      }).catch((error) => {
        this.fetchFormData()
        console.log(error)
      })
    },
    fetchInstrument () {
      const path = '/api/instrument/' + this.instrument_id
      axios.get(path).then((res) => {
        this.instrument_id = res.data.instrument_id
        this.name = res.data.name
        this.code = res.data.code
        this.instrument_type_id = res.data.instrument_type_id
      }).catch((error) => {
        this.fetchTeacher()
        console.log(error)
      })
    },
    updateInstrument () {
      const path = '/api/instrument/update'

      var formData = new FormData()
      var imagefile = document.querySelector('#image')
      formData.append('image', imagefile.files[0])
      formData.append('instrument_id', this.instrument_id)
      formData.append('name', this.name)
      formData.append('code', this.code)
      formData.append('instrument_type_id', this.instrument_type_id)

      axios.post(path, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
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
