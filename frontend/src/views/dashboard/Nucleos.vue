<template>
<div>
  <dashboard>
    <div class="row">
      <div class="col-12 col-xl-6">
        <dashboard-title
          title="Núcleos"
        ></dashboard-title>
				<template>
          <mdb-datatable
            :data="data"
            striped
            bordered
            :paginated="3"
          />
				</template>
        <div class="table-responsive">
          <table class="table table-striped">
            <thead>
              <tr>
                <th>Núcleo</th>
                <th>Telefono</th>
                <th>Dirección</th>
                <th>Ubicación</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="nucleo in nucleos" :key="nucleo.id">
                <td>{{nucleo.nombre}}</td>
                <td>{{nucleo.telefono}}</td>
                <td>{{nucleo.direccion}}</td>
                <td>
                <a :href="nucleo_path+nucleo.id" class="btn btn-primary btn-sm"><i class="fas fa-map-marker-alt mr-2"></i>Ver</a>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="col-12 col-xl-6">
        <dashboard-title title="Ubicación"></dashboard-title>
        <v-map :places="nucleos"></v-map>
      </div>
    </div>
  </dashboard>
</div>
</template>

<script>
import axios from 'axios'
import Dashboard from '@/views/Dashboard'
import dashboardTitle from '@/components/dashboard/Title'
import { mdbDatatable } from 'mdbvue'
import vMap from '@/components/dashboard/Map'


export default {
  data () {
    return {
      nucleos: '',
			nucleo_path: '/dashboard/nucleo/',
			data: {
        columns: [
          {
            label: 'Name',
            field: 'name',
            sort: 'asc'
          },
          {
            label: 'Position',
            field: 'position',
            sort: 'asc'
          },
          {
            label: 'Office',
            field: 'office',
            sort: 'asc'
          }
        ],
        rows: [
          {
            name: 'Tiger Nixon',
            position: 'System Architect',
            office: 'Edinburgh'
					},
					          {
            name: 'Tiger Nixon',
            position: 'System Architect',
            office: 'Edinburgh'
					},
					          {
            name: 'Tiger Nixon',
            position: 'System Architect',
            office: 'Edinburgh'
					},
					          {
            name: 'Tiger Nixon',
            position: 'System Architect',
            office: 'Edinburgh'
          }
				]
			}
    }
  },
  components: {
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
		'v-map': vMap,
		'mdb-datatable': mdbDatatable
  },
  methods: {
    getNucleos () {
      const path = '/api/nucleos'
      axios.get(path).then((respuesta) => {
        this.nucleos = respuesta.data
      }).catch((error) => {
        console.log(error)
      })
    }
  },
  created () {
    this.getNucleos()
  }
}
</script>
