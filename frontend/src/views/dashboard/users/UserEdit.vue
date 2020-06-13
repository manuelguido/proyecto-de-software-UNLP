<template>
  <div>
    <dashboard>
      <!-- Title -->
      <template v-slot:page_title>
        {{pagetitle}}
      </template>
      <!-- Content -->
      <template v-slot:dashboard_content>
        <alert :message=messageData></alert>
        <!-- Form -->
        <form v-on:submit.prevent="updateUser">
          <!-- Row -->
          <div class="row mt-3">
            <!-- Backlink -->
            <div class="col-12 text-left">
              <back-link :url="returnPath" text="Usuarios"></back-link>
            </div>
            <!-- /.BackLink -->
            <!-- Información del docente -->
            <div class="col-12 col-lg-6">
              <!-- Row -->
              <div class="row justify-content-end">
                <!-- Col 12 -->
                <div class="col-12">

                  <dashboard-title title="Informacion del usuario"></dashboard-title>

                  <div class="row">
                    <!-- Nombre -->
                    <div class="col-lg-6">
                      <mdb-input label="Nombre" v-model="name" required autocomplete="off" />
                    </div>
                    <!-- Apellido -->
                    <div class="col-lg-6">
                      <mdb-input label="Apellido" v-model="lastname" required autocomplete="off" />
                    </div>

                    <!-- Username -->
                    <div class="col-lg-6">
                      <mdb-input label="Nombre de usuario" v-model="username" required autocomplete="off" />
                    </div>
                    <!-- Email -->
                    <div class="col-lg-6">
                      <mdb-input label="Email" v-model="email" required autocomplete="off" />
                    </div>

                    <!-- Activo -->
                    <div class="col-12">
                      <div class="custom-control custom-checkbox">
                          <input type="checkbox" class="custom-control-input" id="active" v-model="active">
                          <label class="custom-control-label" for="active">Activo</label>
                      </div>
                    </div>

                    <div class="col-12 mt-5">
                      <dashboard-title title="Roles del usuario"></dashboard-title>
                    </div>

                    <!-- Administrador -->
                    <div class="col-12">
                      <div class="custom-control custom-checkbox">
                          <input type="checkbox" class="custom-control-input" id="is_admin" v-model="is_admin">
                          <label class="custom-control-label" for="is_admin">Administrador</label>
                      </div>
                    </div>

                    <!-- Docente -->
                    <div class="col-12">
                      <div class="custom-control custom-checkbox">
                          <input type="checkbox" class="custom-control-input" id="is_teacher" v-model="is_teacher">
                          <label class="custom-control-label" for="is_teacher">Docente</label>
                      </div>
                    </div>

                    <!-- Preceptor -->
                    <div class="col-12">
                      <div class="custom-control custom-checkbox">
                          <input type="checkbox" class="custom-control-input" id="is_preceptor" v-model="is_preceptor">
                          <label class="custom-control-label" for="is_preceptor">Preceptor</label>
                      </div>
                    </div>

                    <!-- Errors -->
                    <div class="col-12 mt-3">
                      <p v-for="r in errors" :key="r.name" class="mb-2 seed-warning w600">
                        <i class="fas fa-exclamation-triangle seed-warning mr-2"></i>{{r.message}}
                      </p>
                    </div>

                  </div>
                </div>

                <!-- Col 12 -->
                <div class="col-12 col-lg-5 mt-4">
                  <button type="submit" class="btn seed-btn-a btn-block waves-effect mx-0">Guardar</button>
                </div>
                <!-- /.Col 12 -->

              </div>
              <!-- /.Row -->
            </div>
            <!-- /.Información del docente -->
          </div>
          <!-- /.Row -->
        </form>
        <!-- /.Form -->
      </template>
    </dashboard>
  </div>
</template>

<script>
import axios from 'axios'
import { mdbInput } from 'mdbvue'
import Dashboard from '@/views/Dashboard'
import dashboardTitle from '@/components/dashboard/Title'
import backLink from '@/components/dashboard/buttons/BackLink'
import alert from '@/components/Alert'

export default {
  props: {
    user_id: Number
  },
  data () {
    return {
      pagetitle: 'Editar usuario',
      returnPath: '/users',
      user: '',
      messageData: false,
      errors: false,
      // User form information
      name: '',
      lastname: '',
      username: '',
      email: '',
      active: true,
      is_admin: false,
      is_teacher: false,
      is_preceptor: false
    }
  },
  created () {
    this.fetchUser()
  },
  components: {
    mdbInput,
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'back-link': backLink,
    'alert': alert
  },
  methods: {
    fetchUser () {
      const path = '/api/user/' + this.user_id
      axios.get(path).then((res) => {
        this.user_id = res.data.user_id
        this.name = res.data.name
        this.lastname = res.data.lastname
        this.username = res.data.username
        this.email = res.data.email
        this.active = res.data.active
        this.is_admin = res.data.is_admin
        this.is_teacher = res.data.is_teacher
        this.is_preceptor = res.data.is_preceptor
      }).catch((error) => {
        this.fetchUser()
        console.log(error)
      })
    },
    updateUser () {
      this.messageData = ''
      const path = '/api/user/update'
      axios.post(path, {
        user_id: this.user_id,
        name: this.name,
        lastname: this.lastname,
        username: this.username,
        email: this.email,
        active: this.active,
        is_admin: this.is_admin,
        is_teacher: this.is_teacher,
        is_preceptor: this.is_preceptor
      }).then((res) => {
        if (res.data.status === 'success') {
          this.messageData = res.data
          var $this = this
          setTimeout(function () {
            $this.messageData = false
          }, 4000)
        } else {
          this.errors = res.data
        }
      }).catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>
