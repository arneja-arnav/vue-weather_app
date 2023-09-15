<template>
  <HomeDecorator />
  <img alt="Weather logo" src="./assets/weather-news.png">
  <WeatherComponent />
</template>

<script>
import WeatherComponent from "./components/weather_home.vue"
import HomeDecorator from "./components/homePage.vue"

export default {
  name: 'App',
  components: {
    HomeDecorator,
    WeatherComponent,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
