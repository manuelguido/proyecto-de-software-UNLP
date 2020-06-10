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
        <form v-on:submit.prevent="createWorkshop">
          <!-- Row -->
          <div class="row mt-3">
            <!-- Información del taller -->
            <div class="col-12 col-lg-6">
              <!-- Row -->
              <div class="row justify-content-end">
                <!-- Col 12 -->
                <div class="col-12">

                  <dashboard-title title="Informacion del taller"></dashboard-title>

                  <!-- Row -->
                  <div class="row">
                    <!-- Nombre -->
                    <div class="col-12">
                      <mdb-input label="Nombre" v-model="name" required />
                    </div>

                    <!-- Nombre corto -->
                    <div class="col-12">
                      <mdb-input label="Nombre corto" v-model="short_name" required />
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
            <!-- /.Información del taller -->
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
      pagetitle: 'Cargar un nuevo taller',
      messageData: {},
      // Workshop form information
      name: '',
      short_name: ''
    }
  },
  components: {
    mdbInput,
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'form-label': formLabel,
    'alert': alert
  },
  methods: {
    restoreValues () {
      this.name = ''
      this.short_name = ''
    },
    createWorkshop () {
      this.messageData = ''
      const path = '/api/workshop/create'
      axios.post(path, {
        name: this.name,
        short_name: this.short_name
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
