<template>
  <div class="home-banner my-0 py-0">
    <div class="bg">
      <div class="container-fluid pt-5">
        <div class="row pt-5 mt-3">
          <div class="col-12 text-center pt-3 pt-lg-5 mt-4 mt-lg-5">
            <h1 id="title" class="white-a w600 animated fadeIn">{{title}}</h1>
            <h2 id="hashtag" class="white-a ls03 animated fadeIn">#LaOrquestaSomosTodos</h2>
          </div>
          <div class="col-12 text-center pt-3 pt-xl-5">
            <router-link to="/login" class="btn btn-outline-warning mr-lg-4">Iniciar sesión</router-link>
            <router-link to="/login" class="btn btn-warning ml-lg-4">Contacto</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Banner',
  props: ['title']
}
</script>

<style scoped>
  .bg {
    /* The image used */
    background-image: url("../assets/home-wallpaper2.png");
    /* Center and scale the image nicely */
    background-position: center;
    background-repeat: no-repeat;
    background-size: 100vw;
  }

  .home-banner .btn-warning,
  .home-banner .btn-outline-warning {
    font-weight: 600;
    letter-spacing: 0.05em;
  }
  .home-banner .btn-outline-warning {
    border-color: #E6FF00 !important;
    color: #E6FF00 !important;
    background: rgba(0,0,0,.4) !important;
  }
  .home-banner .btn-outline-warning:hover,
  .home-banner .btn-warning {
    background-color: #E6FF00 !important;
    color: #1D252D !important;
  }

  @media (min-width: 1200px) {
    .bg {
      height: 60vh;
      background-size: 100vw !important;
    }
    .home-banner #title{
      font-size: 3.5em;
      margin-bottom: .2em;
    }
    .home-banner #hashtag{
      font-size: 2.8em;
    }
  }
  @media (min-width: 992px) and (max-width: 1200px) {
    .bg {
      height: 52vh;
      background-size: 100vw !important;
    }
    .home-banner #title{
      font-size: 3.5em;
      margin-bottom: .2em;
    }
    .home-banner #hashtag{
      font-size: 2.8em;
    }
  }
  @media (max-width: 992px) and (min-width: 400px){
    .bg {
      height: 40vh;
      background-size: 100vw;
    }
    .home-banner #title{
      font-size: 1.2em;
      margin-bottom: .3em;
    }
    .home-banner #hashtag{
      font-size: .8em;
    }
  }
  @media (max-width: 400px) {
    .bg {
      height: 65vh;
      background-size: 320vw;
    }
    .home-banner #title{
      font-size: 1.2em;
      margin-bottom: .3em;
    }
    .home-banner #hashtag{
      font-size: .8em;
    }
  }
</style>
