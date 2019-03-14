<template>
  <div id="app">
    <TheHeader />
    <TheSearchbar @submitted="onSubmit" />
    <BasePanel v-if="quepyResults" :data="quepyResults" type="SPARQL"/>
    <BasePanel v-if="googleResults" :data="googleResults" type="Google"/>
  </div>
</template>

<script>
import TheSearchbar from "./components/TheSearchbar.vue";
import TheHeader from "./components/TheHeader.vue";
import BasePanel from "./components/BasePanel.vue";
import axios from 'axios';
export default {
  name: 'app',
  components: {
    TheHeader,
    TheSearchbar,
    BasePanel
  },
  data:
  function () {
        return {
            quepyResults: "",
            googleResults: ""
        }
    }
  ,
  /* eslint-disable */
  methods: {
    async onSubmit(searchQuery) {
      let self = this;
      try{
        self.quepyResults = {results: "Loading", query: ""};
        self.googleResults = [{title: "Loading", description: "Fetching Google Search results..."}]; 

        let responseQuepy = await axios.get('http://localhost:8081/?questionSparql=' + searchQuery);
        self.quepyResults = responseQuepy["data"]["quepyResults"];

        let responseGoogle = await axios.get('http://localhost:8081/?questionGoogle=' + searchQuery);
        self.googleResults = responseGoogle["data"]["googleResults"];
      }
      catch(e){
        // eslint-disable-next-line
        console.log(e);
      }
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
  padding-bottom: 2em;
}
</style>
