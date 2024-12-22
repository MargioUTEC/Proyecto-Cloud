import { createStore } from 'vuex';

export default createStore({
  state: {
    isLoggedIn: false,
    username: '',
  },
  mutations: {
    setUsername(state, username) {
      state.username = username;
    },
    setLoggedIn(state, isLoggedIn) {
      state.isLoggedIn = isLoggedIn;
    },
    clearUserData(state) {
      state.username = '';
      state.isLoggedIn = false;
    },
  },
  actions: {
    logout({ commit }) {
      commit('clearUserData');
      // Aquí puedes redirigir al usuario a la página de inicio
    },
  },
  getters: {
    isLoggedIn(state) {
      return state.isLoggedIn;
    },
    getUsername(state) {
      return state.username;
    },
  },
});

