<template>
  <div class="uns">
    <homenav :to_login="nav_to_login"></homenav>
    <home-banner></home-banner>
    <div class="container-fluid w-100">
      <div class="row row-eq-height">

        <!-- Blue column -->
        <div class="col-12 col-md-6 col-lg-4 py-5 blue-column text-left">
          <div class="row">
            <div class="col-12 offset-lg-3 col-lg-8">
              <h1 class="h2 white-a georgia">Orquesta Escuela Berisso</h1>
              <p class="white-a italic mb-3 mb-lg-5 georgia">Fundación el 19 de septiembre de 2005</p>
              <p class="white-a arial">
                La Orquesta Escuela de Berisso comenzó a funcionar en septiembre del 2005 en el barrio de El Carmen de la localidad de Berisso bajo la dirección del Mtro. Juan Carlos Herrero, orientada especialmente a la atención de chicos en situación de vulnerabilidad socio-cultural.
                Desde sus 20 alumnos iniciales fue creciendo hasta atender actualmente una matrícula de aproximadamente 530 chicos, distribuidos en los 15 núcleos que la conforman y dirigida a una franja etaria de 5 a 23 años, cubriendo en su accionar a la casi totalidad de los barrios de Berisso más los espacios cedidos por el Club Español y el Teatro Argentino
              </p>
              <p class="white-a arial">
                En 2015, enmarcado en el festejo por sus 10 años, brindó una serie de conciertos entre los que se incluyó la invitación del Teatro Argentino para formar parte del Ciclo de la Sala A. Piazzolla, una presentación en el CCK de Bs. As, un concierto en el Teatro Mitre de San Salvador de Jujuy para presentarse junto al Sistema de Orquestas Juveniles de Jujuy bajo la dirección del Mtro. Sergio Jurado y el estreno de la Misa Mestiza, escrita en honor de SS el papa Francisco, junto al Vocal de Cámara Platense, el coro de Cámara de la facultad de Bellas Artes y el Ensamble de Percusión de Pehuajó, con la dirección del Mtro. Fernando Tomé.
              </p>
            </div>

            <!-- Social icons -->
            <div class="col-12 offset-lg-3 col-lg-8 mt-lg-5">
              <a target="_black" href="/" class="mr-4">
                <i class="fab fa-instagram white-a fa-lg"></i>
              </a>
              <a target="_black" href="/" class="mr-4">
                <i class="fab fa-twitter white-a fa-lg"></i>
              </a>
              <a target="_black" href="/">
                <i class="fab fa-facebook-f white-a fa-lg"></i>
              </a>
            </div>
            <!-- /.Social icons -->

          </div>
        </div>
        <!-- /.Blue column -->

        <!-- Middle column -->
        <div class="col-12 col-md-6 col-lg-4 py-5 text-left">
          <div class="row">
            <div class="col-12 text-right">
              <tooltip/>
            </div>
            <div class="col-12 offset-lg-1 offset-xl-2 col-lg-12 col-xl-10 mt-3 mt-md-5 pt-4">
              <p class="black-b w400 arial">
                Elegí el instrumento que más te gusta y escribinos a oeberisso@gmail.com o por mensaje de Facebook diciéndonos en que zona de Berisso o alrededores vivís, en que horarios vas al colegio y
                te informaremos en cual de nuestros núcleos podés inscribirte, o también podes acercarte los días sábados de 9 a 12hs a la Escuela Nº 25 de Berisso, calle 126 e/ 89 y 90.
              </p>
              <router-link class="btn btn-outline-primary btn-sm mx-0 mt-3 shadow-none" to="/">Ver más</router-link>
            </div>
            <div class="col-12 offset-lg-1 offset-xl-2 col-lg-12 col-xl-10 mt-3 mt-md-5">
              <hr class="my-5 custom-hr">
            </div>
            <div class="col-12 offset-lg-1 offset-xl-2 col-lg-11 col-xl-9 mt-3 mt-md-5">
              <p class="georgia w600 mt-5 quote black-c italic">
                “Lo que buscamos es tender el puente para que estos chicos y chicas accedan a un bien cultural. A veces se piensa que estos proyectos van a ‘salvar vidas’, o van a ‘salvar de las drogas’. Eso también puede suceder, sí. Pero ante todo, de lo que se trata es de restituir un derecho.”
              </p>
              <p class="little-quote georgia w600 mt-4 footer-note">Bernardo Scherman, Director de Orquesta La Pandilla. 2019.</p>

            </div>
          </div>
        </div>
        <!-- /.Middle column -->

        <!-- Last column -->
        <div class="col-12 col-lg-4 py-lg-5  text-left">
          <div class="row h-100">
            <div class="col-12 offset-xl-1 col-xl-9 bg-orquestra">
            </div>
          </div>
        </div>
        <!-- /.Last column -->

      </div>
    </div>
    <home-footer/>
  </div>
</template>

<script>
import axios from 'axios'
import homenav from '@/components/HomeNav'
import homeBanner from '@/components/homeBanner'
import homefooter from '@/components/HomeFooter'
import Tooltip from '@/components/Home/Tooltip'

export default {
  name: 'Main',
  data () {
    return {
      configuration: {},
      loading: true,
      nav_to_login: true
    }
  },
  components: {
    'homenav': homenav,
    'home-banner': homeBanner,
    'home-footer': homefooter,
    'tooltip': Tooltip
  },
  methods: {
    fetchData () {
      const path = '/api/configuration'
      axios.get(path).then((res) => {
        this.loading = false
        this.configuration = res.data[0]
      }).catch((error) => {
        this.fetchData()
        console.log(error)
      })
    }
  },
  created () {
    this.fetchData()
  }
}
</script>

<style scoped>
.arial {
  font-family: Arial,Helvetica Neue,Helvetica,sans-serif;
}
.georgia {
  font-family: Georgia,Times,Times New Roman,serif;
}
.blue-column {
  background: #0A0924;
}
.footer-note {
  font-size: 14px;
  font-style: italic;
  font-weight: 300;
}
.quote {
  font-size: 17px;
}
.little-quote {
  font-size: 11px;
}
.custom-hr {
  background: #dcdcdc !important;
  padding: 1px 0;
}
.bg-orquestra {
  background-image: url("../assets/orquestra.jpg");
  height: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
@media (min-width: 1366px) {
  .blue-column {
    transform: scaleX(1.13);
  }
  .bg-orquestra {
    min-height: 350px;
    max-height: 795px;
  }
}
@media (min-width: 992px) and (max-width: 1366px) {
  .bg-orquestra {
    min-height: 200px;
    max-height: 400px;
  }
}
@media (max-width: 992px) {
  .bg-orquestra {
    min-height: 400px;
  }
}
</style>
