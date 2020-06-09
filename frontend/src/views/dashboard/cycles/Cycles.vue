<template>
  <div>
    <dashboard>
      <!-- Title -->
      <template v-slot:page_title>
        {{pagetitle}}
      </template>
      <!-- Content -->
      <template v-slot:dashboard_content>
        <!-- Row -->
        <div class="row">
          <!-- Col -->
          <div class="col-12 col-lg-7 mb-4 mb-lg-5">
            <!-- Card -->
            <div class="">
              <!-- Card body -->
              <div class="">
                <!-- Form -->
                <form v-on:submit.prevent="createCycle">
                  
                  <!-- Row -->
                  <div class="row justify-content-end">

                    <!-- Titulo -->
                    <div class="col-12">
                      <dashboard-title title="Cargar un ciclo lectivo"></dashboard-title>
                    </div>

                    <!-- Año -->
                    <div class="col-6">
                      <mdb-input label="Nombre" v-model="year" type="number" required />
                    </div>
                    <!-- Semestre -->
                    <div class="col-lg-6">
                      <div class="form-group">
                        <form-label name="Semestre"></form-label>
                        <select class="browser-default custom-select" v-model="semester_id" required>
                          <option disabled selected>Elegir</option>
                          <option v-for="s in semesters" :key="s.semester_id" :value="s.semester_id">{{s.name}}</option>
                        </select>
                      </div>
                    </div>

                    <!-- Desde -->
                    <div class="col-6">
                      <mdb-input label="Desde" v-model="date_from" type="date" required />
                    </div>

                    <!-- Hasta -->
                    <div class="col-6">
                      <mdb-input label="Hasta" v-model="date_to" type="date" required />
                    </div>

                    <!-- Col 12 -->
                    <div class="col-12 col-lg-4 mt-4">
                      <button type="submit" class="btn seed-btn-b btn-block waves-effect mx-0">Cargar</button>
                    </div>
                    <!-- /.Col 12 -->

                  </div>
                  <!-- /.Row -->
                </form>
                <!-- /.Form -->
              </div>
              <!-- /.Card Body -->
            </div>
            <!-- /.Card -->
          </div>
          <!-- /.Col -->

          <!-- Col -->
          <div class="col-12 col-md-8">
            <dashboard-title title="Listado de ciclos lectivos"></dashboard-title>
          </div>

          <div class="col-12 col-md-4 text-md-right">
            <router-link :to="newCyclePath" class="btn btn-outline-success seed-rounded mx-0"><i class="fas fa-plus mr-3"></i>Nuevo ciclo lectivo</router-link>
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
import { mdbInput } from 'mdbvue'
import Dashboard from '@/views/Dashboard'
import dashboardTitle from '@/components/dashboard/Title'
import dashboardTable from '@/components/dashboard/Table'
import formLabel from '@/components/Label'

export default {
  data () {
    return {
      pagetitle: 'Ciclos lectivos',
      cycles: '',
      showCyclePath: '/cycle/',
      // newCyclePath: '/new/cycle',
      editCyclePath: '/cycle/edit/',
      // Información para la carga de nuevos ciclos
      semesters: '',
      semester_id: '',
      year: '',
      date_from: '',
      date_to: '',
      // Información para tablas
      columns: [
        {
          label: 'Año',
          field: 'year',
          sort: 'asc'
        },
        {
          label: 'Semestre',
          field: 'semester',
          sort: 'asc'
        },
        {
          label: 'Período',
          field: 'period'
        },
        {
          label: 'Ver',
          field: 'show'
        },
        {
          label: 'Editar',
          field: 'edit'
        }
      ],
      rows: []
    }
  },
  created () {
    this.fetchData()
    this.FetchFormData()
  },
  components: {
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'dashboard-table': dashboardTable
  },
  methods: {
    fetchData () {
      const path = '/api/cycles'
      axios.get(path).then((res) => {
        this.cycles = res.data
        this.loadCycles()
      }).catch((error) => {
        console.log(error)
        this.fetchData()
      })
    },
    fetchFormData () {
      const path = '/api/cycles/form_data'
      axios.get(path).then((res) => {
        this.semesters = res.data.semesters
      }).catch((error) => {
        this.fetchFormData()
        console.log(error)
      })
    },
    restoreValues () {
      this.semester_id = ''
      this.year = ''
      this.date_from = ''
      this.date_to = ''
    },
    createCycle () {
      const path = '/api/cycle/create'

      var formData = new FormData()
      formData.append('semester_id', this.semester_id)
      formData.append('year', this.year)
      formData.append('date_from', this.date_from)
      formData.append('date_to', this.date_to)

      axios.post(path, formData, {

      }).then((res) => {
        if (res.data.status === 'success') {
          this.restoreValues()
        }
        this.messageData = res.data
        var $this = this
        setTimeout(function () {
          $this.messageData = false
        }, 4000)
      }).catch((error) => {
        console.log(error)
      })
    },
    loadCycles () {
      let newrow = {}
      for (let i = 0; i < this.cycles.length; i++) {
        newrow = {
          semester: this.cycles[i].semester,
          year: this.cycles[i].year,
          period: this.cycles[i].date_from + ' - ' + this.cycles[i].date_to,
          show: '<a href="' + this.showCyclePath + this.cycles[i].cycle_id + '" class="btn seed-btn-b btn-sm seed-rounded"><i class="far fa-eye mr-3"></i>Ver</a>',
          edit: '<a href="' + this.editCyclePath + this.cycles[i].cycle_id + '" class="btn seed-btn-b btn-sm seed-rounded"><i class="far fa-edit mr-3"></i>Editar</a>'
        }
        this.rows.push(newrow)
      }
    }
  }
}
</script>
