<template>
<div class="home-container aqua-gradient color-block-5">
  <div class="inner-home-container">
    <homenav :to_login="nav_to_login"></homenav>
    <!-- Container -->
    <div class="container-fluid">
      <div class="row justify-content-center py-5 my-lg-5">
        <div class="col-12 col-md-9 col-lg-7 py-md-5">
          <!-- Card -->
          <div class="card home-card py-4 animated fadeIn">
            <div class="card-body p-5">
              <!-- Row -->
              <div class="row">
                <div class="col-12 col-md-4 py-0 text-center">
                  <img id="home-logo" class="uns animated fadeIn" src="../assets/logo.png" />
                </div>
                <div class="col-12 py-0 col-md-8">
                  <div v-if="loading">
                    <div class="spinner-border color-c mt-5" role="status">
                      <span class="sr-only">Loading...</span>
                    </div>
                  </div>
                  <div v-else-if="configuration.active">
                    <h1 class="h3 w600 mb-5">{{ configuration.title }}</h1>
                    <p class="w400 ls02 black-b mt-3 mb-5">{{ configuration.description }}</p>
                    <span class="h6 w400 mx-0 py-2 px-4 color-a bg-color-d seed-rounded shadow">
                      <i class="fas fa-envelope color-a mr-3"></i>{{ configuration.email }}
                    </span>
                  </div>
                  <div v-else>
                    <p class="h5">El sitio se encuentra en mantenimiento</p>
                  </div>
                </div>
              </div>
              <!-- /.Row -->
            </div>
          </div>
          <!-- /.Card -->
        </div>
      </div>
    </div>
    <!-- /.Container -->
  </div>
</div>
</template>

<script>
import axios from 'axios'
import homenav from '@/components/HomeNav'

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
    'homenav': homenav
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
.home-container {
  min-height: 100vh;
}
.inner-home-container {
  min-height: 100vh;
}
.home-card {
  border-radius: 25px;
  background-color: var(--white-a);
  box-shadow:
    18px 18px 25px 0 rgba(0, 0, 0, 0.18),
    -8px -8px 12px 0 rgba(239, 238, 238, 0.3) !important;
}
#home-logo {
  display: inline-block;
  margin: 0 auto !important;
  width: 75%;
}
</style>
