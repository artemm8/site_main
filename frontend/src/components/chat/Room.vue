<template lang="">
    <div >
        <div v-for="room in rooms"> 
            <h3>{{room.name}}</h3>
                <p>{{room.date}}</p>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
     data(){
        return {
           
           rooms:""
        }
    },
    methods: {
        loadRoom(){
            axios({
                url:"http://127.0.0.1:8000/chat/room/",
                method:"get"
            }).then(response=>{
                console.log(response.data.data)
                this.rooms=response.data.data
            }).catch(error=>{
                console.log(error)
            })
        }
    },
    // сreated это метод который сразу с рабатывает при загрузки страницы
    created() {
        axios.defaults.headers["authorization"]="Token "+sessionStorage.getItem("authtoken")
        this.loadRoom()
    },
}
</script>
<style lang="">
    
</style>