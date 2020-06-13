<template>
      <mdb-datatable
        class="my-3 black-b"
        :data="my_data"
        responsive
        arrows
        defaultRow="No hay información"
        noFoundMessage="No hay resultados"
        searchPlaceholder="Buscar"
        :tfoot="false"
        showingText="Mostrando"
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

<style scoped>
thead th {
  color: var(--black-b);
  font-weight: 600 !important;
}
.pagination .page-item, .pagination .active, .pagination .page-item.active  {
  background-color: var(--color-b) !important;
}
.page-item.active {
  background-color: var(--color-b) !important;
}
</style>
