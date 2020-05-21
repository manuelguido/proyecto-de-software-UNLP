<template>
  <div><p>Saliendo del sistema...</p></div>
</template>

<script>
export default {
  methods: {
    returning () {
      window.location.href = '/'
    }
  },
  created () {
    this.returning()
  }
}
</script>
