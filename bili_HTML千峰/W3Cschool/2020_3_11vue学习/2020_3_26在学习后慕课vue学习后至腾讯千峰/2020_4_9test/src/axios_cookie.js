import Vue from 'vue'
import axios_cookie from '@/components/axios_cookie.vue'
import router from './router'
import store from '@/store'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(axios_cookie)
}).$mount('#axios_cookie')