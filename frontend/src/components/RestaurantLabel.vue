<template>
  <div>
    <a :href="getById(restaurantId).homepage" target="_blank">
      <img :src="getById(restaurantId).logo" height="25" />
      {{ getById(restaurantId).name }}
    </a>
  </div>
</template>
<script lang="ts">
import { useRestaurantStore } from '../stores/restaurant'

export default {
  name: 'RestaurantLabel',
  setup() {
    const store = useRestaurantStore()

    return { getById: store.getById }
  },
  props: {
    restaurantId: {
      type: String,
      required: true,
    },
  },
}
</script>
