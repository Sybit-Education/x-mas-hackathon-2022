<template>
  <table>
    <tr v-for="menu in menuList">
      <td>
        {{  menu.restaurant_id }}
      </td>
      <td>
        <h5>{{ menu.name }}</h5>
      </td>
      <td>
      </td>
    </tr>
  </table>
</template>
<script lang="ts">
import { mapState } from 'pinia';
import { useMenuStore } from '../stores/menu';

export default {
  name: 'LunchList',
  computed: {
    ...mapState(useMenuStore, {
      menuList: (store) => store.getAll
    }),
  },
}
</script>