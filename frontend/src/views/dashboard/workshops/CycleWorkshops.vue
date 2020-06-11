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
            <back-link :url="returnPath" text="Talleres"></back-link>
          </div>
          <!-- Col -->
          <div class="col-12 col-md-7">
            <dashboard-title title="Asignar un taller a un ciclo"></dashboard-title>
          </div>
          <!-- /.Col -->
          <!-- Col -->
          <div class="col-12 col-md-10 col-lg-8 mb-5">

            <!-- Form -->
            <form v-on:submit.prevent="assignWorkshop">
              <!-- Row -->
              <div class="row justify-content-end mt-3">

                <!-- Ciclos -->
                <div class="col-12 col-lg-6 mb-2">
                  <div class="form-group">
                    <form-label name="Tipo de documento"></form-label>
                    <select class="browser-default custom-select" v-model="new_cycle_id" required>
                      <option value="0" selected disabled>Elegir</option>
                      <option v-for="c in cycles" :key="c.cycle_id" :value="c.cycle_id">{{c.year}} {{c.semester}}</option>
                    </select>
                  </div>
                </div>

                <!-- Talleres -->
                <div class="col-12 col-lg-6 mb-2">
                  <div class="form-group">
                    <form-label name="Tipo de documento"></form-label>
                    <select class="browser-default custom-select" v-model="new_workshop_id" required>
                      <option value="0" selected disabled>Elegir</option>
                      <option v-for="w in workshops" :key="w.workshop_id" :value="w.workshop_id">{{w.name}} ({{w.short_name}})</option>
                    </select>
                  </div>
                </div>

                <!-- Col 12 -->
                <div class="col-12 col-lg-3">
                  <button type="submit" class="btn seed-btn-b btn-block waves-effect mx-0">Asignar</button>
                </div>
                <!-- /.Col 12 -->
              </div>
              <!-- /.Row -->
            </form>
            <!-- /.Form -->

          </div>
          <!-- /.Col -->
          <!-- /.Table Col -->
          <div class="col-12 col-md-8">
            <dashboard-title title="Listado de talleres asignados"></dashboard-title>
          </div>
          <div class="col-12">
            <dashboard-table
              :columnas=columns
              :filas=rows
            ></dashboard-table>
          </div>
          <!-- /.Table Col -->
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
import dashboardTable from '@/components/dashboard/Table'
import backLink from '@/components/dashboard/buttons/BackLink'
import formLabel from '@/components/Label'
import alert from '@/components/Alert'

export default {
  data () {
    return {
      pagetitle: 'Talleres asignados',
      cycle_workshops: {},
      returnPath: '/workshops',
      unassignCycleWorkshopPath: '/unassign/workshop/',
      messageData: false,
      // From data
      cycles: {},
      workshops: {},
      new_cycle_id: 0,
      new_workshop_id: 0,
      // Table data
      columns: [
        {
          label: 'Ciclo lectivo',
          field: 'cycle',
          sort: 'asc'
        },
        {
          label: 'Taller',
          field: 'workshop',
          sort: 'asc'
        },
        {
          label: 'Desasignar',
          field: 'unassign'
        }
      ],
      rows: []
    }
  },
  mounted () {
    this.fetchData()
    this.fetchFormData()
  },
  components: {
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'dashboard-table': dashboardTable,
    'form-label': formLabel,
    'back-link': backLink,
    'alert': alert
  },
  methods: {
    fetchData () {
      const path = '/api/cycle_workshops'
      axios.get(path).then((res) => {
        this.cycle_workshops = res.data
        this.loadCycleWorkshops()
      }).catch((error) => {
        console.log(error)
        this.fetchData()
      })
    },
    fetchFormData () {
      const path = '/api/cycle_workshops/form_data'
      axios.get(path).then((res) => {
        this.cycles = res.data.cycles
        this.workshops = res.data.workshops
      }).catch((error) => {
        this.fetchFormData()
        console.log(error)
      })
    },
    addRow (cycleWorkshop) {
      var newrow = {
        cycle: cycleWorkshop.year + ' ' + cycleWorkshop.semester,
        workshop: cycleWorkshop.name,
        unassign: '<a href="' + this.unassignCycleWorkshopPath + cycleWorkshop.cycle_workshop_id + '" class="btn btn-default btn-sm seed-rounded"><i class="fas fa-times mr-3"></i>Desasignar</a>'
      }
      this.rows.push(newrow)
    },
    loadCycleWorkshops () {
      for (let i = 0; i < this.cycle_workshops.length; i++) {
        this.addRow(this.cycle_workshops[i])
      }
    },
    restoreValues () {
      this.new_cycle_id = 0
      this.new_workshop_id = 0
    },
    assignWorkshop () {
      this.messageData = false
      const path = '/api/workshop/assign'
      axios.post(path, {
        cycle_id: this.new_cycle_id,
        workshop_id: this.new_workshop_id
      }).then((res) => {
        if (res.data.status === 'success') {
          this.restoreValues()
          this.addRow(res.data.new_cylce_workshop)
        }
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
