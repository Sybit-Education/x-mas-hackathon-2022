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
    {{ raw }}
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      lunches: {
        restaurant_id: String,
        date: Date,
        name: String,
        description: String,
        price: parseFloat
      }=[]
    }
  },
  created() {
    fetch(':5000/v1/lunch').then(response => { this.raw = response.json}, error => {
      console.log(error)
    }
    )
  }
  computed() {
  let lunches: lunches;
    for(rawData in raw){
        restaurant_id: rawData.restaurant_id,
        date: rawData.date,
        name: rawData.name,
        description: rawData.description,
        price: rawData.price
        lunches.add({restaurant_id,date,name,description,price})
    }
    this.lunches = lunches;
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