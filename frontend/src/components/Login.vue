<!-- html -->
<template lang="">
    <div>
        <input placeholder="login" type="text" v-model="login">
                <input placeholder="password" type="text" v-model="password">
                <button @click="setLogin">войти</button>

    </div>
</template>
<!-- js -->
<script>
import axios from "axios"
export default {
    name:"Login",
    //mesta dly peremenix
    data(){
        return {
           login:"" ,
           password:"" 
        }
    },
    //места для функции
    methods: {
        setLogin(){
            //axios это метод для запросов для других сылок
            axios(
                {
                    url:"http://127.0.0.1:8000/account/token/",
                    method:"post",
                    data:{
                        username:this.login,
                        password:this.password
                    }
                }
            ).then(response=>{
                console.log(response)
                sessionStorage.setItem("authtoken",response.data.token)
            }).catch(error=>{
                console.log("не правильный логин или пароль")
            })


        }
    },


}
</script>
<!-- css -->
<style lang="">
    
</style>