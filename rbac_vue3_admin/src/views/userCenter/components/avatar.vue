<template>
    <el-form
        ref="formRef"
        :model="form"
        label-width="100px"
        style="text-align: center;padding-bottom:10px"
    >
        <el-upload
            name="avatar"
            :headers="headers"
            class="avatar-uploader"
            :action="getServerUrl()+'user/uploadImage'"
            :show-file-list="false"
            :on-success="handleAvatarSuccess"
            :before-upload="beforeAvatarUpload"
        >
            <img v-if="imageUrl" :src="imageUrl" class="avatar" />
            <el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon>
        </el-upload>
        <el-button @click="handleConfirm" >更換頭像</el-button>
    </el-form>
</template>


<script setup>
import { defineProps, ref } from "vue"
import requestUtil,{ getServerUrl } from "@/utils/request"
import { ElMessage } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'


const props=defineProps(
    {
      cuser:{
        type:Object,
        default:()=>{},
        required:true
      }
    }
)

const headers=ref({
  Authorization:window.sessionStorage.getItem('token')
})

const form=ref({
  id:-1,
  avatar:''
})
const formRef=ref(null)

const imageUrl=ref("")

form.value=props.cuser;
imageUrl.value=getServerUrl()+'media/userAvatar/'+form.value.avatar

const handleAvatarSuccess = (res) => {
  imageUrl.value=getServerUrl()+'media/userAvatar/'+res.title
  form.value.avatar=res.title;
}


const beforeAvatarUpload = (file) => {
  const isJPG = file.type === 'image/jpeg'
  const isLt2M = file.size / 1024 / 1024 < 2

  if (!isJPG) {
    ElMessage.error('圖片僅限JPG格式')
  }
  if (!isLt2M) {
    ElMessage.error('圖片大小僅限2MB內')
  }
  return isJPG && isLt2M
}

const handleConfirm=async()=>{
    let result=await requestUtil.post("user/updateAvatar",form.value);
    let data=result.data;
    if (data.code==200) {
        ElMessage.success("更換頭像成功")
    } else {
        ElMessage.error(data.info);
    }
}

</script>


<style>

.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.avatar-uploader .el-upload:hover {
  border-color: #767ddd;
}

.el-icon.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  text-align: center;
}

.avatar {
  width: 120px;
  height: 120px;
  display: block;
}
</style>
