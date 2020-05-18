<template>
<div>
  <!--Navbar-->
  <nav class="home-navbar main-navbar navbar navbar-expand-lg navbar-light no-shadow py-5 px-5 uns fixed-top">
      <!-- Navbar brand -->
      <a class="navbar-brand black3 px-5" href="/">
          <!-- <img src='@/assets/img/logo-black.png' class="nav-logo" alt="logo-de-orquesta-escuela-berisso"> -->
      </a>
      <!-- Collapse button -->
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#basicExampleNav"
          aria-controls="basicExampleNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
      </button>
      <!-- Collapsible content -->
      <div class="collapse navbar-collapse mb-auto row" id="basicExampleNav">
          <!-- Links -->
          <ul class="navbar-nav mr-5">
              <li v-if=estado_sitio.activo class="nav-item"><a href="/">Programación</a></li>
              <li v-if=estado_sitio.activo class="nav-item"><a href="/">Novedades</a></li>
              <li v-if=estado_sitio.activo class="nav-item"><a href="/">Instrumentos</a></li>
              <li v-if=estado_sitio.activo class="nav-item"><a href="/">Orquestas</a></li>
              <li class="nav-item home-login-button">
                  <button class="btn btn-primary btn-rounded" onclick="/login">Iniciar Sesión</button>
              </li>
          </ul>
          <!-- Links -->
      </div>
      <!-- Collapsible content -->
  </nav>
  <!--/.Navbar-->

  <!-- Container -->
  <div class="home-bg">
      <!-- Row-->
      <div v-if=estado_sitio.activo class="row px-5 mx-0 home-row">
          <div class="col-xl-6 px-4">
              <h1 class="home-title">{{ estado_sitio.titulo }}</h1>
              <!-- Row -->
              <div class="row px-0 mx-0 mt-4">
                  <!-- Col -->
                  <div class="col-xl-8 mx-0 px-0">
                      <p class="home-text mt-5">{{ estado_sitio.descripcion }}</p>
                  </div>
                  <!-- /.Col -->
              </div>
              <!-- /.Row -->
              <!-- Row -->
              <div class="row px-0 mx-0 mt-4">
                  <!-- Col -->
                  <div class="col-xl-8 mx-0 px-0">
                      <p class="h4 mt-5">{{ estado_sitio.email }}</p>
                  </div>
                  <!-- /.Col -->
              </div>
              <!-- /.Row -->
          </div>
          <!-- Col-->
          <div class="col-xl-6">
          </div>
          <!-- /.Col-->
      </div>
      <!-- /.Row -->
      <!-- Row-->
      <div v-else class="container-fluid pt-5">
          <div class="row justify-content-center pt-5">
              <div class="col-md-8 py-5">
                  <img src="./assets/error_wallpaper.png" class="w-100 card" alt="el sitio se encuentra en mantenimiento">
              </div>
          </div>
      </div>
      <!-- /.Row -->
  </div>
  <!-- /.Container -->
</div>
</template>

<style>
body, html {
  height: 100% !important;
}

.home-bg {
  /* The image used */
  /* background-image: url("@/assets/homewallpaper.png"); */

  /* Full height */
  height: 100vh !important;

  /* Center and scale the image nicely */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

@media (max-width: 992px) {
  .home-bg {
    background-image: none !important;
    background: #fff !important;
  }
}
</style>

<script>
import axios from 'axios'
export default {
  name: 'Main',
  data () {
    return {
      estado_sitio: ' '
    }
  },
  methods: {
    getInfo () {
      const path = '/api/v1.0/infositio'
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
