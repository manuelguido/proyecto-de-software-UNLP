<template>
  <div class="login-container aqua-gradient color-block-5">
    <div class="container">
      <div class="row justify-content-center pt-5">
        <div class="col-12 col-xl-5 pt-xl-5">
          <div class="card">
            <div class="card-body p-xl-5 text-center">
              <h1 class="h4 my-4 mb-xl-5">Iniciar sesión</h1>
              <!-- Form -->
              <form v-on:submit.prevent="login">
                <!-- Email -->
                <div class="form-group">
                  <P class="text-warning">{{message}}</p>
                </div>
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
                <button type="submit" class="btn btn-primary btn-block">Entrar</button>
              </form>
              <!-- /.Form -->
            </div>
          </div>
        </div>
        <div class="col-12 py-4">
          <a href="/" class="btn btn-blue-grey my-5"><i class="fas fa-arrow-left mr-3 white1"></i>Volver al inicio</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      email: '',
      password: '',
      message: ''
    }
  },
  methods: {
    login () {
      this.message = ''
      const path = '/auth_authenticate'
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
</style>
