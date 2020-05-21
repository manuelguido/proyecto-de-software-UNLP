<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Nunito:300,400,500,700&display=swap');

#app {
  font-family: 'Nunito', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #41444b;
  margin: 0;
  padding: 0;
}

html {
    scroll-behavior: smooth !important;
}
body {
    background: #f9f9f9;
}
.hide {
    max-width: 0 !important;
    max-height: 0 !important;
}

/* .display-n { display: none !important;}
.display-b { display: block !important;}
.overflow-h { overflow: hidden !important; }
.no-shadow { box-shadow: none !important; }
.cursor-p { cursor: pointer !important; }
.cursor-d { cursor: default !important; }
.cursor-na { cursor: not-allowed !important; }
.br-0 { border-radius: 0 !important; }
.uns {
    -webkit-touch-callout: none;
      -webkit-user-select: none;
       -khtml-user-select: none;
         -moz-user-select: none;
          -ms-user-select: none;
              user-select: none;
}
.op-hover1:hover {opacity: 0.7 !important;}
.op-hover2:hover {opacity: 0.5 !important;}
.op-hover3:hover {opacity: 0.4 !important;}
.opacity1 {opacity: 0.1 !important;}
.opacity2 {opacity: 0.2 !important;}
.opacity3 {opacity: 0.3 !important;}
.opacity4 {opacity: 0.4 !important;}
.opacity5 {opacity: 0.5 !important;}
.opacity6 {opacity: 0.6 !important;}
.opacity7 {opacity: 0.7 !important;}
.opacity8 {opacity: 0.8 !important;}
.opacity9 {opacity: 0.9 !important;}
.opacity10 {opacity: 1 !important;} */

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
    /* display: none; <- Crashes Chrome on hover */
    -webkit-appearance: none;
    margin: 0; /* <-- Apparently some margin are still there even though it's hidden */
}
input[type=number] {
    -moz-appearance:textfield; /* Firefox */
}
/* .inner-shadow-1 {
    -webkit-box-shadow: inset 0px 0px 20px 8px rgba(112,112,112,0.2);
    -moz-box-shadow: inset 0px 0px 20px 8px rgba(112,112,112,0.2);
    box-shadow: inset 0px 0px 20px 8px rgba(112,112,112,0.2);
} */

/*--------------------------------------------------------------
    Generic
--------------------------------------------------------------*/
@media(max-width: 992px){ .mobile-hide { display: none; }}
@media(min-width: 992px){ .web-hide { display: none; }}

/*--------------------------------------------------------------
    Text
--------------------------------------------------------------*/s
.w200 { font-weight: 200 !important; }
.w300 { font-weight: 300 !important; }
.w400 { font-weight: 400 !important; }
.w500 { font-weight: 500 !important; }
.w600 { font-weight: 600 !important; }
.w700 { font-weight: 700 !important; }
.w800 { font-weight: 800 !important; }
.w900 { font-weight: 900 !important; }
.italic { font-style: italic !important; }
.ls01{ letter-spacing: .01em; }
.ls02{ letter-spacing: .02em; }
.ls03{ letter-spacing: .03em; }
.ls04{ letter-spacing: .04em; }
.ls05{ letter-spacing: .05em; }
.ls06{ letter-spacing: .06em; }
.ls07{ letter-spacing: .07em; }
.ls08{ letter-spacing: .08em; }
.ls09{ letter-spacing: .09em; }

/*--------------------------------------------------------------
    Buttons
--------------------------------------------------------------*/
.btn {
    margin-left: 0 !important;
    margin-right: 0 !important;
}
/* Icon */
.btn i { color: inherit !important; }
/* Rounded */
.btn-rounded { border-radius: 50px !important; }

/*--------------------------------------------------------------
    Cards
--------------------------------------------------------------*/
/* .card-header {
    border: 0 none;
}
.card-radius-16 {
    border-radius: 16px !important;
} */

/*--------------------------------------------------------------
    Panel de docente
--------------------------------------------------------------*/
@media (min-width: 702px) {
    #panel-menu {
        min-height: 100vh;
    }
}
@media (min-width: 992px) {
    .panel-logo {
        display: block !important;
    }
}
.panel {
    background: #fff;
}
.nav-link-panel , .nav-link-nombre {
    color: #353535 !important;
    font-weight: 500;
}
.nav-link-panel {
    font-size: 1.2em;
}
.nav-link-nombre {
    font-size: .9em;
}
#panel-menu {
    z-index: 10;
    border-radius: 0;
    background: #f0f3fa;
}
.panel-banner {
    background: #f0f3fa;
}
.navbar-static-top {
    margin-bottom: 0px;
}
.panel-logo {
    margin: 25px auto;
    width: 35%;
    display: none;
}
.panel-main {
    background: #e6e6e4;
    height: 100%;
}
.panel-main .container-fluid {
    margin: 0 auto;
    padding-top: 10vh;
}

.menuItem {
    transition: 0.1s all !important;
    color: #555 !important;
    border: 0 none !important;
    width: 100% !important;
    padding: .7em 2.3em !important;
    background: none !important;
}
.menuItem a, .menuItem a i {
    color: #555;
    font-size: 1em;
}
.menuItem a:hover {
    color: #0971d9 !important;
}
.menuItem a:hover i {
    color: #0971d9 !important;
}
.menuItemActive a i, .menuItemActive a {
    color: #0971d9 !important;
}
.subItem {
    display: none;
}
.icon-rounded {
    padding: 10px;
    margin-right: 4px;
    border-radius: 50px;
}
.full-height {
    height: 100% !important;
}
.navbar-brand {
    color: #444 !important;
    cursor: default !important;
}
.btn-note-detail {
    background: #7ed4c9;
    font-weight: bold;
}
.alert-fixed {
    position: fixed;
    bottom: 9vh;
    top: auto;
    left: 3vw;;
    right: 3vw;
    z-index:9999;
}
@media (min-width: 992px) {
    .alert-fixed {
        position: fixed;
        bottom: 9vh;
        left: 30vw;
        right: 30vw;
        z-index:9999;
    }
}
.page-buttons {
    display: inline-block !important;
}
#bigmapid {
    height: 60vh;
    width: 100%;
}
#minmapid {
    height: 65vh;
    width: 100%;
}

/*--------------------------------------------------------------
    Interacción de tablas del panel de doncente
--------------------------------------------------------------*/
th, td {
    padding-bottom: 10px !important;
    padding-top: 10px !important;
}
.table-selected {
    background: rgba(44, 118, 149, 0.5) !important;
}
.table-select {
    transition: 0.08s all !important;
}
.table-select:hover {
    background: rgba(44, 118, 149, 0.6) !important;
}
.table-select:active {
    background: rgba(44, 118, 149, 0.8) !important;
}

.instrumento {
    max-height: 300px;
    max-width: 200px;
}

</style>
