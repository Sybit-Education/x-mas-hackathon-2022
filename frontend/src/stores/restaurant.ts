import type { Restaurant } from "@/interfaces/Restaurant";
import { RestaurantService } from "@/services/restaurant.service";
import { defineStore } from "pinia";

export const useRestaurantStore = defineStore("restaurant", {
  state: () => ({
    restaurants: [] as Array<Restaurant>,
  }),
  getters: {
    getAll: (state) => state.restaurants,
    getById: (state) => (id: string) =>
      state.restaurants.find((restaurant: Restaurant) => restaurant.id === id),
  },
  actions: {
    async init() {
      const restaurantService = new RestaurantService()
      const list: Array<Restaurant> = await restaurantService.getList()

      list.forEach((item) => {
        const restaurant: Restaurant = {
          id: item.id,
          name: item.name,
          notes: item.notes,
          city: item.city,
          homepage: item.homepage,
          logo: item.logo,
        }
        this.restaurants.push(restaurant)
      })
    }
  }
})
