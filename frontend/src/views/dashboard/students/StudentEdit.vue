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
            <router-link :to="editpath" class="btn btn-info btn-sm seed-rounded ml-0"><i class="far fa-edit mr-3"></i>Editar</router-link>
            <router-link :to="deletepath" class="btn btn-danger btn-sm seed-rounded"><i class="fas fa-trash mr-3"></i>Eliminar</router-link>
          </div>
        </div>
        <div class="row mt-3">
          <div class="col-12 col-lg-5">
            <div class="card">
              <div class="card-body">
                <div class="row">
                  <div class="col-12 col-xl-8">
                    <h1 class="h5 w600 black-c">{{student.name}} {{student.lastname}}</h1>
                  </div>
                  <div class="col-12 col-xl-4 text-xl-right">
                    <level-button :level="student.level"></level-button>
                  </div>
                  <div class="col-12">
                    <p class="w600 my-2">Género: {{student.gender}}</p>
                    <p class="w600 my-2">Documento: {{student.document_type}} {{student.document_number}}</p>
                    <p class="w600 my-2">Teléfono: {{student.phone}}</p>
                    <p class="my-2">Fecha de nacimiento: {{student.birth_date | formatDateFull}}</p>
                    <p class="my-2">Barrio: {{student.neighborhood}}</p>
                    <p class="my-2">Escuela: {{student.school}}</p>
                  </div>
                </div>
              </div>
            </div>
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
      pagetitle: 'Información del estudiante',
      editpath: '/dashboard/student/' + this.student_id,
      deletepath: '/dashboard/student/' + this.student_id,
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
