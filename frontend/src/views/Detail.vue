<template>
  <h1 class="header">Details</h1>
  <RestaurantGrid/>
</template>

<script lang="ts">
import RestaurantGrid from "@/components/RestaurantGrid.vue"
export default {
  name: "Detail.vue",
  components: {RestaurantGrid}
}
</script>

<style>
.header {
  color: #00bd7e;
  margin-bottom: 15px;
}

</style>