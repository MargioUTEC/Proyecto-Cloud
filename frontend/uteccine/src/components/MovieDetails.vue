<template>
    <div class="movie-details">
      <div class="description">
        <h2>{{ movie.title }}</h2>
        <p>{{ movie.description }}</p>
        <button @click="closeDescription">X</button>
      </div>
      <div class="poster">
        <img :src="movie.poster" :alt="movie.title" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        movie: {
          title: "Película",
          description: "Descripción de la película",
          poster: "./src/assets/40226.jpg"
        }
      };
    },
    methods: {
      closeDescription() {
        this.$router.push({ name: 'HomeSection' });
      }
    }
  };
  </script>
  
  <style>
  /* Estilos para el componente MovieDetails.vue */
  .movie-details {
    display: flex;
    justify-content: center;
  }
  
  .description {
    flex: 1;
    padding: 20px;
  }
  
  .poster {
    flex: 1;
    padding: 20px;
  }
  
  button {
    background-color: red;
    color: white;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
  }
  </style>
  