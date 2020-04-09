import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
// 所有数据存放的地方，其他vue文件中使用数据都需引用
export default new Vuex.Store({
  state: {
	count: 0 
  },
  // 执行方法
  mutations: {
	countadd (state){
		state.count++
	}
  },
  actions: {
  },
  modules: {
  }
})
