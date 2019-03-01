<template>
<div>
  <!-- the condition is to determine whether plural is needed. 
  If there is a carriage return inside the result (not at the end) 
  or the result is an array, then there are multiple results. -->
  <span v-bind:class="classObject"><b>{{type}}</b> result<span v-if="Array.isArray(data) || data.indexOf('\n') !== (data.length - 1)">s</span>
  </span>
  <div id = "panelContainer">
      <!--<ag-grid-vue style="width: 100%; height: 100%;"
                  class="ag-theme-balham"
                  :columnDefs="columnDefs"
                  :rowData="rowData"
                  :enableSorting="true"
                  :enableFilter="true"
                  :enableColResize="true">
      </ag-grid-vue>-->
      <span v-if="type === 'Dataset'" 
            style="white-space: pre-wrap; display: inline-block; padding-top: 0.5em; padding-bottom: 0.5em;">{{data}}</span>
      <ul v-else>
        <li v-for="(result, index) in data" :key="`result-${index}`">
          <h1>{{result.title.split("http")[0]}}</h1>
          <a v-if="result.link" :href="result.link">{{result.link}}</a>
          <p v-if="result.description">{{result.description}}</p>
        </li>
      </ul>
  </div>
</div>
</template>

<script>

export default {
  name: 'BasePanel',
  props: ["data", "type"],
   data() {
            return {

            }
        },
    components: {
      
    },
    computed: {
      classObject: function () {
        return {
          'resultsSource': true,
          'colorGoogle': this.type === 'Google',
          'colorDataset': this.type === 'Dataset'
        }
      }
    },
    beforeMount() {
      if(this.data.type === "google"){
        this.data.filter(item => item.title.length > 3);
      }
    }
}

</script>

<style lang="scss" scoped>
  @import "../assets/variables.sass";
  @import "../assets/icofont.min.css";
  .colorGoogle{
    background-color: $sourceGoogle;
  }
  .colorDataset{
    background-color: $sourceDataset;
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

</style>
