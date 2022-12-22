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

<script lang="ts">
export default {
  data() {
    return {
      
      lunch: {
        id: String,
        createdTime: String,
        fields: Array<{ 
          date: Date,
          restaurant: String,
          name: String,
          description: String,
          Price: GLfloat
        }>
      }
    }
  },
  created() {
    fetch('http:127.0.0.1:5000/v1/lunch').then(response => {
      this.lunch = response
    }, error => {
      console.log(error)
    }
    )
    console.log(this.lunch)
  }
}
</script>

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