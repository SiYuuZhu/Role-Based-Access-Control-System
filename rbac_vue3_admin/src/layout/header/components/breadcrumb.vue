<template>
    <el-icon><HomeFilled /></el-icon>&nbsp;
  <el-breadcrumb :separator-icon="ArrowRight">
    <el-breadcrumb-item v-for="(item,index) in breadcrumbList">{{ item.name }}</el-breadcrumb-item>
  </el-breadcrumb>
</template>

<script setup>
import { ArrowRight,HomeFilled } from '@element-plus/icons-vue'
import { ref,watch } from 'vue'
import { useRoute } from 'vue-router'


const route = useRoute()

const breadcrumbList = ref([])

const init_breadcrumbList=()=>{
    breadcrumbList.value = route.matched
}

init_breadcrumbList()

watch(route, ()=>{
    init_breadcrumbList()
  },{deep:true, immediate:true})



</script>

<style lang="scss" scoped>

</style>