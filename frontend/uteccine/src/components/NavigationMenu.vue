<template>
  <nav>
    <router-link to="/">
      <div class="logo">
        <img src="https://media.discordapp.net/attachments/1097364694752305213/1107479597437681764/logouteccine.png" alt="Logo">
      </div>
    </router-link> 
    <ul class="nav-links">
      <li><router-link to="/">Inicio</router-link></li>
      <li><router-link to="/Login">Login</router-link></li>
      <li><router-link to="/dulceria">Dulceria</router-link></li>
      <li><router-link to="/compras">Mis Compras</router-link></li>
    </ul>
    <div class="user-info" v-if="isLoggedIn">

      <div class="username-box">{{ username }}</div>
      <button @click="logout">Desconectar</button>
    </div>
  </nav>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  computed: {
    ...mapGetters(['isLoggedIn', 'getUsername']),
    username() {
      return this.getUsername;
    }
  },
  methods: {
    ...mapActions(['logout'])
  },
  mounted() {
    if (!this.isLoggedIn) {
      this.$router.push('/'); // Redirecciona al home si no hay usuario logueado
    }
  }
}
</script>

<style>
/* Estilos CSS específicos del componente Navbar */
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background: linear-gradient(to bottom, #2980B9, #48C9B0, #BB8FCE, #ED51FF);
}

.logo img {
  height: 115px;
  /* Estilos adicionales para el logotipo */
}

.user-info {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 0.5rem;
  color: #fff;
}

.username-box {
  display: inline-block;
  padding: 5px 10px;
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 4px;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 1rem;
  align-items: center; /* Centra verticalmente los enlaces */
  flex-grow: 1; /* Ocupa el espacio disponible */
  justify-content: center; /* Centra horizontalmente los enlaces */
}

.nav-links li {
  text-align: center;
}

.nav-links li a {
  text-decoration: none;
  color: #fff;
  font-size: 24px;
  font-weight: bold;
}
</style>

