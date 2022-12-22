<script lang="ts">
import type {Restaurant} from "@/interfaces/Restaurant";
import type {Menu} from "@/interfaces/Menu";

export default {
  data() {
    return {
      restaurants: [] as Restaurant[],
      menus: [] as Menu[]
    };
  },
  created() {
    fetch('http://127.0.0.1:5000/v1/restaurant').then(async response => {
          this.restaurants = await response.json() as Restaurant[];
        }, error => {
          console.log(error)
        }
    ),
    fetch('http://127.0.0.1:5000/v1/lunch').then(async response => {
          this.menus = await response.json() as Menu[];
          for(let m in this.menus) {
            for(let r in this.restaurants) {
              console.log(r.id);
              if (m.restaurant_id === r.id) {
                m.restaurant_id = r.name;
                break;
              }
            }
          }
        }, error => {
          console.log(error)
        }
    )
  },
}
</script>

<template>
  <li v-for="m in menus">
    <div class="grid-container">
      <div class="restaurant">{{ m.restaurant_id}}</div>
      <div class="name">{{ m.name }}</div>
      <div class="desc">{{ m.description }}</div>
      <div class="price">{{ m.price}}€</div>
    </div>
  </li>
</template>

<style scoped>
.grid-container {
  display: grid;
  grid-template-columns: auto auto auto;
  padding-top: 20px;
}

.restaurant {
  color: #b51783;
  font-size: 20px;
}

.link {
  color: #3ca2ef;
  font-size: 20px;
}
.desc {
  font-size: 25px;
}
</style>