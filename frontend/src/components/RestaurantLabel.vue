<template>
  <div v-if="getById(restaurantId)">
    <a v-if="homepage" :href="homepage" target="_blank">
      <img v-if="logo" :src="logo" height="25" /><br />
      {{ name }}, {{ city }}
    </a>
    <span v-else>
      <img v-if="logo" :src="logo" height="25" /><br />
      {{ name }}, {{ city }}
    </span>
  </div>
  <div v-else>[loading ...]</div>
</template>
<script lang="ts">
import { useRestaurantStore } from '../stores/restaurant'

export default {
  name: 'RestaurantLabel',
  props: {
    restaurantId: {
      type: String,
      required: true,
    },
  },
  setup() {
    const store = useRestaurantStore()

    return { getById: store.getById }
  },
  computed: {
    homepage() {
      return this.getById(this.restaurantId)?.homepage
    },
    logo() {
      return this.getById(this.restaurantId)?.logo
    },
    name() {
      return this.getById(this.restaurantId)?.name
    },
    city() {
      return this.getById(this.restaurantId)?.city
    },
  },
}
</script>
