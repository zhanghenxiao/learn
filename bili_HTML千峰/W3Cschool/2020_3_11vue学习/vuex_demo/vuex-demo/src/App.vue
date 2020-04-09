<!-- 禁止使用 空格 和 tab 混合缩进 (no-mixed-spaces-and-tabs) -->
<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->
	<h1> name : {{this.$store.state.name}}</h1>
	<h1> count: {{this.$store.state.count}}</h1>
	<h1>count:{{count}}</h1>
	<p @click="countadd()">点我自增</p>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
export default {
  name: 'App',
  // components: {
  //   HelloWorld
  // }
  computed:{
	count(){
		return this.$store.state.count
	}
  },
  // commit 参数对应的是 store实列中的方法
  methods:{
	countadd(){  
		this.$store.commit('countadd')
	}
  }	
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
