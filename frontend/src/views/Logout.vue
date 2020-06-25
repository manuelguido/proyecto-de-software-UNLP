<template>
  <div class="container pt-5">
    <div class="row pt-5 mt-5">
      <div class="col-12 text-center mt-5">
        <div class="d-flex justify-content-center">
          <div class="spinner-border text-light" role="status">
            <span class="sr-only">Loading...</span>
          </div>
        </div>
      </div>
      <div class="col-12 text-center mt-3">
        <p class="black-d">Saliendo del sistema...</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    returning () {
      setTimeout(function () {
        window.location.href = '/'
      }, 130)
    }
  },
  created () {
    this.returning()
  }
}
</script>
