<template>
  <div id="app">
    <TheHeader />
    <TheSearchbar @submitted="onSubmit" />
    <BasePanel v-if="quepyResults" :data="quepyResults" type="SPARQL"/>
    <BasePanel v-if="googleResults" :data="sqlResults" type="SQL"/>
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
            googleResults: "",
            sqlResults: ""
        }
    }
  ,
  /* eslint-disable */
  methods: {
    async getQuepy(query){
        const responseQuepy = await axios.get('http://localhost:8081/?questionSparql=' + query);
        this.quepyResults = responseQuepy["data"]["quepyResults"];
        console.log(this.quepyResults.query);

        const adjustedQuery = encodeURIComponent(this.quepyResults.query) + "&output=json";

        const responseD2rq = await axios.get('http://localhost:2020/sparql?query=' + adjustedQuery);
        console.log(responseD2rq);
        this.sqlResults = responseD2rq.data.results.bindings.map(el => el.x1);
    },
    async getGoogle(query){
        const responseGoogle = await axios.get('http://localhost:8081/?questionGoogle=' + query);
        this.googleResults = responseGoogle["data"]["googleResults"];
    },
    async onSubmit(searchQuery) {
      let self = this;
      try{
        self.quepyResults = {results: "Loading", query: ""};
        self.googleResults = [{title: "Loading", description: "Fetching Google Search results..."}]; 
        self.sqlResults = [{value: "Loading"}]; 

        const [quepyReturn, googleReturn] = await Promise.all([
          self.getQuepy(searchQuery),
          self.getGoogle(searchQuery)
        ]);
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
