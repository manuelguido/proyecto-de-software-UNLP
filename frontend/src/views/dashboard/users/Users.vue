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
          <!-- /.Table Col -->
          <div class="col-12 col-md-8">
            <dashboard-title title="Listado de usuarios"></dashboard-title>
          </div>
          <div class="col-12 col-md-4 text-md-right">
            <router-link :to="newUserPath" class="btn btn-outline-success seed-rounded mx-0"><i class="fas fa-plus mr-3"></i>Nuevo usuario</router-link>
          </div>
          <div class="col-12">
            <dashboard-table
              :columnas=columns
              :filas=rows
            ></dashboard-table>
          </div>
          <!-- /.Table Col -->
        </div>
      </template>
      <!-- /.Content -->
    </dashboard>
  </div>
</template>

<script>
import axios from 'axios'
import Dashboard from '@/views/Dashboard'
import dashboardTitle from '@/components/dashboard/Title'
import dashboardTable from '@/components/dashboard/Table'

export default {
  data () {
    return {
      pagetitle: 'Usuarios',
      users: '',
      showUserPath: '/user/',
      newUserPath: '/new/user',
      editUserPath: '/user/edit/',
      columns: [
        {
          label: 'Apellido',
          field: 'lastname',
          sort: 'asc'
        },
        {
          label: 'Nombre',
          field: 'name',
          sort: 'asc'
        },
        {
          label: 'Nombre de usuario',
          field: 'username',
          sort: 'asc'
        },
        {
          label: 'Ver',
          field: 'show'
        },
        {
          label: 'Editar',
          field: 'edit'
        }
      ],
      rows: []
    }
  },
  created () {
    this.fetchData()
  },
  components: {
    'dashboard': Dashboard,
    'dashboard-title': dashboardTitle,
    'dashboard-table': dashboardTable
  },
  methods: {
    fetchData () {
      const path = '/api/users'
      axios.get(path).then((respuesta) => {
        this.users = respuesta.data
        this.loadUsers()
      }).catch((error) => {
        console.log(error)
        this.fetchData()
      })
    },
    loadUsers () {
      let newrow = {}
      for (let i = 0; i < this.users.length; i++) {
        newrow = {
          lastname: this.users[i].lastname,
          name: this.users[i].name,
          username: this.users[i].username,
          show: '<a href="' + this.showUserPath + this.users[i].user_id + '" class="btn seed-btn-primary btn-sm seed-rounded"><i class="far fa-eye mr-3"></i>Ver</a>',
          edit: '<a href="' + this.editUserPath + this.users[i].user_id + '" class="btn seed-btn-warning btn-sm seed-rounded"><i class="far fa-edit mr-3"></i>Editar</a>'
        }
        this.rows.push(newrow)
      }
    }
  }
}
</script>
