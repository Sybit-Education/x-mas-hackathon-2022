<template>
  <div id="home-view">
    <lunch-list />

    <hr />

    <h3>Dein Lieblingsrestaurant fehlt?</h3>

    <p>
      Dann implementiere einen Crawler für dein Lieblingsrestaurant und mache einen PR!
      <br />
      Weitere Infos in der
      <a
        href="https://github.com/Sybit-Education/x-mas-hackathon-2022/blob/main/backend/README.md#neuen-crawler-implementieren"
      >
        README
      </a>
    </p>
  </div>
</template>

<script setup lang="ts">
import LunchList from '@/components/LunchList.vue'
</script>

<style>
hr {
  margin-top: 1rem;
  margin-bottom: 1rem;
}
</style>
