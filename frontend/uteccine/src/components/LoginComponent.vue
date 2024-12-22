<template>
  <div class="container">
    <div class="login">
      <h1 class="login-title">Login</h1>
      <div class="main">
        <form @submit.prevent="login">
          <div class="input-group">
            <label for="username">Username</label>
            <input type="text" v-model="username" placeholder="Enter your username" id="username" class="input-field">
          </div>
          <div class="input-group">
            <label for="password">Password</label>
            <input type="password" v-model="password" placeholder="Enter your password" id="password" class="input-field">
          </div>
          <div class="input-group">
            <button>Login</button>
          </div>
        </form>
        <div class="signup-link">
          <p>¿No tienes cuenta? <router-link class="link" to="/register">Regístrate</router-link></p>
        </div>
      </div>
    </div>
    <div class="img">
      <span>
        <h1>Welcome</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit</p>
      </span>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginComponent',
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    login() {
      axios.post('http://proyect-1296764638.us-east-1.elb.amazonaws.com:8001/login', {
          username: this.username,
          password: this.password
        })
        .then(response => {
          if (response.status === 200) {
            // Inicio de sesión exitoso
            this.$store.commit('setUsername', this.username); // Guardar el nombre de usuario en el store
            this.$store.commit('setLoggedIn', true);
            this.$router.push('/');
          } else {
            alert('Error en la solicitud de inicio de sesión');
          }
        })
        .catch(error => {
          if (error.response) {
            if (error.response.status === 404) {
              alert('Este usuario no existe');
            } else if (error.response.status === 403) {
              alert('Contraseña incorrecta');
            } else {
              alert('Error en la solicitud de inicio de sesión');
            }
          } else {
            console.error(error);
          }
        });
    },
  },
};
</script>
<style scoped>
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

html, body {
  width: 100%;
  height: 100%;
  display: flex;
  background-image: url(https://media.discordapp.net/attachments/1097364694752305213/1107112319026208838/bg.jpg?width=759&height=427);
  background-size: cover;
  background-position: center;
  font-family: sans-serif;
}

.container {
  display: flex;
  margin: auto;
  width: 800px;
  height: 400px;
  box-shadow: 4px 4px 4px #014670;
  background-image: url(https://media.discordapp.net/attachments/1097364694752305213/1107112319026208838/bg.jpg?width=759&height=427);
  background-size: cover;
  background-position: center;
  font-family: sans-serif;
}

.main button {
  width: 100%;
  height: 35px;
  margin-top: 20px;
  font-size: 15px;
  background-color: blue;
  color: white;
}


.login {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 300px;
  background-color: #eaeaea;
  text-align: center;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 4px 4px 4px #014670;
}

.login-title {
  margin-bottom: 20px;
  color: #014670;
  font-size: 35px;
}

.main form {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: transparent !important; /* Fondo completamente transparente */
  border: none !important; /* Sin borde */
  box-shadow: none !important; /* Sin sombra */
}

.input-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 15px;
}

.input-group label {
  margin-bottom: 5px;
  color: #014670;
  font-weight: bold;
}

.input-field {
  width: 100%;
  height: 35px;
  padding-left: 8px;
  box-sizing: border-box;
  outline: none;
  border: 1px solid #014670;
  color: #014670;
}

.main button:hover,
.input-field:hover {
  box-shadow: 3px 3px 3px rgba(1, 70, 112, 0.5);
}

.main a {
  display: block;
  font-size: 13px;
  text-align: right;
  color: #014670;
  margin-top: 10px;
  text-decoration: none;
}

.img {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  order: 2;
  flex-grow: 2;
  background-image: url(https://media.discordapp.net/attachments/1097364694752305213/1107112319026208838/bg.jpg?width=759&height=427);
  background-size: cover;
  background-position: center;
  text-align: center;
  color: #eee;
}


.img span {
  margin: auto;
}

.img span h1 {
  font-size: 50px;
  text-shadow: 0 0 10px #014670;
}

.img span p {
  font-size: 15px;
}

.signup-link {
  margin-top: 10px;
  text-align: center;
  color: #014670;
  display: flex;
  justify-content: center;
}

.signup-link p {
  font-size: 13px;
  margin: 0;
}

.link {
  padding-right: 32px;
}

.signup-link a {
  color: #014670;
  text-decoration: none;
}


.input-group button {
  margin: 0 auto; /* Centrar el botón */
  display: block;
}
</style>

