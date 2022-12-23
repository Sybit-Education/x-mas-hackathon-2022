<template>
  <table width="100%">
    <thead>
      <tr>
        <th width="20%">Datum</th>
        <th>Menü</th>
        <th width="10%">Preis</th>
        <th width="20%">Restaurant</th>
      </tr>
    </thead>
    <tr v-for="(menu, index) in menuList" :key="index">
      <td>
        {{ menu.date }}
      </td>
      <td>
        <h4>{{ menu.name }}</h4>
        <p>{{ menu.description }}</p>
      </td>
      <td>
        {{ menu.price }}
      </td>
      <td>
        <restaurant-label :restaurant-id="menu.restaurant_id" />
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
