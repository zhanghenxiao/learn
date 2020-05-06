<template>
    <div>
        this is nowplaying.vue  page
        <ul>
            <li v-for="data in datalist" :key="data" @click="headclick(data)">
                {{data}}
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    data() {
        return {
            datalist:["111","222","333"]
        }
    },
    methods: {
        headclick(id){
            // 路由跳转 ---编程式导航
          this.$router.push('/detail') // 匹配/detail路由然后跳转
          this.$router.push(`/detail/${id}`) // 匹配/detail路由然后跳转

        }
    },
}
</script>

<style>

</style>