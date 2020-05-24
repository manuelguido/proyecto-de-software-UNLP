<template>
  <div style="height: 500px; width: 100%">
    <l-map
      :zoom="zoom"
      :center="center"
      :options="mapOptions"
      style="height: 100%"
      @update:center="centerUpdate"
      @update:zoom="zoomUpdate"
    >
      <l-tile-layer
        :url="url"
        :attribution="attribution"
      />
      <l-marker v-for="place in places" :key="place.id" :lat-lng="coord(place)">
        <l-popup>
          <div class="marker-popup">
            <h3 class="w400 mb-2">{{place.nombre}}</h3>
            <p class="w300 my-0"><i class="fas fa-phone-alt seed-primary mr-2"></i>{{place.telefono}}</p>
            <p class="w300 my-0"><i class="fas fa-map-marker-alt seed-primary mr-2"></i>{{place.direccion}}</p>
          </div>
        </l-popup>
      </l-marker>
    </l-map>
  </div>
</template>

<script>
import { latLng, Icon } from 'leaflet'
import { LMap, LTileLayer, LMarker, LPopup, LTooltip } from 'vue2-leaflet'

delete Icon.Default.prototype._getIconUrl
Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png')
})

export default {
  name: 'Map',
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
    LTooltip
  },
  props: {
    places: null
  },
  data () {
    return {
      zoom: 12,
      center: latLng(-34.9060, -57.89),
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      currentZoom: 12,
      currentCenter: latLng(-34.9060, -57.89),
      showParagraph: false,
      mapOptions: {
        zoomSnap: 0.5
      }
    }
  },
  methods: {
    zoomUpdate (zoom) {
      this.currentZoom = zoom
    },
    centerUpdate (center) {
      this.currentCenter = center
    },
    showLongText () {
      this.showParagraph = !this.showParagraph
    },
    coord (place) {
      return latLng(place.latitude, place.longitude)
    }
  }
}
</script>

<style scoped>
.marker-popup {
  font-family: 'Nunito', sans-serif;
}
.marker-popup h3 {
  font-size: 17px !important;
}
</style>
