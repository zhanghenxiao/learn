<template>
    <div>
        child1 -- {{myname}}
        <slot></slot>
        <slot></slot>
    </div>
</template>

<script>
export default {
    // 组件间的通信
    props:["myname"]
}
</script>

<style scoped>

</style>

<style lang="css" scoped>
    div{
    background-color: yellow 
}
</style>