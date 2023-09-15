<template>
  <div class="home-decorator">
    <!-- Header Section -->
    <header>
      <h1 class="title">{{ title }}</h1>
    </header>
    
    <!-- Content Section -->
    <div class="content">
      <!-- Your home page content goes here -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeDecorator',
  props: {
    title: {
      type: String,
      default: 'Welcome to my little Weather Website', // Default title
    },
    imageUrl: {
      type: String,
      default: 'path-to-default-image.jpg', // Default image URL
    },
  },
};
</script>

<style scoped>
/* Add component-specific styles here */
.home-decorator {
  background-color: #f0f0f0; /* Background color for the entire decorator */
  text-align: center;
  font-family: Arial, sans-serif;
}

.title {
  color: #333; /* Title text color */
  font-size: 36px; /* Title font size */
  margin-bottom: 10px; /* Margin below the title */
}

.decorative-image {
  max-width: 100%; /* Ensure the image fits within its container */
  border: 2px solid #333; /* Add a border around the image */
  border-radius: 10px; /* Rounded corners for the image */
  margin-bottom: 20px; /* Margin below the image */
}

.content {
  /* Your styles for the content section */
}
</style>

