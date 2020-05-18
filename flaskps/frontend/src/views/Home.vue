<template>
  <div>
    <p>{{ mensaje }}</p>
	<component-a></component-a>
  </div>
</template>

<script>
import axios from 'axios'
import Card from '@/components/Card.vue'

export default {
	name: 'Main',
	data () {
		return {
		mensaje: 'Sin mensaje!'
		}
	},
	components: {
		'component-a': Card 
	},
	methods: {
		getMensaje () {
		const path = 'http://localhost:5000/api/v1.0/mensaje'
		axios.get(path).then((respuesta) => {
			this.mensaje = respuesta.data
		})
		.catch((error) => {
			console.log(error)
		})
		}
	},
	created () {
		this.getMensaje()
	}
}
</script>
