<template>
    <div>this page is axios_cookie.vue 
        <hr>
        {{datalistimg}}
        {{datalistname}}
        <ul>
            <li v-for="data in 19" :key="data">
                {{data}}
                <!-- <img src:222> -->
            </li>
        </ul>
        
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return{
             datalistimg : "",
             datalistname : ""
        }
    },
    mounted() {
        axios.get("/ajax/mostExpected?ci=55&limit=10&offset=0&token=").then(res=>{
            console.log(res.data);
            console.log("猫眼");
            console.log(res.data.coming.length) 
            // this.datalistimg = (res.data.coming[0].img)
            // this.datalistname = 
        })
    },
    
}
</script>

<style lang="scss" scoped>
    div{
       background-color: violet;
    }
</style>


