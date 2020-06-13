<template>
      <mdb-datatable
        :data="my_data"
        class="mt-4"
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

<style>
th,
.th-sm,
th.th-sm,
th.sorting {
  color: #818699 !important;
  font-size: 16px;
  font-weight: 600 !important;
}

td div {
  color: var(--black-c);
  font-weight: 400 !important;
}

@media (min-width: 1500px) {
  .dataTables_filter input {
    min-width: 300px !important;
  }
}
@media (min-width: 992px) {
  .dataTables_filter input {
    min-width: 300px !important;
  }
}
</style>
