<template>
  <div class="register">
    <div class="register-container">
      <h2>Registro</h2>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="username">Nombre de usuario:</label>
          <input type="text" id="username" class="form-control" v-model="username">
        </div>
        <div class="form-group">
          <label for="email">Correo electrónico:</label>
          <input type="email" id="email" class="form-control" v-model="email">
        </div>
        <div class="form-group">
          <label for="password">Contraseña:</label>
          <input type="password" id="password" class="form-control" v-model="password">
        </div>
        <div class="form-group">
          <label for="names">Nombres:</label>
          <input type="text" id="names" class="form-control" v-model="names">
        </div>
        <div class="form-group">
          <label for="surnames">Apellidos:</label>
          <input type="text" id="surnames" class="form-control" v-model="surnames">
        </div>
        <button type="submit" class="btn btn-primary">Registrarse</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
      names: '',
      surnames: ''
    };
  },
  methods: {
    submitForm() {
      axios.post('http://proyect-1296764638.us-east-1.elb.amazonaws.com:8001/user', {
        username: this.username,
        email: this.email,
        password: this.password,
        names: this.names,
        surnames: this.surnames
      })
        .then(response => {
          if (response.data.success) {
            this.$router.push('/Login');
          } else {
            alert('Error al crear el usuario o correo ya existe');
          }
        })
        .catch(error => {
          if (error.response && error.response.status === 400) {
            alert('El usuario o correo ya existe');
          } else {
            console.error(error);
          }
        });
    }
  }
};
</script>
<style>
@import url('https://fonts.googleapis.com/css?family=Nunito+Sans:400,700&display=swap');

body {
  font-family: 'Nunito Sans', sans-serif;
}

.register {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-image: url('https://wallpaper-house.com/data/out/6/wallpaper2you_122658.jpg');
  background-repeat: no-repeat;
  background-size: cover;
}

.register-container {
  text-align: center;
  background-color: #ffffff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 400px;
}

.register h2 {
  margin-bottom: 30px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  font-weight: bold;
  display: block;
  margin-bottom: 5px;
}

.form-control {
  border: 2px solid #dddddd;
  border-radius: 3px;
  padding: 10px;
  width: 100%;
}

.btn-primary {
  background-color: #4caf50;
  color: #ffffff;
  border: none;
  border-radius: 3px;
  padding: 10px 20px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-primary:hover {
  background-color: #2e7d32;
  transition: opacity 0.3s ease;
}
</style>
