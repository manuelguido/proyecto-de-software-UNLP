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
        <!-- Form -->
        <form v-on:submit.prevent="createUser">
          <!-- Row -->
          <div class="row mt-3">
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

                    <div class="col-12 mt-5">
                      <dashboard-title title="Contraseña del usuario"></dashboard-title>
                    </div>

                    <!-- Nombre -->
                    <div class="col-lg-6">
                      <mdb-input type="password" label="Contraseña" v-model="password" required autocomplete="off" />
                    </div>

                    <!-- Apellido -->
                    <div class="col-lg-6">
                      <mdb-input type="password" label="Repetir contraseña" v-model="password_confirm" required autocomplete="off" />
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
                  <button type="submit" class="btn seed-btn-b btn-block waves-effect mx-0">Guardar</button>
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
import alert from '@/components/Alert'

export default {
  data () {
    return {
      pagetitle: 'Cargar un nuevo usuario',
      user: '',
      messageData: false,
      errors: false,
      // User form information
      name: '',
      lastname: '',
      username: '',
      email: '',
      active: true,
      password: '',
      password_confirm: '',
      is_admin: false,
      is_teacher: false,
      is_preceptor: false
    }
  },
  components: {
    mdbInput,
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'alert': alert
  },
  methods: {
    restoreValues () {
      this.name = ''
      this.lastname = ''
      this.username = ''
      this.email = ''
      this.active = true
      this.password = ''
      this.password_confirm = ''
      this.is_admin = false
      this.is_teacher = false
      this.is_preceptor = false
    },
    createUser () {
      this.messageData = ''
      const path = '/api/user/create'
      axios.post(path, {
        name: this.name,
        lastname: this.lastname,
        username: this.username,
        email: this.email,
        active: this.active,
        password: this.password,
        password_confirm: this.password_confirm,
        is_admin: this.is_admin,
        is_teacher: this.is_teacher,
        is_preceptor: this.is_preceptor
      }).then((res) => {
        if (res.data.status === 'success') {
          this.restoreValues()
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
