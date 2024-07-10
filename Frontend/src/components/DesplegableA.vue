<template>
    <div class="desplegar" @click="mostrado = !mostrado">Desplegar tanque</div>
    <transition name="talla">
      <div class="desplegable" v-if="mostrado">
        <p>wawwawawawawaw</p>
      </div>
    </transition>
    <div class="random">asdad</div>
</template>

<script setup>
import { ref } from 'vue';

let mostrado = ref(false)


</script>

<style>
  .talla-enter-active, .talla-leave-active{
    transition: .2s ease;
  }
  .talla-enter-from, .talla-leave-to{
    margin-top: -200px;
  }
  .desplegar{
    position: relative;
    background-color: red;
    z-index: 9;
    height: 200px;
  }
  .desplegable{
    background-color: blue;
    height: 200px;
    z-index: 8;
    position: relative;
  }
  .random{
    position: relative;
    background-color: green;
  }
</style>