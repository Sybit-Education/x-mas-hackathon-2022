import type { Menu } from "@/interfaces/Menu";
import { MenuService } from "@/services/menu.service";
import { defineStore } from "pinia";

export const useMenuStore = defineStore("menu", {
  state: () => ({
    menus: [] as Array<Menu>,
  }),
  getters: {
    getAll: (state) => state.menus
  },
  actions: {
    async init() {
      const restaurantService = new MenuService()
      const list: Array<Menu> = await restaurantService.getList()

      list.forEach((item) => {
        const menu: Menu = {
          name: item.name,
          date: item.date,
          description: item.description,
          price: item.price,
          restaurant_id: item.restaurant_id
        }
        this.menus.push(menu)
      })
    }
  }
})
