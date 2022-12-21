<template>
  <img src="../assets/milanesa-napolitana-ensalada.jpg">
  <Searchbar/>
</template>

<script setup lang="ts">
import Searchbar from "@/components/Searchbar.vue"
</script>

<style>
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
  padding: 0 15px 15px 0;
}
input{
  width: 87%;
  height: 30px;
}
.form-button {
  background-color: #00bd7e;
  height: 30px;
}
</style>