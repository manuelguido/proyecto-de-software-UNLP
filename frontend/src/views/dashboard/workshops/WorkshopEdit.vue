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
        <form v-on:submit.prevent="updateWorkshop">
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
                  <button type="submit" class="btn seed-btn-b btn-block waves-effect mx-0">Actualizar</button>
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
  props: {
    workshop_id: Number
  },
  data () {
    return {
      pagetitle: 'Editar taller',
      messageData: {},
      // Workshop form information
      name: '',
      short_name: ''
    }
  },
  created () {
    this.fetchWorkshop()
  },
  components: {
    mdbInput,
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'form-label': formLabel,
    'alert': alert
  },
  methods: {
    fetchWorkshop () {
      const path = '/api/workshop/' + this.workshop_id
      axios.get(path).then((res) => {
        this.name = res.data.name
        this.short_name = res.data.short_name
      }).catch((error) => {
        this.fetchWorkshop()
        console.log(error)
      })
    },
    updateWorkshop () {
      this.message = ''
      const path = '/api/workshop/update'
      axios.post(path, {
        workshop_id: this.workshop_id,
        name: this.name,
        short_name: this.short_name
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
