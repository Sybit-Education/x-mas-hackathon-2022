import type { Restaurant } from "@/interfaces/Restaurant"
import api from "./api"

export class RestaurantService {
  async getList(): Array<Restaurant> {
    const response = await api.restClient().get(`/restaurant`)
    if (response.status === 200) {
      return response.data
    }
    console.error(response)
  }
}
