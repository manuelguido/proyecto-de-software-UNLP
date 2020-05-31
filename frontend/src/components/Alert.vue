<template>
  <div>
    <!-- success -->
    <div v-if="alert.status == 'success'" class="alert-fixed shadow p-0">
        <div class="alert card alert-dismissible fade show m-0 success-bottom" role="alert">
            <strong class="black-c"><i class="fas fa-check-circle mr-3 fa-lg seed-success"></i>{{alert.message}}</strong>
            <button type="button" class="close text-right" @click='closeAlert'>
                <span>&times;</span>
            </button>
        </div>
    </div>
    <!-- /.success -->
    <!-- warning -->
    <div v-if="alert.status == 'warning'" class="alert-fixed shadow p-0">
        <div class="alert card alert-dismissible fade show m-0 warning-bottom" role="alert">
            <strong class="black-c"><i class="fas fa-exclamation-circle mr-3 fa-lg seed-warning"></i>{{alert.message}}</strong>
            <button type="button" class="close text-right" @click='closeAlert'>
                <span>&times;</span>
            </button>
        </div>
    </div>
    <!-- /.warning -->
    <!-- error -->
    <div v-if="alert.status == 'error'" class="alert-fixed shadow p-0">
        <div class="alert card alert-dismissible fade show m-0 bottom-danger" role="alert">
            <strong class="black-c"><i class="fas fa-exclamation-circle mr-3 fa-lg seed-danger"></i>{{alert.message}}</strong>
            <button type="button" class="close text-right" @click='closeAlert'>
                <span>&times;</span>
            </button>
        </div>
    </div>
    <!-- /.error -->
  </div>
</template>

<script>
export default {
  props: {
    alert: ''
  },
  methods: {
    closeAlert () {
      this.alert = ''
    }
  }
}
</script>

<style scoped>
.alert-fixed {
  position: fixed !important;
  z-index: 1080 !important;
}
@media(min-width: 992px) {
  .alert-fixed {
    top: 10vh !important;
    right: 1vw !important;
  }
}
@media(max-width: 991.98px) {
  .alert-fixed {
    bottom: 6vh !important;
    right: 3vw !important;
    left: 3vw !important;
  }
}
</style>
