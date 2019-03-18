<template>
<div>
  <!-- the condition is to determine whether plural is needed. 
  If there is a carriage return inside the result (not at the end) 
  or the result is an array, then there are multiple results. -->
  <span v-bind:class="classObject"><b>{{type}}</b> result</span>

  <div id = "panelContainer">

      <div v-if="type === 'SPARQL'"> 
        <div v-if="data.results === 'Loading'" class="spinner">
          <div class="double-bounce1"></div>
          <div class="double-bounce2"></div>
        </div>
            <span v-else style="white-space: pre-wrap; display: inline-block; padding-top: 0.5em; padding-bottom: 0.5em;">{{data.results}}</span>
      </div>
      <div v-else-if="type === 'SQL'">
         <div v-if="data[0].value === 'Loading'" class="spinner">
          <div class="double-bounce1"></div>
          <div class="double-bounce2"></div>
        </div>
        <ag-grid-vue v-else style="width: 100%; height: 30vh; padding: 1em 0; background-color: #f8f9fa;"
                    class="ag-theme-balham"
                    :columnDefs="columnDefs"
                    :rowData="data"
                    :enableSorting="true"
                    :enableFilter="true"
                    :onGridReady="onGridReady" 
                    >
        </ag-grid-vue>
      </div>
      <div v-else-if="type === 'Google'">
         <div v-if="data[0].title === 'Loading'" class="spinner">
          <div class="double-bounce1"></div>
          <div class="double-bounce2"></div>
        </div>
        <ul v-else>
          <li v-for="(result, index) in data" :key="`result-${index}`">
            <h1>{{result.title.split(/(http|www)\w+/)[0]}}</h1>
            <a v-if="result.link" :href="result.link">{{result.link.substring(0, 40)}}(...)</a>
            <p v-if="result.description">{{result.description}}</p>
          </li>
        </ul>
      </div>
  </div>
</div>
</template>

<script>
import {AgGridVue} from "ag-grid-vue";

export default {
  name: 'BasePanel',
  props: ["data", "type"],
  data() {
            return {
                columnDefs: null
            }
        },
  components: {
      AgGridVue
  },
  beforeMount() {
      this.columnDefs = [
          {headerName: 'Results', field: 'value'}
      ];
  },
  computed: {
    classObject: function () {
      return {
        'resultsSource': true,
        'colorGoogle': this.type === 'Google',
        'colorSPARQL': this.type === 'SPARQL',
        'colorSQL': this.type === 'SQL'
      }
    }
  },
  methods: {
    onGridReady(params){
      params.api.sizeColumnsToFit();
    }
  },
  beforeUpdate() {
    if(this.type === "Google"){
      this.data.filter(item => item.title.length > 3);
    }
  }
}

</script>

<style lang="scss" scoped>
  @import "../../node_modules/ag-grid-community/dist/styles/ag-grid.css";
  @import "../../node_modules/ag-grid-community/dist/styles/ag-theme-balham.css";
  @import "../assets/variables.sass";
  @import "../assets/icofont.min.css";
  .colorGoogle{
    background-color: $sourceGoogle;
  }
  .colorSPARQL{
    background-color: $sourceSPARQL;
  }
  .colorSQL{
    background-color: $sourceSQL;
  }
  .resultsSource{
    margin: 1em 0em 0em 20%;
    position: relative;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    padding: 0.25em 1em;
    display: inline-block;
    font-family: $font-primary;
    color: $neutral100;
  }
  #panelContainer{
    width: 60%;
    border-radius: 10px;
    border-top-left-radius: 0px;
    background-color: $neutral100;
    box-shadow: 0 2px 6px 0 hsla(0, 0%, 0%, 0.2);
    margin: 0em auto 0.5em;
    position: relative;
    font-family: $font-primary;
    max-height: 40vh;
    overflow-y: auto;
    padding: 0em 1em;
    box-sizing: border-box;
    overflow-x: hidden;
    span{
      font-size: $size-base;
      line-height: 1.75em;
    }
    ul{
      list-style-type: none;
      padding: 0px;
      li{
        margin-top: 1.5em;
        h1{
          margin: 0px;
          padding: 0px;
          font-size: 1.5em;
        }
        a{
          margin: 0px;
          padding: 0px;
        }
        p{
          margin: 0.5em 0em 0em 0em;
          padding: 0px;
        }
      }
      li:first-child{
        margin-top: 0em;
      }
    }
  }
  #panelContainer::-webkit-scrollbar {
      -webkit-appearance: none;
  }

  #panelContainer::-webkit-scrollbar:vertical {
      width: 11px;
  }

  #panelContainer::-webkit-scrollbar:horizontal {
      height: 11px;
  }

  #panelContainer::-webkit-scrollbar-thumb {
      border-radius: 8px;
      border: 2px solid white; /* should match background, can't be transparent */
      background-color: rgba(0, 0, 0, .5);
  }
  .spinner {
  width: 40px;
  height: 40px;

  position: relative;
  margin: 50px auto;
}

.double-bounce1, .double-bounce2 {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background-color: #333;
  opacity: 0.6;
  position: absolute;
  top: 0;
  left: 0;
  
  -webkit-animation: sk-bounce 2.0s infinite ease-in-out;
  animation: sk-bounce 2.0s infinite ease-in-out;
}

.double-bounce2 {
  -webkit-animation-delay: -1.0s;
  animation-delay: -1.0s;
}

@-webkit-keyframes sk-bounce {
  0%, 100% { -webkit-transform: scale(0.0) }
  50% { -webkit-transform: scale(1.0) }
}

@keyframes sk-bounce {
  0%, 100% { 
    transform: scale(0.0);
    -webkit-transform: scale(0.0);
  } 50% { 
    transform: scale(1.0);
    -webkit-transform: scale(1.0);
  }
}

</style>
