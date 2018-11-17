<template>
  <div id="app">
    <TheHeader />
    <TheSearchbar @submitted="onSubmit" />
    <BasePanel />
  </div>
</template>

<script>
import TheSearchbar from "./components/TheSearchbar.vue";
import TheHeader from "./components/TheHeader.vue";
import BasePanel from "./components/BasePanel.vue";
export default {
  name: 'app',
  components: {
    TheHeader,
    TheSearchbar,
    BasePanel
  },
  methods: {
    onSubmit(searchQuery) {
      
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Karla:400,400i,700,700i');
body{
  background-color: #e1e7ec;
}
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  transition: all 0.2s ease-in-out;
}
</style>
