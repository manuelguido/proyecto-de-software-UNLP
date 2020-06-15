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
          <!-- Backlink -->
          <div class="col-12 col-lg-3 text-left">
            <back-link :url="returnPath" text="Usuarios"></back-link>
          </div>
          <!-- /.BackLink -->
          <div class="col-12 col-lg-4 text-right pt-3">
            <router-link v-if="usuario_update" :to="editPath" title="Editar"><i class="far fa-edit click-icon"></i></router-link>
            <!-- Form -->
            <form v-if="usuario_destroy" v-on:submit.prevent="deleteUser" class="display-inline">
              <input class="display-none" v-model="user_id">
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
                    <h1 class="h5 w600 black-c">{{user.name}} {{user.lastname}}</h1>
                  </div>
                  <div class="col-12 col-xl-4 text-xl-right">
                    <p v-if="user.active" class="btn btn-outline-success btn-sm seed-rounded">Activo</p>
                    <p v-else class="btn btn-outline-warning btn-sm seed-rounded">Inactivo</p>
                  </div>
                  <div class="col-12">
                    <p class="my-2">Nombre de usuario: {{user.username}}</p>
                    <p class="my-2">Email: {{user.email}}</p>
                  </div>
                  <div v-if="user.is_admin || user.is_teacher || user.is_preceptor" class="col-12 mt-2">
                    <p class="my-2 w600">Roles</p>
                    <p class="my-2 seed-primary" v-if="user.is_admin">Administrador</p>
                    <p class="my-2 seed-primary" v-if="user.is_teacher">Docente</p>
                    <p class="my-2 seed-primary" v-if="user.is_preceptor">Preceptor</p>
                  </div>
                  <div v-else class="col-12 mt-2">
                    <p class="my-2 black-c italic">El usuario no tiene roles</p>
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
import backLink from '@/components/dashboard/buttons/BackLink'
import alert from '@/components/Alert'

export default {
  data () {
    return {
      pagetitle: 'Información del usuario',
      returnPath: '/users',
      editPath: '/user/edit/' + this.user_id,
      user: '',
      confirmDeleteMsg: '¿Estás seguro de eliminar al usuario? Esta accion no se puede deshacer',
      messageData: {},
      usuario_update: false,
      usuario_destroy: false
    }
  },
  mounted () {
    this.fetchUpdate()
    this.fetchDestroy()
    this.fetchData()
  },
  props: {
    user_id: Number
  },
  components: {
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'back-link': backLink,
    'alert': alert
  },
  methods: {
    fetchData () {
      const path = '/api/user/' + this.user_id
      axios.get(path).then((res) => {
        this.user = res.data
      }).catch((error) => {
        console.log(error)
        this.fetchData()
      })
    },
    fetchUpdate () {
      axios.get('/api/user/permission/usuario_update').then((res) => {
        this.usuario_update = res.data
      }).catch((error) => {
        console.log(error)
        this.fetchUpdate()
      })
    },
    fetchDestroy () {
      axios.get('/api/user/permission/usuario_destroy').then((res) => {
        this.usuario_destroy = res.data
      }).catch((error) => {
        console.log(error)
        this.fetchDestroy()
      })
    },
    deleteUser () {
      if (confirm(this.confirmDeleteMsg)) {
        const path = '/api/user/delete'
        axios.post(path, {
          user_id: this.user_id
        }).then((res) => {
          this.messageData = res.data
          if (res.data.status === 'success') {
            setTimeout(function () {
              window.location.href = '/users'
            }, 800)
          }
        }).catch((error) => {
          console.log(error)
        })
      }
    }
  }
}
</script>
