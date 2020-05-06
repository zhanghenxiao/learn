import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
import film from '@/views/film'
import nowplaying from '@/views/film/nowplaying'
import comingsoon from '@/views/film/comingsoon'
import center from '@/views/center'
import cinema from '@/views/cinema'
import detail from '@/views/detail'

Vue.use(VueRouter) //注册路由
//路由路径写好之后  都需在组件中写上路由容器 <router-view></router-view>  

const routes = [
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: Home
  // },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // },

  //先在路由文件中导入对应的组件 后再添加路径
  // 查看重定向与正常路劲写法的区别
  {
    path: '/film',
    component: film,
    children :[
      {
        path: 'nowplaying',
        component: nowplaying
      },
      {
        path: 'comingsoon',
        component: comingsoon
      },
      // 嵌套路由再次重定向
      {
        path: '',
        redirect: '/film/nowplaying'
      },
    ],

  },
  {
    path: '/center',
    component: center
  },
  {
    path: '/cinema',
    component: cinema
  },
  // 路由重定向
  // {
  //   path: '*',
  //   redirect: '/film'
  // },
  {
    // path: '/detail', 实现路由跳转
    path: '/detail/:id', //获取路由ID
    // 若匹配多级路由
    //path: '/detail/:id/:id2/:id3'
    component: detail
  },

]


const router = new VueRouter({
  routes
})

export default router
