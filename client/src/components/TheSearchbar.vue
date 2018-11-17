<template>
  <div id = "searchBoxContainer">
    <form @submit.prevent="handleSubmit">
      <input id = "searchBox" autofocus v-model="searchValue"/>
      <button type="submit">
        <i class="icofont-search-1"></i>
      </button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'TheSearchbar',
  data() {
    return {
      searchValue: ''
    }
  },
  methods: {
    handleSubmit() {
      this.$emit("submitted", this.searchValue);
    }
  }
}

</script>

<style lang="scss" scoped>
  @import "../assets/variables.sass";
  @import "../assets/icofont.min.css";
  #searchBoxContainer{
    width: 60%;
    border-radius: 10px;
    background-color: $neutral100;
    box-shadow: 0 2px 6px 0 hsla(0, 0%, 0%, 0.2);
    margin: 1em auto;
    position: relative;
    text-align: left;
    #searchBox{
      padding: 1em 1em;
      border: none;
      outline: none;
      font-size: $size-medium;
      margin: 0;
      background-color: $transparent;
      width: calc(100% - 5em);
      font-family: $font-primary;
    }
    button{
      position: absolute;
      right: 0px;
      top: 0px;
      height: 100%;
      background-color: $primary500;
      border: none;
      border-top-right-radius: 10px;
      border-bottom-right-radius: 10px;
      width: 5em;
      transition: all 0.2s ease-in-out;
      i{
        font-size: 1.5em;
        color: $neutral100;
      }
      &:hover{
        background-color: $primary900;
        cursor: pointer;
        cursor: mouse;
      }
      &:focus{
        outline: none;
      }
    }
  }
</style>
