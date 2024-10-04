<template>
    <div class="app-container">
        <el-row :gutter="20">
            <el-col :span="8">
                <el-card class="box-card">
                    <template v-slot:header>
                        <div class="clearfix">
                        <span>帳戶資訊</span>
                        </div>
                    </template>
                    <div>
                        <div class="text-center">
                            <avatar :cuser="currentUser"/>
                        </div>
                        <ul class="list-group list-group-striped">
                            <li class="list-group-item">
                                <svg-icon icon="user" />&nbsp;&nbsp;使用者名稱
                                <div class="pull-right">{{currentUser.username}}</div>
                            </li>
                            <li class="list-group-item">
                                <svg-icon icon="phone" />&nbsp;&nbsp;手機號碼
                                <div class="pull-right">{{currentUser.phonenumber}}</div>
                            </li>
                            <li class="list-group-item">
                                <svg-icon icon="email" />&nbsp;&nbsp;電子郵件
                                <div class="pull-right">{{currentUser.email}}</div>
                            </li>
                            <li class="list-group-item">
                                <svg-icon icon="peoples" />&nbsp;&nbsp;所屬角色
                                <div class="pull-right">{{currentUser.roles}}</div>
                            </li>
                            <li class="list-group-item">
                                <svg-icon icon="date" />&nbsp;&nbsp;創建時間
                                <div class="pull-right">{{currentUser.create_time}}</div>
                            </li>
                        </ul>
                    </div>
                </el-card>
            </el-col>
            <el-col :span="16">
                <el-card>
                    <template v-slot:header>
                        <div class="clearfix">
                        <span>基本資料</span>
                        </div>
                    </template>
                    <el-tabs v-model="activeTab">
                        <el-tab-pane label="基本資料管理" name="userinfo">
                            <userInfo :cuser="currentUser"/>
                        </el-tab-pane>
                        <el-tab-pane label="修改密碼" name="resetPwd">
                            <resetPwd :cuser="currentUser"/>
                        </el-tab-pane>
                    </el-tabs>
                </el-card>
            </el-col>
        </el-row>
    </div>

</template>
    
<script setup>
import { ref } from 'vue'
import avatar from './components/avatar.vue'
import userInfo from './components/userInfo.vue'
import resetPwd from './components/resetPwd.vue'


const currentUser = JSON.parse(sessionStorage.getItem("currentUser"))
const activeTab = ref("userinfo")
</script>

    
<style lang="scss" scoped>
.list-group-striped > .list-group-item {
    border-left:0;
    border-right:0;
    border-radius:0;
    padding-left:0;
    padding-right:0;
}

.list-group-item{
    border-bottom:1px solid #e7eaec;
    border-top:1px solid #e7eaec;
    margin-bottom:-1px;
    padding:11px 0;
    font-size:13px;
}

.pull-right{
    float:right !important;
}

::v-deep .el-card__body{
    height:230px;
}

::v-deep .box-card{
    height:450px;
}

</style>