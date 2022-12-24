import axios from 'axios'

const API_PREFIX = '/v1'

export class Api {
  server!: string

  /**
   * Get the base-URL of the Service
   */
  getServer() {
    if (this.server) {
      return this.server
    }
    if (import.meta.env.VITE_APP_API_SERVER) {
      this.server = import.meta.env.VITE_APP_API_SERVER
    } else {
      this.server = window.location.origin
      if (this.server && this.server.charAt(this.server.length - 1) === '/') {
        this.server = this.server.substring(0, this.server.length - 1)
      }
    }
    console.info(`%c⚙️ Rest-Service: ${this.server}`, 'color: #5793c9')
    return this.server
  }
  getApi() {
    return this.getServer() + API_PREFIX
  }
  restClient() {
    return axios.create({
      baseURL: this.getApi(),
      timeout: 5000,
      headers: {
        'Content-Type': 'application/json'
      }
    })
  }
}
