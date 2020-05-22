<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  mounted () {
    let recaptchaScript = document.createElement('style')
    recaptchaScript.setAttribute('rel', 'stylesheet')
    recaptchaScript.setAttribute('href', 'https://unpkg.com/leaflet@1.6.0/dist/leaflet.css')
    recaptchaScript.setAttribute('integrity', 'sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ==')
    recaptchaScript.setAttribute('crossorigin', '')
    document.head.appendChild(recaptchaScript)

    recaptchaScript = document.createElement('script')
    recaptchaScript.setAttribute('src', 'https://unpkg.com/leaflet@1.6.0/dist/leaflet.js')
    recaptchaScript.setAttribute('integrity', 'sha512-gZwIG9x3wUXg2hdXF6+rVkLF/0Vi9U8D2Ntg4Ga5I5BZpVkVxlJWbSQtXPSiUTtC0TjtGOmxa1AJPuV0CPthew==')
    recaptchaScript.setAttribute('crossorigin', '')
    document.head.appendChild(recaptchaScript)
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;600;700&display=swap');
@import './assets/css/lightseed.css';

#app {
    font-family: 'Nunito', sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: left;
    color: #41444b;
    margin: 0;
    padding: 0;
}

</style>
