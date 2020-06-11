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
        <div class="row">
          <div class="col-12 text-left">
            <back-link :url="returnPath" text="Asignación de talleres"></back-link>
          </div>
          <!-- Col -->
          <div class="col-12 col-md-7">
            <dashboard-title title="Desasignar el taller del ciclo"></dashboard-title>
          </div>
          <!-- /.Col -->
          <!-- Col -->
          <div class="col-12 col-lg-8">
            <p>Esta acción no se puede deshacer.</p>
            <p>El taller segirá existiendo, pero ya no sera parte del ciclo lectivo {{cycle_workshop.year}} - {{cycle_workshop.semester}}.</p>
            <p>Además toda la información relacionada con el taller se perderá, incluyendo los alumnos que concurren y los docentes que lo dictan.</p>
            <!-- Form -->
            <form v-on:submit.prevent="unAssignWorkshop">
              <!-- Row -->
              <div class="row justify-content-end mt-4">
                <input class="display-none" v-model="cycle_workshop_id">
                <!-- Col 12 -->
                <div class="col-12 col-lg-5">
                  <button type="submit" class="btn seed-btn-b btn-block waves-effect mx-0">Cofirmar</button>
                </div>
                <!-- /.Col 12 -->
              </div>
              <!-- /.Row -->
            </form>
            <!-- /.Form -->

          </div>
          <!-- /.Col -->
        </div>
      </template>
      <!-- /.Content -->
    </dashboard>
  </div>
</template>

<script>
import axios from 'axios'
import Dashboard from '@/views/Dashboard'
import dashboardTitle from '@/components/dashboard/Title'
import backLink from '@/components/dashboard/buttons/BackLink'
import alert from '@/components/Alert'

export default {
  data () {
    return {
      pagetitle: 'Desasignar taller',
      cycle_workshop: '',
      returnPath: '/cycle_workshops/',
      messageData: false
      // From data
    }
  },
  props: {
    cycle_workshop_id: Number
  },
  mounted () {
    this.fetchData()
  },
  components: {
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'back-link': backLink,
    'alert': alert
  },
  methods: {
    fetchData () {
      const path = '/api/cycle_workshop/' + this.cycle_workshop_id
      axios.get(path).then((res) => {
        this.cycle_workshop = res.data
      }).catch((error) => {
        console.log(error)
        this.fetchData()
      })
    },
    unAssignWorkshop () {
      this.messageData = false
      const path = '/api/workshop/unassign'
      axios.post(path, {
        cycle_workshop_id: this.cycle_workshop_id
      }).then((res) => {
        this.messageData = res.data
        setTimeout(function () {
          window.location.href = '/cycle_workshops/'
        }, 800)
      }).catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>
