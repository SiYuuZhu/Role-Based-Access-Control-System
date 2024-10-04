<template>
    <div class="app-container">

        <el-row :gutter="20" class="header">
            <el-col :span="7">
                <el-input placeholder="請輸入欲查詢的使用者名稱" v-model="queryForm.query" clearable ></el-input>
            </el-col>
            <el-button type="primary" :icon="Search" @click="initUserList" round>查詢</el-button>
            <el-button type="success" :icon="DocumentAdd" @click="handleDialogValue()" round>新增</el-button>
            <el-popconfirm title="您確定要刪除這些使用者？" @confirm="handleDelete(null)">
                <template #reference>
                    <el-button type="danger" :disabled="delBtnStatus" :icon="Delete" round>批量刪除</el-button>
                </template>
            </el-popconfirm>
        </el-row>

        <el-table
            :data="tableData"
            stripe
            style="width: 100%"
            @selection-change="handleSelectionChange"
        >
            <el-table-column type="selection" width="55" />
            <el-table-column prop="avatar" label="頭像" width="80" align="center">
                <template v-slot="scope">
                    <img :src="getServerUrl()+'media/userAvatar/'+scope.row.avatar" width="50" height="50"/>
                </template>
            </el-table-column>
            <el-table-column prop="username" label="使用者名稱" width="100" align="center"/>
            <el-table-column prop="roles" label="角色列表" width="200" align="center">
                <template v-slot="scope">
                    <el-tag size="small" type="warning" v-for="item in scope.row.roleList">   {{item.name}}</el-tag>
                </template>
            </el-table-column>
            <el-table-column prop="email" label="電子信箱" width="150" align="center"/>
            <el-table-column prop="phonenumber" label="手機" width="120" align="center"/>
            <el-table-column prop="status" label="帳號狀態" width="200" align="center" >
                <template v-slot="{row}" >
                    <el-switch  v-model="row.status"  @change="statusChangeHandle(row)" active-text="正常"
                                inactive-text="停用" :active-value="1" :inactive-value="0"></el-switch>
                </template>
            </el-table-column>
            <el-table-column prop="create_time" label="創建時間" width="200" align="center"/>
            <el-table-column prop="login_date" label="最後登入時間" width="200" align="center"/>
            <el-table-column prop="remark" label="備註"  />

            <el-table-column prop="action" label="操作" width="380" fixed="right" align="left">
                <template v-slot="scope" >
                    <el-button  type="warning" :icon="Tools" @click="handleRoleDialogValue(scope.row.id,scope.row.roleList)" round>分配角色</el-button>
                    <el-popconfirm  v-if="scope.row.username!='yuuu'" title="您確定對該使用者重置密碼嗎?" @confirm="handleResetPassword(scope.row.id)">
                        <template #reference>
                            <el-button  type="primary" :icon="RefreshRight" round>密碼重置</el-button>
                        </template>
                    </el-popconfirm>
                    <el-button type="primary" v-if="scope.row.username!='yuuu'" :icon="Edit" @click="handleDialogValue(scope.row.id)" round></el-button>
                    <el-popconfirm  v-if="scope.row.username!='yuuu'" title="您確定要刪除該使用者?" @confirm="handleDelete(scope.row.id)">
                        <template #reference>
                        <el-button  type="danger" :icon="Delete" round/>
                        </template>
                    </el-popconfirm>
                </template>
            </el-table-column>
        </el-table>
        <el-pagination
            v-model:current-page="queryForm.pageNum"
            v-model:page-size="queryForm.pageSize"
            :page-sizes="[10, 20, 30, 40]"
            layout="total, sizes, prev, pager, next, jumper"
            :total="total"
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
        />

        <Dialog v-model="dialogVisible" :dialogVisible="dialogVisible" :id="id" :dialogTitle="dialogTitle" @initUserList="initUserList"></Dialog>
        <RoleDialog v-model="roleDialogVisible" :sysRoleList="sysRoleList" :roleDialogVisible="roleDialogVisible" :id="id" @initUserList="initUserList"></RoleDialog>
    </div>
</template>


<script setup>
import { ref } from 'vue'
import requestUtil,{ getServerUrl } from "@/utils/request"
import { Search , Delete, DocumentAdd, Edit, Tools, RefreshRight} from '@element-plus/icons-vue'
import Dialog from './components/dialog.vue'
import RoleDialog from './components/roleDialog.vue'
import { ElMessage } from 'element-plus'

const dialogVisible=ref(false)
const dialogTitle=ref("")
const id=ref(-1)

const handleDialogValue=(userId)=>{
  if(userId){
    id.value = userId;
    dialogTitle.value = "使用者修改"
  }else {
    id.value=-1;
    dialogTitle.value = "使用者新增"
  }
  dialogVisible.value = true
}

const delBtnStatus=ref(true)
const multipleSelection = ref([])
const handleSelectionChange = (selection)=>{
    console.log("selected")
    console.log(selection)
    multipleSelection.value = selection
    delBtnStatus.value = selection.length == 0
}

const handleDelete=async (id)=>{
  var ids = []
  if(id){
    ids.push(id)
  }else{
    multipleSelection.value.forEach(row=>{
      ids.push(row.id)
    })
  }
  const res=await requestUtil.del("user/action",ids)
  if(res.data.code==200){
    ElMessage({
      type: 'success',
      message: '已成功刪除!'
    })
    initUserList();
  }else{
    ElMessage({
      type: 'error',
      message: res.data.info,
    })
  }
}


const sysRoleList = ref([])
const roleDialogVisible = ref(false)
const handleRoleDialogValue=(userId,roleList)=>{
    console.log("roleList:",roleList)
    console.log("id:",id)
    id.value=userId;
    sysRoleList.value=roleList;
    roleDialogVisible.value=true
}

const handleResetPassword = async (id)=>{
  const res=await requestUtil.get("user/resetPassword?id="+id)
  if(res.data.code==200){
    ElMessage({
      type: 'success',
      message: '該使用者密碼已重置'
    })
    initUserList();
  }else{
    ElMessage({
      type: 'error',
      message: res.data.info,
    })
  }
}

const statusChangeHandle = async (row)=>{
  let res=await requestUtil.post("user/status",{id:row.id,status:row.status});
  if(res.data.code==200){
    ElMessage({
      type: 'success',
      message: '該使用者帳號狀態已更新'
    })
  }else{
    ElMessage({
      type: 'error',
      message: res.data.info,
    })
    initUserList();
  }
}

const tableData = ref([])

const total = ref([])
const queryForm = ref({
    query:'',
    pageNum:1,
    pageSize:10
})

const initUserList = async ()=>{
    const res = await requestUtil.post("user/search",queryForm.value)
    tableData.value = res.data.userList
    total.value = res.data.total
}

const handleSizeChange = (pageSize)=>{
    queryForm.value.pageSize = pageSize
    queryForm.value.pageNum = 1
    initUserList()
}

const handleCurrentChange = (pageNum)=>{
    queryForm.value.pageNum = pageNum
    initUserList()
}

initUserList()

</script>


<style lang="scss" scoped>
.header{
  padding-bottom: 16px;
  box-sizing: border-box;
}

.el-pagination{
  float: right;
  padding: 20px;
  box-sizing: border-box;
}

::v-deep th.el-table__cell{
  word-break: break-word;
  background-color: #f8f8f9 !important;
  color: #515a6e;
  height: 40px;
  font-size: 13px;

}

.el-tag--small {
  margin-left: 5px;
}
</style>