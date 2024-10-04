<template>
    <el-form ref="pwdRef" :model="form" :rules="rules" label-width="80px">
        <el-form-item label="原密碼" prop="oldPassword">
            <el-input v-model="form.oldPassword" placeholder="請輸入原密碼" type="password" show-password/>
        </el-form-item>
        <el-form-item label="新密碼" prop="newPassword">
            <el-input v-model="form.newPassword" placeholder="請輸入新密碼" type="password" show-password/>
        </el-form-item>
        <el-form-item label="確認密碼" prop="confirmPassword">
            <el-input v-model="form.confirmPassword" placeholder="再次確認新密碼" type="password" show-password/>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="handleSubmit">儲存</el-button>
        </el-form-item>
    </el-form>
</template>
  

<script setup>
import { defineProps, ref } from "vue";
import requestUtil from "@/utils/request";
import { ElMessage } from 'element-plus'

const props=defineProps(
    {
        cuser:{
            type:Object,
            default:()=>{},
            required:true
        }
    }
)

const form = ref({
    id:-1,
    oldPassword:'',
    newPassword:'',
    confirmPassword:''
})

const pwdRef=ref(null)

form.value=props.cuser;

const equalToPassword = (rule, value, callback) => {
    if (form.value.newPassword !== value) {
        callback(new Error("兩次輸入密碼不一致"));
    }
    else {
        callback();
    }
};

const rules = ref({
    oldPassword: [{ required: true, message: "請輸入原密碼", trigger: "blur" }],
    newPassword: [{ required: true, message: "新密碼不得為空", trigger: "blur" }, { min: 6, max: 20, message: "長度限6~20字元", trigger: "blur" }],
    confirmPassword: [{ required: true, message: "請確認新密碼", trigger: "blur" }, { required: true, validator: equalToPassword, trigger: "blur" }]
});


const handleSubmit = () => {
    pwdRef.value.validate(async (valid)=>{
        if (valid) {
        let result = await requestUtil.post("user/updateUserPwd", form.value);
        let data = result.data;
        if (data.code == 200) {
            ElMessage.success(data.info)
        }else{
            ElMessage.error(data.info)
        }
        }
    })
}

</script>


<style scoped>

</style>
