<template>
  <mdb-datatable
    :data="my_data"
    striped
    bordered
    responsive
    next="Anterior"
    previous="Siguiente"
    defaultRow="No hay información"
    noFoundMessage="No hay resultados"
    searchPlaceholder="Buscar"
    :tfoot="false"
    showingText="Mostrando"
    pagination="false"
  ></mdb-datatable>
</template>

<script>
import { mdbDatatable } from 'mdbvue'
export default {
  name: 'DatatablePage',
  components: {
    mdbDatatable
  },
  props: {
    'columnas': [],
    'filas': []
  },
  data () {
    return {
      my_data: {
        columns: [],
        rows: []
      }
    }
  },
  methods: {
    loadTableData () {
      this.my_data.columns = this.columnas
      this.my_data.rows = this.filas
    }
  },
  created () {
    this.loadTableData()
  }
}
</script>
