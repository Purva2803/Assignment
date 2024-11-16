<script setup lang="ts">
import MovieDetails from './components/MovieDetails.vue'
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
import './assets/theme.css'
</script>

<template>
  <Navbar />
  <MovieDetails />
  <Footer />
</template>

<style>
body {
  margin: 0;
  padding: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell,
    'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
}

#app {
  width: 100%;
  min-height: 100vh;
}
</style>
