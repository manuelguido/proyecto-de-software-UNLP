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
        <!-- Edition row -->
        <div class="row">
          <div class="col-12 col-lg-3 text-left">
            <back-link :url="returnPath" text="Talleres"></back-link>
          </div>
          <div class="col-12 col-lg-4 text-right pt-3">
            <router-link v-if="administrativo_update" :to="editPath" title="Editar"><i class="far fa-edit click-icon"></i></router-link>
            <!-- Form -->
            <form v-if="administrativo_destroy" v-on:submit.prevent="deleteWorkshop" class="display-inline">
              <input class="display-none" v-model="workshop_id">
              <button type="submit" class="bg-none b-0" title="Eliminar"><i class="fas fa-trash click-icon"></i></button>
            </form>
          </div>
        </div>
        <!-- /.Edition row -->

        <!-- Information row -->
        <div class="row mt-3">
          <div class="col-12 col-lg-7">
            <div class="card seed-shadow seed-s-rounded">
              <div class="card-body">
                <div class="row">
                  <div class="col-12 col-xl-8">
                    <h1 class="h5 w600 black-c">{{workshop.name}}</h1>
                  </div>
                  <div class="col-12">
                    <p class="w600 my-2">{{workshop.short_name}}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- /.Information row -->
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
      pagetitle: 'Información del taller',
      returnPath: '/workshops',
      editPath: '/workshop/edit/' + this.workshop_id,
      workshop: '',
      confirmDeleteMsg: '¿Estás seguro de eliminar el taller? Esta accion no se puede deshacer',
      messageData: {},
      administrativo_update: false,
      administrativo_destroy: false
    }
  },
  mounted () {
    this.fetchUpdate()
    this.fetchDestroy()
    this.fetchData()
  },
  props: {
    workshop_id: Number
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
      const path = '/api/workshop/' + this.workshop_id
      axios.get(path).then((response) => {
        this.workshop = response.data
      }).catch((error) => {
        this.fetchData()
        console.log(error)
      })
    },
    fetchUpdate () {
      axios.get('/api/user/permission/administrativo_update').then((res) => {
        this.administrativo_update = res.data
      }).catch((error) => {
        this.fetchUpdate()
        console.log(error)
      })
    },
    fetchDestroy () {
      axios.get('/api/user/permission/administrativo_destroy').then((res) => {
        this.administrativo_destroy = res.data
      }).catch((error) => {
        this.fetchDestroy()
        console.log(error)
      })
    },
    deleteWorkshop () {
      if (confirm(this.confirmDeleteMsg)) {
        const path = '/api/workshop/delete'
        axios.post(path, {
          workshop_id: this.workshop_id
        }).then((response) => {
          this.messageData = response.data
          setTimeout(function () {
            window.location.href = '/workshops'
          }, 400)
        }).catch((error) => {
          console.log(error)
        })
      }
    }
  }
}
</script>
