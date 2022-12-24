import type { Restaurant } from "@/interfaces/Restaurant"
import { Api } from "./api"

export class RestaurantService extends Api {
  async getList(): Promise<Restaurant[]> {
    const response = await this.restClient().get(`/restaurant`)
    if (response.status === 200) {
      return response.data
    }
    console.error(response)
    return [] as Array<Restaurant>
  }
}
