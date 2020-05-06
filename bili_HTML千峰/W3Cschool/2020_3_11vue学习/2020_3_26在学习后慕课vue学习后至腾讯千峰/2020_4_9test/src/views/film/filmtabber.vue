<template>
    <div>
        this is tabber.vue page
        <!-- 声明式导航 高亮显示 -->
        <ul>
            <!-- 嵌套路由不要 ./ -->
            <router-link to="/film/nowplaying" tag="li" activeClass="active">正在上映</router-link>
            <router-link to="/film/comingsoon" tag="li" activeClass="active">即将上映</router-link>
        </ul>
    </div>
</template>
<style lang="scss" scoped>
    .active{
        color: red;
        border-bottom: 5px solid tan;
    }
</style>
