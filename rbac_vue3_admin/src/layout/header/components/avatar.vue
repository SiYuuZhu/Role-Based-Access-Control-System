<template>
    <el-dropdown>
    <span class="el-dropdown-link">
      <el-avatar :size="45" :src="circleUrl" />
      &nbsp;&nbsp; {{currentUser.username}}
      <el-icon class="el-icon--right">
        <arrow-down/>
      </el-icon>

    </span>
    <template #dropdown>
      <el-dropdown-menu>
        <el-dropdown-item>
          <router-link :to="{name:'帳號中心'}">
          &nbsp;
          <el-icon><Compass /></el-icon>帳號中心
          &nbsp;&nbsp;
          </router-link>
        </el-dropdown-item>
        <el-dropdown-item @click="logout">
          &nbsp;&nbsp;
          <el-icon><SwitchButton /></el-icon>登出
          &nbsp;&nbsp;
        </el-dropdown-item>
      </el-dropdown-menu>
    </template>
  </el-dropdown>
</template>


<script setup>
import { ArrowDown, Compass, SwitchButton } from '@element-plus/icons-vue'
import { getServerUrl } from '@/utils/request'
import router from '@/router'
import store from '@/store';

const currentUser = JSON.parse(sessionStorage.getItem("currentUser"))
const circleUrl = getServerUrl() + 'media/userAvatar/' + currentUser.avatar

const logout=()=>{
    window.sessionStorage.clear()
    router.replace("/login")
    store.commit('RESET_TAB')
}
</script>


<style lang="scss" scoped>
.el-dropdown-link {
  cursor: pointer;
  color: #277da1;
  display: flex;
  align-items: center;
}
</style>

