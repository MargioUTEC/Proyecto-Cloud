<template>
  <div class="home-section">
    <div class="section-title">
      <img
        src="https://media.discordapp.net/attachments/1097364694752305213/1106766088802410576/pelicula_1.png?width=427&height=427"
        alt="Icono"
        class="icon"
      />
      <h1 class="title-text">Cartelera</h1>
    </div>
    <div class="movies-container">
      <div
        v-for="(movie, index) in upcomingMovies"
        :key="movie.id"
        :class="['movie', getMovieClass(movie.classification)]"
      >
        <div class="movie-wrapper">
          <div class="poster-container">
            <img
              :src="movie.poster[0]"
              alt="Movie Poster"
              class="movie-poster"
            />
            <div class="button-wrapper" v-if="showButtons[index]">
              <button class="more-button" @click="showDetails(movie.id)">
                Ver más
              </button>
              <button class="buy-button" @click="fetchOptions(movie.id)">
                Comprar
              </button>
            </div>
          </div>
          <div class="movie-details">
            <h3>{{ movie.title }}</h3>
            <p>{{ movie.releaseDate }}</p>
          </div>
        </div>
      </div>
    </div>
    <MovieDialog
  v-if="selectedMovie"
  :movie="selectedMovie"
  :options="options"
  @close="closeDescription"
  @buyOption="fetchOptions"
/>
  </div>
</template>
<script>
import axios from 'axios';
import MovieDialog from './MovieDialog.vue';

export default {
  data() {
  return {
    upcomingMovies: [],
    selectedMovie: null,
    showButtons: [],
    movieOptions: {}
  };
},

  components: {
    MovieDialog
  },

  mounted() {
    axios
      .get('http://proyect-1296764638.us-east-1.elb.amazonaws.com:8000/movies')
      .then(response => {
        this.upcomingMovies = response.data.movies.map(movie => {
          return {
            id: movie.id,
            title: movie.name,
            year: movie.year,
            gender: movie.gender,
            classification: movie.classification,
            duration: movie.duration,
            language: movie.language,
            description: movie.description,
            poster: this.generateLocalImagePaths(movie.id)
          };
        });
        this.showButtons = new Array(this.upcomingMovies.length).fill(true);
      })
      .catch(error => {
        console.error('Error al obtener las películas:', error);
      });
  },

  methods: {
    generateLocalImagePaths(movieId) {
      const imagePaths = [];
      if(movieId === 1){
imagePaths.push("https://media.discordapp.net/attachments/1097364694752305213/1107516678541168660/image.png")
}
if(movieId === 2){
imagePaths.push("https://media.discordapp.net/attachments/1097364694752305213/1107517088123334676/No-Time-to-Die-Official-Imax-Poster-1.png?width=341&height=427")
}
      if (movieId === 3) {

        imagePaths.push("https://media.discordapp.net/attachments/1097364694752305213/1107517347117420634/MV5BZWMyYzFjYTYtNTRjYi00OGExLWE2YzgtOGRmYjAxZTU3NzBiXkEyXkFqcGdeQXVyMzQ0MzA0NTM.png?width=288&height=427")
      }
if(movieId === 4){
imagePaths.push("https://media.discordapp.net/attachments/1097364694752305213/1107517607021662208/MV5BNmQxZTNiODYtNzBhYy00MzVlLWJlN2UtNTc4YWZjMDIwMmEzXkEyXkFqcGdeQXVyMTkxNjUyNQ.png?width=288&height=427")
}
if(movieId === 5){
imagePaths.push("https://media.discordapp.net/attachments/1016561697072353331/1107523361141166131/the-suicide-squad-new-character-posters_3zjs.png?width=288&height=427")
}
if(movieId === 6){
imagePaths.push("https://media.discordapp.net/attachments/1016561697072353331/1107523403197448243/MV5BYjkwMzIxYzMtOTVkMS00NDQxLThkMjItNzgxN2RiNjdlNTliXkEyXkFqcGdeQXVyODE5NzE3OTE.png?width=296&height=427")
}
if(movieId === 7){
imagePaths.push("https://media.discordapp.net/attachments/1016561697072353331/1107523663630192640/MV5BMGJkNDJlZWUtOGM1Ny00YjNkLThiM2QtY2ZjMzQxMTIxNWNmXkEyXkFqcGdeQXVyMDM2NDM2MQ.png?width=288&height=427")
}
if(movieId === 8){
imagePaths.push("https://media.discordapp.net/attachments/1016561697072353331/1107523851925065788/MV5BZGRhYjE2NWUtN2FkNy00NGI3LTkxYWMtMDk4Yjg5ZjI3MWI2XkEyXkFqcGdeQXVyMTEyMjM2NDc2.png?width=288&height=427")
}
if(movieId === 9){
imagePaths.push("https://media.discordapp.net/attachments/1016561697072353331/1107524013699379225/MV5BODMwYTYyY2ItOWQ5Yi00OTI1LTllYTQtYTdlNWM4YzJhYTM0XkEyXkFqcGdeQXVyMTA2MDU0NjM5.png?width=288&height=427")
}
if(movieId === 10){
imagePaths.push("https://media.discordapp.net/attachments/1016561697072353331/1107524239524909076/MV5BMzQ5ZDZhZDItZTNmZi00MWQ0LWJlNDUtZTE4ZWJmODNlM2Y3XkEyXkFqcGdeQXVyMDA4NzMyOA.png?width=288&height=426")
}
      else {
imagePaths.push('https://media.discordapp.net/attachments/1097364694752305213/1106766088802410576/pelicula_1.png?width=427&height=427');
      // Agrega condiciones if-else para otras películas si es necesario
      }
      return imagePaths;
    },

    getMovieClass(classification) {
      if (classification === 'G') {
        return 'clase-g';
      } else if (classification === 'PG') {
        return 'clase-pg-13'
      } else if (classification === 'PG-13') {
        return 'clase-pg-13';
      } else if       (classification === 'R') {
        return 'clase-r';
      } else {
        return '';
      }
    },

    showDetails(movieId) {
      const selectedMovie = this.upcomingMovies.find(movie => movie.id === movieId);
      if (selectedMovie) {
        this.selectedMovie = selectedMovie;
      }
    },

    closeDescription() {
      // Lógica para cerrar la descripción de la película
      // Puedes implementar esta función según tus necesidades
      this.selectedMovie = null;
    },

  fetchOptions(movieId) {
  // Verificar si el usuario está logeado
  if (!this.$store.state.username) {
    // Redireccionar al login
    this.$router.push('/login');
    return;
  }

   console.log(`Comprar ticket de la película con ID ${movieId}`);

  // Realiza la solicitud al servidor para obtener las opciones de películas
  axios
    .get(`http://proyect-1296764638.us-east-1.elb.amazonaws.com:8000/movies/${movieId}/options`)
    .then(response => {
      this.movieOptions = response.data.options;
    })
    .catch(error => {
      console.error('Error al obtener las opciones de películas:', error);
    });
}

  }
};
</script>

