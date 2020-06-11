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
        <!-- Main row -->
        <div class="row">
          <!-- Col 12 -->
          <div class="col-12 col-lg-7">
            <!-- Row -->
            <div class="row">

              <div class="col-12">
                <back-link :url="returnPath" text="Instrumentos"></back-link>
              </div>

              <div class="col-12 col-lg-9">
                <h1 class="h5 w600 black-c">{{instrument.name}}</h1>
              </div>

              <div class="col-12 col-lg-3 text-lg-right uns">
                <router-link :to="editPath" title="Editar"><i class="far fa-edit click-icon"></i></router-link>
                <!-- Form -->
                <form v-on:submit.prevent="deleteInstrument" class="display-inline">
                  <input class="display-none" value="{{instrument_id}}" v-model="instrument_id">
                  <button type="submit" class="bg-none b-0" title="Eliminar"><i class="fas fa-trash click-icon"></i></button>
                </form>
              </div>

              <div class="col-12 mb-4"><hr class="m-0 p-0"></div>

              <div class="col-12 col-lg-6">
                <p class="w600 my-2">Código: <span class="seed-primary">{{instrument.code}}</span></p>
                <p class="w400 my-2">Tipo: {{instrument.type}}</p>
              </div>
              <div class="col-12 col-lg-6">
                <img :src="image_path+instrument.image" class="w-100">
              </div>

            </div>
            <!-- /.Row -->
          </div>
          <!-- /.Col 12 -->
        </div>
        <!-- /.Main row -->
      </template>
    </dashboard>
  </div>
</template>

<script>
import axios from 'axios'
import Dashboard from '@/views/Dashboard'
import dashboardTitle from '@/components/dashboard/Title'
import levelButton from '@/components/dashboard/buttons/LevelButton'
import backLink from '@/components/dashboard/buttons/BackLink'
import alert from '@/components/Alert'

export default {
  data () {
    return {
      pagetitle: 'Información del instrumento',
      returnPath: '/instruments',
      editPath: '/instrument/edit/' + this.instrument_id,
      image_path: '/static/img/instruments/',
      instrument: '',
      confirmDeleteMsg: '¿Estás seguro de eliminar el instrumento? Esta accion no se puede deshacer',
      messageData: {}
    }
  },
  created () {
    this.fetchData()
  },
  props: {
    instrument_id: Number
  },
  components: {
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'level-button': levelButton,
    'back-link': backLink,
    'alert': alert
  },
  methods: {
    fetchData () {
      const path = '/api/instrument/' + this.instrument_id
      axios.get(path).then((res) => {
        this.instrument = res.data
      }).catch((error) => {
        console.log(error)
        this.fetchData()
      })
    },
    deleteInstrument () {
      if (confirm(this.confirmDeleteMsg)) {
        const path = '/api/instrument/delete'
        axios.post(path, {
          instrument_id: this.instrument_id
        }).then((res) => {
          this.messageData = res.data
          setTimeout(function () {
            window.location.href = '/instruments'
          }, 800)
        }).catch((error) => {
          console.log(error)
        })
      }
    }
  }
}
</script>
