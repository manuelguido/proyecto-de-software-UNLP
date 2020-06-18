<template>
  <div class="login-container aqua-gradient color-block-5">
    <div class="inner-login-container">
      <homenav :to_login="false"></homenav>
      <div class="container">
        <div class="row justify-content-center pt-5">
          <div class="col-12 col-lg-5 pt-4 pt-lg-5">
            <div class="card mt-lg-4">
              <div class="card-body p-5 text-center">
                <h1 class="h4 mb-4">Iniciar sesión</h1>
                <!-- Form -->
                <form v-on:submit.prevent="login">

                  <!-- Loading Spinner -->
                  <div v-if="loading" class="d-flex justify-content-center mb-4">
                    <div class="spinner-border color-c" role="status">
                      <span class="sr-only">Loading...</span>
                    </div>
                  </div>
                  <!-- /.Loading Spinner -->

                  <!-- Message -->
                  <div v-if="status_message" class="form-group">
                    <p class="h6" :class="message_class">{{status_message}}</p>
                  </div>
                  <!-- /.Message -->

                  <!-- Email -->
                  <div class="form-group">
                    <label class="sr-only" for="email">Ingrese su email</label>
                    <div class="input-group mb-4">
                      <div class="input-group-prepend bg-none">
                        <div class="input-group-text btn-light">
                          <i class="fas fa-envelope white-text"></i>
                        </div>
                      </div>
                      <input type="text" v-model="email" name="email" class="form-control py-0" id="email" placeholder="Email o nombre de usuario" required>
                    </div>
                  </div>
                  <!-- /.Email -->

                  <!-- Password -->
                  <div class="form-group">
                    <label class="sr-only" for="password">Ingrese su contraseña</label>
                    <div class="input-group mb-4">
                      <div class="input-group-prepend bg-none">
                        <div class="input-group-text btn-light">
                          <i class="fas fa-lock white-text"></i>
                        </div>
                      </div>
                      <input type="password" v-model="password" name="password" id="password" class="form-control py-0"  placeholder="Contraseña" required>
                    </div>
                  </div>
                  <!-- /.Password -->

                  <button type="submit" class="btn btn-primary btn-block waves-effect">Entrar</button>

                </form>
                <!-- /.Form -->
                <div class="row my-4">
                    <div class="col-12"><hr></div>
                    <div class="col-12 w400 black-c">También puedes</div>
                </div>

                <a href="/google_login" class="btn btn-danger btn-block waves-effect w600"><i class="fab fa-google mr-3"></i>Iniciar con google</a>

              </div>
              <!-- /.Card Body -->
            </div>
          </div>
          <div class="col-12 py-5 text-center">
            <router-link to="/" class="btn btn-indigo waves-effect my-lg-4"><i class="fas fa-arrow-left mr-3 white-a"></i>Volver al inicio</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import homenav from '@/components/HomeNav'

export default {
  data () {
    return {
      email: '',
      password: '',
      loading: false,
      status_message: '',
      message_class: 'text-warning'
    }
  },
  components: {
    'homenav': homenav
  },
  methods: {
    login () {
      this.loading = true
      this.status_message = ''
      const path = '/auth/authenticate'
      axios.post(path, {
        email: this.email,
        password: this.password
      }).then((respuesta) => {
        if (respuesta.data.success) {
          window.location.href = '/dashboard'
        } else {
          this.loading = false
          this.status_message = respuesta.data.message
        }
      }).catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>
.login-container {
  min-height: 100vh;
}
.inner-login-container {
  min-height:  100vh;
  background-color: rgba(255,255,255,0.2);
}
</style>
