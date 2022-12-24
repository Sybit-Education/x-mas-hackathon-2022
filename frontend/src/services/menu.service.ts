import type { Menu } from "@/interfaces/Menu"
import { Api } from './api'

export class MenuService extends Api {
  async getList(): Promise<Menu[]> {
    const response = await this.restClient().get(`/lunch`)
    if (response.status === 200) {
      return response.data
    }
    console.error(response)
    return [] as Array<Menu>
  }
}
