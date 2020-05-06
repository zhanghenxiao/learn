<template>
    <div>
        this page is detail.vue
    </div>
</template>

<script>
export default {
    mounted() {
        console.log(location.hash);  //获取路由ID
        console.log(this.$route.params.id)
    },
}
</script>

<style>

</style>