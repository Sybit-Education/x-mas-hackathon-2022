import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import './assets/main.css'
import { useRestaurantStore } from './stores/restaurant';

const app = createApp(App)

app.use(createPinia())
app.use(router)

const restaurantStore = useRestaurantStore()
restaurantStore.init()

app.mount('#app')
