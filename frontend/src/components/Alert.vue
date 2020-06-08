<template>
  <div>
    <!-- success -->
    <div v-show="message.status == 'success'" class="alert-fixed">
        <div class="card m-0 success-bottom shadow-lg">
          <div class="card-body p-3">
              <span class="black-c"><i class="fas fa-check-circle mr-3 fa-lg seed-success"></i>{{message.message}}</span>
            <button type="button" class="close text-right pl-3" @click='closeMessage'>
                <span>&times;</span>
            </button>
              <!-- <span class="ml-3 p-2 c-pointer" @click='closeMessage'></span> -->
          </div>
        </div>
    </div>
    <!-- /.success -->
    <!-- warning -->
    <div v-show="message.status == 'warning'" class="alert-fixed shadow p-0">
        <div class="alert card alert-dismissible fade show m-0 warning-bottom" role="alert">
            <strong class="black-c"><i class="fas fa-exclamation-circle mr-3 fa-lg seed-warning"></i>{{message.message}}</strong>
            <button type="button" class="close text-right" @click='closeMessage'>
                <span>&times;</span>
            </button>
        </div>
    </div>
    <!-- /.warning -->
    <!-- error -->
    <div v-show="message.status == 'error'" class="alert-fixed shadow p-0">
        <div class="alert card alert-dismissible fade show m-0 bottom-danger" role="alert">
            <strong class="black-c"><i class="fas fa-exclamation-circle mr-3 fa-lg seed-danger"></i>{{message.message}}</strong>
            <button type="button" class="close text-right" @click='closeMessage'>
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
    message: ''
  },
  watch: {
    message: function () {
      var $this = this
      setTimeout(function () {
        $this.message = false
      }, 4000)
    }
  },
  methods: {
    closeMessage () {
      this.message = ''
    }
  }
}
</script>

<style scoped>
.alert-fixed {
  position: fixed !important;
  z-index: 1080 !important;
  width: auto !important;
}
.alert-fixed, .alert-fixed * {
  transition: 0.4s all !important;
}
.alert-fixed button {
  border: 0 none;
  background: none;
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
/* .success-bottom { border-bottom: 4px solid var(--seed-success) !important; }
.warning-bottom { border-bottom: 4px solid var(--seed-warning) !important; }
.danger-bottom { border-bottom: 4px solid var(--seed-danger) !important; } */
</style>
