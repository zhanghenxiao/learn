import Vue from 'vue'
import App from './App.vue'
import Vuex from 'vuex'

Vue.config.productionTip = false
// 使用
Vue.use(Vuex) 
const store = new Vuex.Store({
	state:{
		count : 0,
		name : "cookie"
	},
	//修改方法
	mutations:{
		countadd(state){
			state.count++
		}
	}
})

new Vue({
	// 引用挂载在Vue上
	store,
  render: h => h(App),
}).$mount('#app')
