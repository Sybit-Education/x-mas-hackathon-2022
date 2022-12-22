import type { Menu } from "@/interfaces/Menu"
import api from "./api"

export class MenuService {
  async getList(): Array<Menu> {
    const response = await api.restClient().get(`/lunch`)
    if (response.status === 200) {
      return response.data
    }
    console.error(response)
  }
}
