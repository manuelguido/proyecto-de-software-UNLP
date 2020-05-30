<template>
  <div class="login-container aqua-gradient color-block-5">
    <div class="inner-login-container">
      <homenav :to_login="nav_to_login"></homenav>
      <div class="container">
        <div class="row justify-content-center pt-5">
          <div class="col-12 col-lg-5 pt-lg-5">
            <div class="card mt-lg-4">
              <div class="card-body p-lg-5 text-center">
                <h1 class="h4 mb-4 mb-lg-5">Iniciar sesión</h1>
                <!-- Form -->
                <form v-on:submit.prevent="login">
                  <!-- Message -->
                  <div class="form-group">
                    <P class="text-warning">{{message}}</p>
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
      message: '',
      nav_to_login: false
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
        console.log(respuesta.data.status)
        this.message = respuesta.data.message
        if (respuesta.data.success) {
          window.location.href = '/dashboard'
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
  /* background-co  lor: rgba(255,255,255,0.6); */
}
</style>
