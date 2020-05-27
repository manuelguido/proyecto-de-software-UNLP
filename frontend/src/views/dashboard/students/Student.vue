<template>
  <div>
    <dashboard>
      <!-- Title -->
      <template v-slot:page_title>
        {{pagetitle}}
      </template>
      <!-- Content -->
      <template v-slot:dashboard_content>
        <div class="row">
          <div class="col-12 col-lg-5">
            <h1 class="h3">{{student.name}} {{student.lastname}}</h1>
            <level-button :level="student.level"></level-button>
            <p class="w600 my-2">Género: {{student.gender}}</p>
            <p class="my-2">Fecha de nacimiento: {{student.birth_date | formatDateFull}}</p>
            <p class="my-2">{{student.neighborhood}}</p>
            <p class="my-2"></p>
            <p class="my-2"></p>
          </div>
        </div>
      </template>
    </dashboard>
  </div>
</template>

<script>
import axios from 'axios'
import Dashboard from '@/views/Dashboard'
import dashboardTitle from '@/components/dashboard/Title'
import levelButton from '@/components/dashboard/buttons/LevelButton'

export default {
  data () {
    return {
      pagetitle: 'Información de estudiante',
      // editpath: '/dashboard/student/',
      // deletepath: '/dashboard/student/',
      student: ''
    }
  },
  created () {
    this.fetchData()
  },
  props: {
    student_id: Number
  },
  components: {
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'level-button': levelButton
  },
  methods: {
    fetchData () {
      const path = '/api/student/' + this.student_id
      axios.get(path).then((respuesta) => {
        this.student = respuesta.data
        console.log(path)
      }).catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>
