<template>
    <div>
        <h5> this page is childe1.ve </h5>
        <hr>
        child1 -- {{myname}}
        <slot></slot>
        <slot> </slot>
       {{name}}
    </div>
</template>

<script>
import axios from 'axios'
export default {
    // 组件间的通信
    props:["myname"],
    mounted() {
        // https://maoyan.com/#movie/.f-hot
        axios.get("/ajax/mostExpected?ci=55&limit=10&offset=0&token=").then(res=>{
            console.log(res.data);
            console.log("猫眼");
            console.log(res.data.coming.length) 
            this.img = (res.data.coming[0].img)
        })
    },
    methods: {
        
    },

//     mounted() {
//         //代理猫眼 proxy库
//         axios.get("/j/search_tags?type=movie&source=").then(res=>{
//             console.log(res.data);)},
//         // 利用json server库 模拟数据 请求多条数据在本地 github有使用方法
//         // axios.get("/json/db.json").then(res=>{
//         //     console.log(res.data);
//         //     console.log("22")
//         // }),
//         // axios.get("/ajax/mostExpected?ci=55&limit=10&offset=0&token=").then(res=>{
//         //     console.log(res.data);
//         //     console.log("33")
//         // })
// <img src="https://p1.meituan.net/170.230/movie/fcabb91dbae511e8a32af1deeb0c1cec204154.jpg" onerror="this.style.visibility='hidden'">
            //  http://p1.meituan.net/w.h/movie/fcabb91dbae511e8a32af1deeb0c1cec204154.jpg
}
</script>

<style lang="css" scoped>
    div{
    background-color: yellow 
    }


</style>

