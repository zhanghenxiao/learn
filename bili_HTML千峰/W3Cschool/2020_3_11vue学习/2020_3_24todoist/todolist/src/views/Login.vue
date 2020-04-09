<template>
  <div class="login">122223341324
    <h1>This is an login page</h1>
	<button type="button" @click="add()">添加</button>
  </div>
</template>

<script>
// 引用store，并且在方法中载入store ，若其他vue文件中使用数据都需引用
import store from "@/store" 
export default {
	name: 'login',
	store,
	methods: {
		add(){
			console.log('add pass')
			// 提交数据至store中，然后state存放数据
			store.commit('countadd')
		}
	}
}
</script>

<style>
</style>
