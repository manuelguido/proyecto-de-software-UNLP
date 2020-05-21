<template>
<div>
  <dashboard>
    <div class="row">
      <div class="col-12 col-xl-6">
        <div class="row">
          <div class="col-12">
            <dashboard-title title="Núcleos"></dashboard-title>
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
                    <a :href="nucleo.id" class="btn btn-primary btn-sm"><i class="fas fa-map-marker-alt mr-2"></i>Ver</a>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
                <!-- </div>
                <div class="col-12">
                    <nav class="row">
                        <div class="col-12 text-right">
                            {% if page == 1 %}
                            <a class="btn btn-primary mr-3 disabled" href="/">Anterior</a>
                            {% else %}
                            <a class="btn btn-primary mr-3" href="/panel_nucleos/{{page - 1}}">Anterior</a>
                            {% endif %}
                            {% if lastpage == 1 %}
                            <a class="btn btn-primary mr-3 disabled" href="/">Siguiente</a>
                            {% else %}
                            <a class="btn btn-primary mr-3" href="/panel_nucleos/{{page + 1}}">Siguiente</a>
                            {% endif %}
                        </div>
                    </nav>
                </div> -->
          </div>
        </div>
      </div>
      <div class="col-12 col-lg-6">
				<l-map ref="myMap" @ready="doSomethingOnReady()"></l-map>
        <div id="bigmapid"></div>
      </div>
    </div>
  </dashboard>
</div>
</template>

<script>
import axios from 'axios'
import Dashboard from '@/views/Dashboard'
import dashboardTitle from '@/components/dashboard/Title'
export default {
  data () {
    return {
      nucleos: ''
    }
  },
  components: {
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle
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
	doSomethingOnReady() {
    this.map = this.$refs.myMap.mapObject
  },
  // methods: {
  //   loadmap () {
  //     var latitude, longitude, marker
  //     var mymap = L.map('bigmapid').setView([-34.9060, -57.89], 12.1)

  //     L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
  //       attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
  //       maxZoom: 18,
  //       id: 'mapbox/streets-v11',
  //       accessToken: 'pk.eyJ1IjoibnVtZXJhIiwiYSI6ImNrNDF0bnQ2ejAxZmwzZHB0aTNta3FrZmgifQ.72Hy10HV07lVW5VjaQr9sA'
  //     }).addTo(mymap);

  //     for (let i = 0; i < nucleos.length; i++) {
  //       latitude = nucleos[i].latitude
  //       longitude = nucleos[i].longitude
  //       marker = L.marker([latitude, longitude]).addTo(mymap)
  //     }
  //   }
  // },
  created () {
    this.getNucleos()
  }
}
</script>
