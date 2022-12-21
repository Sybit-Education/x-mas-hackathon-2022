<template>
  <div>
    <button @click="$router.push({ name: 'home' })">Go Back</button>
  </div>
  <h1>Details</h1>
</template>

<script>
export default {
  name: "Detail.vue"
}
</script>

<style>
button{
  background-color: #00bd7e;
}
</style>