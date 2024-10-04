<template>
    <el-form ref="userRef" :model="form" :rules="rules" label-width="100px" >
        <el-form-item label="手機號碼：" prop="phonenumber">
            <el-input v-model="form.phonenumber" maxlength="11" />
        </el-form-item>
        <el-form-item label="電子郵件：" prop="email">
            <el-input v-model="form.email" maxlength="50"/>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="handleSubmit">儲存</el-button>
        </el-form-item>
   </el-form>
</template>
    
<script setup>
import { ref,defineProps} from "vue"
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

const form=ref({
  id:-1,
  phonenumber:'',
  email:''
})

const userRef=ref(null)

const rules = ref({
  email: [{ required: true, message: "電子郵件不得為空", trigger: "blur" }, { type: "email", message: "請輸入正確的電子郵件", trigger: ["blur", "change"] }],
  phonenumber: [{ required: true, message: "手機號碼不得為空", trigger: "blur" }, { pattern: /\d{8}$/, message: "請輸入正確的手機號碼", trigger: "blur" }],
});

form.value=props.cuser;

const handleSubmit = () => {
  userRef.value.validate(async (valid) => {
    if(valid) {
        let result = await requestUtil.post("user/save", form.value);
        let data = result.data;
        if (data.code == 200) {
            ElMessage.success("儲存成功")
            window.sessionStorage.setItem("currentUser",JSON.stringify(form.value))
        }
        else{
          ElMessage.error(data)
        }
    }
  })
}
</script>
    

<style lang="scss" scoped>
    
</style>