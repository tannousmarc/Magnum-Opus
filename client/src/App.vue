<template>
  <div id="app">
    <TheHeader />
    <TheSearchbar @submitted="onSubmit" />
    <BasePanel :data="result"/>
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
            result: ""
        }
    }
  ,
  methods: {
    onSubmit(searchQuery) {
      let self = this;
      axios.get('http://localhost:8081/?question=' + searchQuery)
      .then(function (response) {
        // handle success
        console.log(response);
        self.result = response["data"];
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      });
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
