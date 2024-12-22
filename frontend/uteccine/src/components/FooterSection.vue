<template>
  <footer>
    <div class="footer-content">
      <div class="logo">

      </div>
      <ul class="footer-links">

        <!-- Agrega más enlaces según sea necesario -->
      </ul>
    </div>
    <div class="social-media-links">
      <a href="#"><i class="fab fa-facebook"></i></a>
      <a href="#"><i class="fab fa-twitter"></i></a>
      <a href="#"><i class="fab fa-instagram"></i></a>
      <!-- Agrega más enlaces de redes sociales según sea necesario -->
    </div>
  </footer>
</template>

<script>
export default {
  // Lógica del componente Footer
}
</script>

<style scoped>
/* Estilos CSS específicos del componente Footer */
footer {
  background-color: #f5f5f5;
  padding: 1rem;
  text-align: center;
}

.footer-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo img {
  height: 40px;
  /* Estilos adicionales para el logotipo */
}

.footer-links {
  list-style: none;
  display: flex;
  gap: 1rem;
}

.footer-links li a {
  text-decoration: none;
  color: #333;
  /* Estilos adicionales para los enlaces del footer */
}

.social-media-links a {
  margin: 0 0.5rem;
  color: #333;
  /* Estilos adicionales para los enlaces de redes sociales */
}
</style>
