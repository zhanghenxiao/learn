<template>
    <div>
        this is tabber.vue page
        <!-- 声明式导航 高亮显示 -->
        <ul>
            <router-link to="/film" tag="li" activeClass="active">电影</router-link>
            <router-link to="/center" tag="li" activeClass="active">我的</router-link>
            <router-link to="/cinema" tag="li" activeClass="active">影院</router-link>
        </ul>
    </div>
</template>
<style lang="scss" scoped>
    .active{
        color: red;
    }
    div{
        position: fixed;  // 定位于相对于浏览器窗口的指定坐标，。此元素的位置可通过 "left"、"top"、"right" 以及"bottom" 属性来规定。不论窗口滚动与否，元素都会留在那个位置
        bottom: 5px;   //离底部的位置为 5px
        left: 0px;  // 将这个div 放置底部 
        height: 50px;
        width: 100%;
        background-color: white;
        ul{
            display: flex;  //"弹性布局"，用来为盒状模型提供最大的灵活性。
            li{
                flex:1;
                text-align: center;
                
            }
        }
    }
</style>
