<template>
  <div>
    <h1>This is film page</h1>
    一级路由 
      嵌套路由
      <div>film 轮播组件</div>
      <!-- 路由容器 -->
        <filmtabber></filmtabber>
        <div>
          <router-view></router-view>
        </div>
        
      <!-- <div>正在热映</div>
      <div>即将上映 </div> -->
      <!-- <nowplaying></nowplaying>
      <comingsoon></comingsoon>  -->
  </div>
</template>

<script>
// import nowplaying from './views/film/nowplaying'
// import comingsoon from './views/film/comingsoon'
import filmtabber from './film/filmtabber'
export default {
  components:{
    // nowplaying,
    // comingsoon
    filmtabber
  },
}

</script>
<style>

</style>