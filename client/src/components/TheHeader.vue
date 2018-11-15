<template>
  <div id = "headerContainer">
      <span class = "name">Veritas</span>
      <span class = "version">alpha</span>
  </div>
</template>

<script>
export default {
  name: 'TheHeader'
}
</script>

<style lang="scss" scoped>
  @import "../assets/variables.sass";
  @import "../assets/icofont.min.css";
  #headerContainer{
    width: 60%;
    margin: 5em auto 0;
    font-family: $font-primary;
    .name{
        color: $primary500;
        font-size: $size-large;
        font-weight: $weight-bold;
    }
    .version{
        color: $neutral900;
    }
  }
</style>
