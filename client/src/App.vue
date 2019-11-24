<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <NoAuthHeader/>
  </div>
</template>

<script>
import NoAuthHeader from './components/NoAuthHeader.vue'

export default {
  name: 'app',
  components: {
    NoAuthHeader
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
