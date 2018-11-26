<template>
  <div id = "panelContainer">
      <!--<ag-grid-vue style="width: 100%; height: 100%;"
                  class="ag-theme-balham"
                  :columnDefs="columnDefs"
                  :rowData="rowData"
                  :enableSorting="true"
                  :enableFilter="true"
                  :enableColResize="true">
      </ag-grid-vue>-->
      <span style="white-space: pre-wrap;">{{data}}</span>
  </div>
</template>

<script>
import {AgGridVue} from "ag-grid-vue";
export default {
  name: 'BasePanel',
  props: ["data"],
   data() {
            return {
                columnDefs: null,
                rowData: null
            }
        },
    components: {
        AgGridVue
    },
    beforeMount() {
        this.columnDefs = [
            {headerName: 'Make', field: 'make'},
            {headerName: 'Model', field: 'model'},
            {headerName: 'Price', field: 'price'},
            {headerName: 'Year', field: 'year'},
            {headerName: 'Owner', field: 'owner'},
            {headerName: 'Color', field: 'color'}
        ];

        this.rowData = [
            {make: 'Toyota', model: 'Celica', price: 35000, year: 1997, owner: "John Doe", color: "Red"},
            {make: 'Ford', model: 'Mondeo', price: 32000, year: 2003, owner: "Joan Doe", color: "Silver"},
            {make: 'Porsche', model: 'Boxter', price: 72000, year: 2015, owner: "Johnny Doe", color: "Black"},
            {make: 'Toyota', model: 'Celica', price: 35000, year: 1997, owner: "John Doe", color: "Red"},
            {make: 'Ford', model: 'Mondeo', price: 32000, year: 2003, owner: "Joan Doe", color: "Silver"},
            {make: 'Porsche', model: 'Boxter', price: 72000, year: 2015, owner: "Johnny Doe", color: "Black"},
            {make: 'Toyota', model: 'Celica', price: 35000, year: 1997, owner: "John Doe", color: "Red"},
            {make: 'Ford', model: 'Mondeo', price: 32000, year: 2003, owner: "Joan Doe", color: "Silver"},
            {make: 'Porsche', model: 'Boxter', price: 72000, year: 2015, owner: "Johnny Doe", color: "Black"},
            {make: 'Toyota', model: 'Celica', price: 35000, year: 1997, owner: "John Doe", color: "Red"},
            {make: 'Ford', model: 'Mondeo', price: 32000, year: 2003, owner: "Joan Doe", color: "Silver"},
            {make: 'Porsche', model: 'Boxter', price: 72000, year: 2015, owner: "Johnny Doe", color: "Black"},
            {make: 'Toyota', model: 'Celica', price: 35000, year: 1997, owner: "John Doe", color: "Red"},
            {make: 'Ford', model: 'Mondeo', price: 32000, year: 2003, owner: "Joan Doe", color: "Silver"},
            {make: 'Porsche', model: 'Boxter', price: 72000, year: 2015, owner: "Johnny Doe", color: "Black"},
            {make: 'Toyota', model: 'Celica', price: 35000, year: 1997, owner: "John Doe", color: "Red"},
            {make: 'Ford', model: 'Mondeo', price: 32000, year: 2003, owner: "Joan Doe", color: "Silver"},
            {make: 'Porsche', model: 'Boxter', price: 72000, year: 2015, owner: "Johnny Doe", color: "Black"},
            {make: 'Toyota', model: 'Celica', price: 35000, year: 1997, owner: "John Doe", color: "Red"},
            {make: 'Ford', model: 'Mondeo', price: 32000, year: 2003, owner: "Joan Doe", color: "Silver"},
            {make: 'Porsche', model: 'Boxter', price: 72000, year: 2015, owner: "Johnny Doe", color: "Black"},
            {make: 'Toyota', model: 'Celica', price: 35000, year: 1997, owner: "John Doe", color: "Red"},
            {make: 'Ford', model: 'Mondeo', price: 32000, year: 2003, owner: "Joan Doe", color: "Silver"},
            {make: 'Porsche', model: 'Boxter', price: 72000, year: 2015, owner: "Johnny Doe", color: "Black"},
            {make: 'Toyota', model: 'Celica', price: 35000, year: 1997, owner: "John Doe", color: "Red"},
            {make: 'Ford', model: 'Mondeo', price: 32000, year: 2003, owner: "Joan Doe", color: "Silver"},
            {make: 'Porsche', model: 'Boxter', price: 72000, year: 2015, owner: "Johnny Doe", color: "Black"},
            {make: 'Toyota', model: 'Celica', price: 35000, year: 1997, owner: "John Doe", color: "Red"},
            {make: 'Ford', model: 'Mondeo', price: 32000, year: 2003, owner: "Joan Doe", color: "Silver"},
            {make: 'Porsche', model: 'Boxter', price: 72000, year: 2015, owner: "Johnny Doe", color: "Black"},
            {make: 'Toyota', model: 'Celica', price: 35000, year: 1997, owner: "John Doe", color: "Red"},
            {make: 'Ford', model: 'Mondeo', price: 32000, year: 2003, owner: "Joan Doe", color: "Silver"},
            {make: 'Porsche', model: 'Boxter', price: 72000, year: 2015, owner: "Johnny Doe", color: "Black"},
            {make: 'Toyota', model: 'Celica', price: 35000, year: 1997, owner: "John Doe", color: "Red"},
            {make: 'Ford', model: 'Mondeo', price: 32000, year: 2003, owner: "Joan Doe", color: "Silver"},
            {make: 'Porsche', model: 'Boxter', price: 72000, year: 2015, owner: "Johnny Doe", color: "Black"}
        ];
    }
}

</script>

<style lang="scss" scoped>
  @import "../assets/variables.sass";
  @import "../assets/icofont.min.css";
  #panelContainer{
    width: 60%;
    border-radius: 10px;
    background-color: $neutral100;
    box-shadow: 0 2px 6px 0 hsla(0, 0%, 0%, 0.2);
    margin: 1em auto 5em;
    position: relative;
    font-family: $font-primary;
    height: 60vh;
    overflow-y: scroll;
    padding: 1em 1.5em;
    box-sizing: border-box;
    span{
      font-size: $size-base;
      line-height: 1.75em;
    }
  }
</style>
