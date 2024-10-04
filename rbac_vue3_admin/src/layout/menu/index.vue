<template>
    <el-menu
        active-text-color="#ffd04b"
        background-color="#6d768e"
        class="el-menu-vertical-demo"
        text-color="#fff"
        router
        :default-active="'/index'"
      >
        <el-menu-item index="/index" @click="openTab({name:'首頁',path:'/index'})">
            <el-icon><home-filled/></el-icon>
            <span>首頁</span>
        </el-menu-item>

        <el-sub-menu :index="menu.path" v-for="menu in menuList">
            <template #title>
                <el-icon><svg-icon :icon="menu.icon"/></el-icon>
                <span>{{ menu.name }}</span>
            </template>
            <el-menu-item :index="child.path" v-for="child in menu.children" @click="openTab(child)">
                <el-icon><svg-icon :icon="I=child.icon" /></el-icon>
                <span>{{ child.name }}</span>
            </el-menu-item>
        </el-sub-menu>

    </el-menu>
</template>
    
<script setup>
import { HomeFilled } from '@element-plus/icons-vue'
import store from '@/store'
const menuList = JSON.parse(sessionStorage.getItem("menuList"))

const openTab=(tab_child)=>{
    store.commit('ADD_TABS',tab_child)
}
</script>
    
<style lang="scss" scoped>
    
</style>