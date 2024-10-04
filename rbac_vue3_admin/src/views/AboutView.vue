<template>

    <el-button type="primary" @click="handleLogin">Login</el-button>
    <el-button type="success" @click="handleUserList">UserList</el-button>

</template>


<script setup>

import requestUtil from '@/utils/request'

const handleLogin = async()=>{
  let result = await requestUtil.get("user/jwt_test")
  let data = result.data;
  if( data.code == 200 ){
    const token = data.token
    console.log("login successfully, token ="+token)
    window.sessionStorage.setItem("token",token)
  }else{
    console.log("login FAILED")
  }
}

const handleUserList = async()=>{
  let result = await requestUtil.get("user/test")
  let data = result.data;
  if (data.code==200){
    const userlist = data.data;
    console.log("使用者列表 UserList="+userlist)
  }else{
    console.log("FAILED")
  }
}

</script>
