<template>
  <div class="login-container aqua-gradient color-block-5">
    <div class="inner-login-container">
      <homenav :to_login="false"></homenav>
      <div class="container">
        <div class="row justify-content-center pt-5">
          <div class="col-12 col-lg-5 pt-lg-5">
            <div class="card mt-lg-4">
              <div class="card-body p-lg-5 text-center">
                <h1 class="h4 mb-4">Iniciar sesión</h1>
                <!-- Form -->
                <form v-on:submit.prevent="login">

                  <!-- Loading Spinner -->
                  <div v-if="success_login" class="d-flex justify-content-center mb-4">
                    <div class="spinner-border color-b" role="status">
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
                      <input type="email" v-model="email" name="email" class="form-control py-0" id="email" placeholder="Ingrese su email" required>
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
                      <input type="password" v-model="password" name="password" id="password" class="form-control py-0"  placeholder="Ingrese su contraseña" required>
                    </div>
                  </div>
                  <!-- /.Password -->

                  <button type="submit" class="btn btn-primary btn-block waves-effect">Entrar</button>

                </form>
                <!-- /.Form -->
                <div class="row my-4">
                    <div class="col-12"><hr></div>
                    <div class="col-12 w400 black-c">También podés</div>
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
      success_login: false,
      status_message: '',
      message_class: 'text-warning'
    }
  },
  components: {
    'homenav': homenav
  },
  methods: {
    login () {
      this.message = ''
      const path = '/auth/authenticate'
      axios.post(path, {
        email: this.email,
        password: this.password
      }).then((respuesta) => {
        this.status_message = ''
        if (respuesta.data.success) {
          this.success_login = true
          setTimeout(function () {
            window.location.href = '/dashboard'
          }, 350)
        } else {
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
