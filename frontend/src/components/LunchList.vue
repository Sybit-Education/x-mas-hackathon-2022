<template>
  <table width="100%">
    <thead>
      <tr>
        <th width="20%">Datum</th>
        <th>Menü<sup>1</sup></th>
        <th width="10%">Preis<sup>1</sup></th>
        <th width="20%">Restaurant</th>
      </tr>
    </thead>
    <tr v-for="(menu, index) in menuList" :key="index">
      <td>
        {{ menu.date }}
      </td>
      <td>
        <h3>{{ menu.name }}</h3>
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
  <div><sup>1</sup>Alle Angaben ohne Gewähr! Die Daten wurden automatisch von den Webseiten ausgelesen.</div>
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

<style>
table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
  vertical-align: top;
}

tr:nth-child(even) {
  background-color: #212121;
}

tr:nth-child(odd) {
  background-color: #333333;
}
</style>