<style scoped>
/* Estilos específicos del componente HomeSection.vue */
.home-section {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.section-title {
  margin-bottom: 20px;
  display: flex;
  align-items: center;
}

.icon {
  width: 50px; /* Ajusta el tamaño según tus preferencias */
  margin-right: 10px; /* Ajusta el margen según tus preferencias */
}

.title-text {
  font-size: 1.5rem;
}

.movies-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 2rem;
}

.movie {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 1rem;
  cursor: pointer;
  position: relative;
}

.movie-grid {
  flex-basis: 33.33%;
}

.movie-wrapper {
  position: relative;
}

.poster-container {
  position: relative;
  width: 200px;
  height: 300px;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.movie-poster {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
  position: relative;
}

.movie-poster:hover {
  transform: scale(1.05);
}

.movie-details {
  margin-top: 0.5rem;
  text-align: center;
}

.button-wrapper {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: flex-end;
  background-color: rgba(0, 0, 0, 0.7);
  padding: 0.5rem;
  opacity: 0;
  transition: opacity 0.3s ease, transform 0.3s ease;
  transform: translateY(100%);
}

.movie-wrapper:hover .button-wrapper {
  opacity: 1;
  transform: translateY(0%);
}

.more-button,
.buy-button {
  padding: 0.5rem 1rem;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.more-button {
  background-color: #ff0000;
}

.buy-button {
  margin-left: 0.5rem;
  background-color: #ff0000;
}

.movie:hover .more-button,
.movie:hover .buy-button {
  background-color: #cc0000;
}

button:hover {
  background-color: #cc0000;
}

      .home-section {
  display: flex;
  flex-direction: column;
    align-items: center;
}

.section-title {
  margin-bottom: 20px;
  display: flex;
  align-items: center;
}

.icon {
  width: 50px; /* Ajusta el tamaño según tus preferencias */
  margin-right: 10px; /* Ajusta el margen según tus preferencias */
}

.title-text {
  font-size: 1.5rem;
}

.movies-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 2rem;
}

.movie {
  display: flex;
  flex-direction: column;
}

/* Estilos específicos para las clasificaciones de películas */
.clase-g {
  background-color: green;
}

.clase-pg-13 {
  background-color: orange;
}

.clase-r {
  background-color: red;
}
</style>

