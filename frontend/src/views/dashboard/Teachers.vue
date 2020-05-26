<template>
<div>
  <dashboard>
    <div class="row">
      <div class="col-12 col-xl-6">
        <dashboard-title title="Núcleos"></dashboard-title>
        <dashboard-table
          :columnas=columns
          :filas=rows
        ></dashboard-table>
      </div>
      <div class="col-12 col-xl-6">
        <dashboard-title title="Ubicación"></dashboard-title>
        <v-map :places="teachers"></v-map>
      </div>
    </div>
  </dashboard>
</div>
</template>

<script>
import axios from 'axios'
import Dashboard from '@/views/Dashboard'
import dashboardTitle from '@/components/dashboard/Title'
import dashboardTable from '@/components/dashboard/Table'
import vMap from '@/components/dashboard/Map'

export default {
  data () {
    return {
      teachers: '',
      teacher_path: '/dashboard/teacher/',
      columns: [
        {
          label: 'Nucleo',
          field: 'nombre',
          sort: 'asc'
        },
        {
          label: 'Dirección',
          field: 'direccion',
          sort: 'asc'
        },
        {
          label: 'Teléfono',
          field: 'telefono',
          sort: 'asc'
        }
      ],
      rows: []
    }
  },
  components: {
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'v-map': vMap,
    'dashboard-table': dashboardTable
  },
  methods: {
    getNucleos () {
      const path = '/api/teachers'
      axios.get(path).then((respuesta) => {
        this.teachers = respuesta.data
        this.loadTeachers()
      })
        .catch((error) => {
          console.log(error)
        })
    },
    loadTeachers () {
      let newrow = {}
      for (let i = 0; i < this.teachers.length; i++) {
        newrow = {nombre: this.teachers[i].nombre, direccion: this.teachers[i].direccion, telefono: this.teachers[i].telefono}
        this.rows.push(newrow)
      }
    }
  },
  created () {
    this.getNucleos()
  }
}
</script>
