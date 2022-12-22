<template>
<li v-for="lunch in lunches">
 <div class="grid-container">
    <div class="restaurant">{{lunch.restaurant_id}}</div>
    <div class="name">{{lunch.name}}</div>
    <div class="desc">{{lunch.description}}</div>
    <div class="price">{{lunch.price}}€</div>
    <div class="desc"></div>
  </div>
</li>
  <div>
    {{ lunches }}
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return{
      lunches: Array<{}>
    }
  },
  created() {
    fetch(':5000/v1/lunch').then(response => {
      let raw:{} = JSON.stringify(response)
      let lunches: Array<{}> = new Array<{}>();
      for(let rawData in raw){
        let restaurant_id = rawData.restaurant_id;
            let date = rawData.date;
            let name = rawData.name;
            let description = rawData.description;
            let price = rawData.price;
        lunches.push({restaurant_id:restaurant_id,date:date,name:name,description:description,price:price});
      }
      this.lunches = lunches;

        }, error => {
      console.log(error)
    }
    )
  },
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