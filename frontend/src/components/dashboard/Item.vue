<template>
	<div class="col-12 col-lg-6 col-xl-3 mb-3">
		<a class="py-2 card waves-effect dashboard-item w-100" v-bind:class="'bg-'+color+'-light'" v-bind:href="url">
			<!-- Card Body -->
			<div class="card-body">
				<!-- Chart with Info -->
				<div class="media align-items-center">
					<!-- Chart with Info - Info -->
					<div class="media-body">
						<h2 class="h5 w200 m-0" v-bind:class="color+'-dark'"><i v-bind:class="icon" class="icon mr-3"></i>{{label}}</h2>
					</div>
					<!-- End Chart with Info - Info -->
				</div>
				<!-- End Chart with Info -->
			</div>
			<!-- End Card Body -->
		</a>
	</div>
</template>

<style>
.dashboard-item:hover {
	text-decoration: none !important;
	opacity: 0.7;
}
</style>

<script>
export default {
    props: ['url', 'icon', 'label', 'color']
}
</script>
