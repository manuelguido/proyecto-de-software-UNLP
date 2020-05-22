<template>
<div class="home-container">
  <homenav></homenav>
  <!-- Container -->
  <div class="container-fluid">
    <div class="row justify-content-center py-5 my-5">
      <div class="col-12 col-xl-5 py-xl-5">
        <div class="card home-card p-xl-5">
          <div class="card-body p-xl-5">
            <div v-if="estado_sitio.activo">
              <h1 class="h3 w600 mb-4">{{ estado_sitio.titulo }}</h1>
              <p class="h4 mb-2">{{ estado_sitio.descripcion }}</p>
              <p class="h5 mt-5">{{ estado_sitio.email }}</p>
            </div>
            <div v-else>
              <p class="h5">El sitio se encuentra en mantenimiento</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /.Container -->
</div>
</template>

<script>
import axios from 'axios'
import homenav from '@/components/HomeNav'
export default {
  name: 'Main',
  data () {
    return {
      estado_sitio: ' '
    }
  },
  components: {
    'homenav': homenav
  },
  methods: {
    getInfo () {
      const path = '/api/info_sitio'
      axios.get(path).then((respuesta) => {
        this.estado_sitio = respuesta.data
      })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created () {
    this.getInfo()
  }
}
</script>

<style scoped>
.home-container {
  min-height: 100vh;
}
.home-card {
  border-radius: 40px;
  box-shadow: -5px -5px 20px 20% #efeeee;
}
</style>
