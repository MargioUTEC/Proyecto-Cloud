<template>
  <div id="app">
    <NavigationMenu />
    <router-view />
    <FooterSection />
  </div>
</template>

<script>
import NavigationMenu from './components/NavigationMenu.vue';
import FooterSection from './components/FooterSection.vue';

export default {
  components: {
    NavigationMenu,
    FooterSection
  }
}
</script>

<style>
/* Global styles for the App.vue component */
#app {
  /* Styles for the main container of the application */
}
</style>

