<template>
  <div>
    <h2>Weather App</h2>
    
    <!-- Input Field for Location -->
    <div>
      <label for="locationInput">Enter Location:</label>
      <input
        type="text"
        id="locationInput"
        v-model="location"
      />
      <button @click="fetchWeatherData">Get Weather</button>
    </div>
    
    <!-- Display Weather Information -->
    <div v-if="weatherData">
      <h3>Weather Information for {{ location }}</h3>
      <p>Temperature: {{ weatherData.temperature }}°C</p>
      <p>Condition: {{ weatherData.condition }}</p>
      <p>Humidity: {{ weatherData.humidity }}%</p>
      <p>Wind Speed: {{ weatherData.windSpeed }} km/h</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'WeatherComponent',
  data() {
    return {
      location: '', // Input field value for location
      weatherData: null, // Weather data retrieved from API
    };
  },
  methods: {
    async fetchWeatherData() {
      // Simulated weather data (replace with actual API call)
      try {
        const apiKey = '38932e14f595bf93a6755538e5f21218';
        const location = this.location; // Get the location from your data property

        // Make the API request to OpenWeatherMap
        const response = await axios.get(
        `https://api.openweathermap.org/data/2.5/weather?q=${location}&units=metric&appid=${apiKey}`
      );
      
      // Extract relevant weather data from the API responseconst
        const weatherData = {
          temperature: response.data.main.temp,
          condition: response.data.weather[0].description,
          humidity: response.data.main.humidity,
          windSpeed: response.data.wind.speed,
        };

      // Update your data property to store the weather data
        this.weatherData = weatherData;

        // Check if the response contains data
        if (response.data.length > 0) {
          // Add a timestamp to each weather data entry
          const formattedData = response.data.map(data => ({
            ...data,
            timestamp: new Date().toISOString(),
          }));

          //Make a POST request to send the data to your Django backend 
          await axios.post('http://localhost:8000/api/weather-data/', formattedData); // Adjust the URL to your API endpoint

          // Handle a successful POST request 
          console.log('Weather data sent to the backend.');
        }}
      catch (error) {
        console.error('Error fetching weather data:', error);
      }
    },
  },
};
    
</script>

<style scoped>
/* Add component-specific styles here */
</style>

