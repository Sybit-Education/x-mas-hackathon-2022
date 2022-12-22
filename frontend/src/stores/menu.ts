import type { Menu } from "@/interfaces/Menu";
import { MenuService } from "@/services/menu.service";
import { defineStore } from "pinia";

export const useMenuStore = defineStore("meun", {
  state: () => ({
    menus: [] as Array<Menu>,
  }),
  getters: {
    getAll: (state) => state.menus,
    getById: (state) => (id: string) =>
      state.menus.find((restaurant: Menu) => restaurant.id === id),
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
          price: item.price
        }
        this.menus.push(menu)
      })
    }
  }
})
