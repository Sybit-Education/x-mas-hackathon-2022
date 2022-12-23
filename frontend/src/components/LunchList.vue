<template>
  <table width="100%">
    <thead>
      <tr>
        <td>Restaurant</td>
        <td>Datum</td>
        <td>Menü</td>
        <td>Beschreibung</td>
        <td>Preis</td>
      </tr>
    </thead>
    <tr v-for="(menu, index) in menuList" :key="index">
      <td>
        <restaurant-label :restaurant-id="menu.restaurant_id" />
      </td>
      <td>
        {{ menu.date }}
      </td>
      <td>
        <h5>{{ menu.name }}</h5>
      </td>
      <td>
        {{ menu.description }}
      </td>
      <td>
        {{ menu.price }}
      </td>
    </tr>
  </table>
</template>
<script lang="ts">
import { mapState } from 'pinia'
import { useMenuStore } from '../stores/menu'
import RestaurantLabel from './RestaurantLabel.vue'

export default {
  name: 'LunchList',
  components: { RestaurantLabel },
  computed: {
    ...mapState(useMenuStore, {
      menuList: (store) => store.getAll,
    }),
  },
}
</script>
