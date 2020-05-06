<template>
  <div>
      this page is appvue
    <p>{{mytext}}</p>
    <input type="text" v-model="mytext">
    <button @click="addclick()">add</button>
    <ul>
      <li v-for="data in datalist" :key="data">{{data}}</li>
    </ul>

    <!-- 组件的使用 -->
    <child1 myname="来自父组件的问候">
      <div>
        slot演示
      </div>
      <div>1111</div>
    </child1>

    <!-- 把路由加载到权限最高的组件上 -->
    <tabber></tabber>
    <!-- 路由容器 -->
    <router-view></router-view>  

  </div>
</template>


<script>
// import Vue from 'vue'
// 导入组件路径 并注册组件才能使用
import child1 from '@/components/child1'
import tabber from '@/components/tabber'
	export default {
		data() {
			return {
        mytext: '111',
        datalist: []
			}
    },
    methods: {
      addclick(){
        console.log(this.mytext)
        this.datalist.push(this.mytext)
        console.log(this.datalist)
      }
    },
    // 局部注册无需导入vue
    //全局注册需导入 18 行import Vue from 'vue'
    components:{
      child1,
      tabber
    }
	}
</script>

<style lang="css" scoped>
    li{
      list-style: none;
    }
    p{
      background-color: red;
    }
</style>                                                                                                               