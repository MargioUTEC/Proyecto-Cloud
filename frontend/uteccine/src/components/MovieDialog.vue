<template>
  <div class="dialog-container">
    <div class="dialog-content">
      <h3>{{ movieCopy.title }}</h3>
      <p>{{ movieCopy.description }}</p>
      <p>Duration: {{ durationInHours }}</p>
      <p>Year: {{ movieCopy.year }}</p>
      <div>
    <strong>Gender:</strong>
    <ul class="options-list">
      <li v-for="genre in movieCopy.gender" :key="genre" class="option-item">{{ genre }}</li>
    </ul>
  </div>
  <div>
    <strong>Language:</strong>
    <ul class="options-list">
      <li v-for="lang in movieCopy.language" :key="lang" class="option-item">{{ lang }}</li>
    </ul>
  </div>
  <div>
    <strong>Classification:</strong>
    <ul class="options-list">
      <li v-for="classification in movieCopy.classification" :key="classification" class="option-item">
        {{ classification }}
      </li>
    </ul>
  </div>
      <button class="close-button" @click="closeDialog">
        <span class="close-icon"></span>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    movie: {
      type: Object,
      required: true
    },
    movieOptions: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      movieCopy: {}
    };
  },
  mounted() {
    this.movieCopy = Object.assign({}, this.movie);
    this.fetchMovieInfo();
  },
  computed: {
    durationInHours() {
      const minutes = this.movieCopy.duration;
      const hours = Math.floor(minutes / 60);
      const remainingMinutes = minutes % 60;
      return `${hours}h ${remainingMinutes}min`;
    }
  },
  methods: {
    closeDialog() {
      this.$emit('close');
    },
    fetchMovieInfo() {
      const movieTitle = this.movieCopy.title;
      const apiUrl = `http://proyect-1296764638.us-east-1.elb.amazonaws.com:8000/movie/${movieTitle}`;

      fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
          if (data.success) {
            const movieInfo = data.movie_info;
            this.movieCopy.description = movieInfo.description;
            this.movieCopy.duration = movieInfo.duration;
            this.movieCopy.year = movieInfo.year;
            this.movieCopy.name = movieInfo.name;
            this.movieCopy.gender = movieInfo.gender;
            this.movieCopy.language = movieInfo.language;
            this.movieCopy.classification = movieInfo.classification;
          } else {
            console.error('La API no pudo obtener la información de la película');
          }
        })
        .catch(error => {
          console.error('Error al obtener la información de la película:', error);
        });
    }
  }
};
</script>

<style scoped>
/* Estilos específicos del componente MovieDialog.vue */
.dialog-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 9999;
}

.dialog-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  text-align: center;
}

.close-button
{
  position: absolute;
  top: 10px;
  right: 10px;
  width: 50px;
  height: 50px;
  border: none;
  background-color: transparent;
  cursor: pointer;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 5px;
}

.close-icon {
  position: relative;
  width: 30px;
  height: 30px;
  border: 4px solid red;
  border-radius: 50%;
}

.close-icon::before,
.close-icon::after {
  content: "";
  position: absolute;
  width: 16px;
  height: 4px;
  background-color: red;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.close-icon::before {
  transform: translate(-50%, -50%) rotate(45deg);
}

.close-icon::after {
  transform: translate(-50%, -50%) rotate(-45deg);
}

/* Estilos para los cuadros de género, idioma y clasificación */
.genre-container,
.language-container,
.classification-container {
  margin-top: 10px;
}

.genre-container strong,
.language-container strong,
.classification-container strong {
  display: block;
  margin-bottom: 5px;
}

.genre-container ul,
.language-container ul,
.classification-container ul {
  list-style-type: none;
  padding: 0;
}

.genre-container li,
.language-container li,
.classification-container li {
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 3px;
  padding: 2px 5px;
  margin-right: 5px;
}

.options-list {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
  justify-content: center; /* Centrar horizontalmente las opciones */
}

.option-item {
  display: inline-block;
  background-color: #eee;
  padding: 2px 5px;
  border-radius: 3px;
  text-align: center; /* Centrar verticalmente el texto */
}
</style>
