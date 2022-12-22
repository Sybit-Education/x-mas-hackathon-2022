<template>
  <div class="grid-container">
    <div class="restaurant">TestRestaurant</div>
    <div class="desc">Mehr infos</div>
    <div class="desc">
      <p><a class="link" href="https://www.google.de/">Zum Mittagstisch</a>
      </p></div>
    <div class="restaurant">TestRestaurant2</div>
    <div class="desc">Beschreibung</div>
    <div class="desc">
      <p><a class="link" href="https://www.google.de/">Zum Mittagstisch</a></p>
    </div>
  </div>
</template>

<script>
export default {
  name: "RestaurantGrid.vue",
  props:{
    restaurantId: {
      type: String,
      required: true,
    }
  },
  data() {
    return {
      restaurant: null,
    }
  }
}
</script>

<style scoped>
.grid-container {
  display: grid;
  grid-template-columns: auto auto auto;
  padding: 10px;
}

.restaurant {
  color: #07d995;
  font-size: large;
}

.link {
  color: #3ca2ef;
}
</style>