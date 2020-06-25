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
            <router-link v-if="usuario_new" :to="newUserPath" class="btn btn-outline-success seed-rounded mx-0"><i class="fas fa-plus mr-3"></i>Nuevo usuario</router-link>
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
      usuario_new: false,
      usuario_show: false,
      usuario_update: false,
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
          label: '',
          field: 'show'
        },
        {
          label: '',
          field: 'edit'
        }
      ],
      rows: []
    }
  },
  mounted () {
    this.fetchNew()
    this.fetchShow()
    this.fetchUpdate()
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
        this.fetchData()
        console.log(error)
      })
    },
    // Data fetch for permissions
    fetchNew () {
      axios.get('/api/user/permission/usuario_new').then((res) => {
        this.usuario_new = res.data
      }).catch((error) => {
        this.fetchNew()
        console.log(error)
      })
    },
    fetchShow () {
      axios.get('/api/user/permission/usuario_show').then((res) => {
        this.usuario_show = res.data
      }).catch((error) => {
        this.fetchShow()
        console.log(error)
      })
    },
    fetchUpdate () {
      axios.get('/api/user/permission/usuario_update').then((res) => {
        this.usuario_update = res.data
      }).catch((error) => {
        this.fetchUpdate()
        console.log(error)
      })
    },
    loadUsers () {
      let newrow = {}
      var varshow
      var varedit
      for (let i = 0; i < this.users.length; i++) {
        varshow = '<p class="display-none">-</p>'
        varedit = '<p class="display-none">-</p>'
        if (this.usuario_show) { varshow = '<a href="' + this.showUserPath + this.users[i].user_id + '" class="btn seed-btn-primary btn-sm seed-rounded"><i class="far fa-eye mr-3"></i>Ver</a>' }
        if (this.usuario_update) { varedit = '<a href="' + this.editUserPath + this.users[i].user_id + '" class="btn seed-btn-secondary btn-sm seed-rounded"><i class="fas fa-pencil-alt mr-3"></i>Editar</a>' }
        newrow = {
          lastname: this.users[i].lastname,
          name: this.users[i].name,
          username: this.users[i].username,
          show: varshow,
          edit: varedit
        }
        this.rows.push(newrow)
      }
    }
  }
}
</script>
