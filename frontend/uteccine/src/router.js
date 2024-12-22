import { createRouter, createWebHistory } from 'vue-router';
import HomeSection from './components/HomeSection.vue';
import LoginComponent from './components/LoginComponent.vue'; // Asegúrate de importar el componente 'Login' correctamente
import MovieDetails from './components/MovieDetails.vue';
import RegisterForm from './components/RegisterForm.vue';
import MisCompras from './components/MisCompras.vue';
import MiDulceria from './components/MiDulceria.vue';

const routes = [
  {
    path: '/',
    name: 'HomeSection',
    component: HomeSection
  },
  {
    path: '/login',
    component: LoginComponent,
  },
  {
    path: '/register',
    component: RegisterForm,
  },
  {
    path: '/compras',
    component: MisCompras,
  },
  {
    path: '/dulceria',
    component: MiDulceria,
  },
  
  {
    path: '/movie/:id',
    name: 'MovieDetails',
    component: MovieDetails
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
