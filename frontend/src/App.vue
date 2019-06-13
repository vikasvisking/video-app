
<template>
	<div class="container">
		<nav  class= "navbar navbar-expand-sm bg-dark navbar-dark">
			<ul class="navbar-nav">
				<li class="nav-item">
					<router-link to="/" class="nav-link">Home</router-link>
				</li>
				<li class="nav-item">
					<router-link to="/video" class="nav-link">Video</router-link>
				</li>
				<li>
					<router-link to="/create" class="nav-link">Add A new video</router-link>
				</li>
				
			</ul>
		</nav>
		<br />
		<transition name="fade">
			<router-view></router-view>
		</transition>
	</div>
  <!-- <v-app>
   <router-view/>
  </v-app> -->
  <!-- <div>
  	 <router-view></router-view>
  	</div> -->
</template>
<style>
    .fade-enter-active, .fade-leave-active {
      transition: opacity .5s
    }
    .fade-enter, .fade-leave-active {
      opacity: 0
    }
</style>

<!-- <script>
export default {
  name: 'App'
}
</script> -->

<script>
export default {
  name: 'app',

}
</script>