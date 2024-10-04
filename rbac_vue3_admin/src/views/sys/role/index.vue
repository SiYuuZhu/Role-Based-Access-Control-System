<template>
    <div class="app-container">
        <el-row :gutter="20" class="header">
            <el-col :span="6">
                <el-input placeholder="請輸入欲查詢的角色名稱" v-model="queryForm.query" clearable ></el-input>
            </el-col>
            <el-button type="primary" :icon="Search" @click="initRoleList" round>查詢</el-button>
            <el-button type="success" :icon="DocumentAdd" @click="handleDialogValue()" round>新增</el-button>
            <el-popconfirm title="確定要批量刪除這些角色嗎？" @confirm="handleDelete(null)">
                <template #reference>
                    <el-button type="danger" :disabled="delBtnStatus" :icon="Delete" round>批量删除</el-button>
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
                <el-table-column prop="name" label="角色名稱" width="150" align="center"/>
                <el-table-column prop="code" label="權限代稱" width="150" align="center"/>
                <el-table-column prop="create_time" label="創建時間" width="150" align="center"/>
                <el-table-column prop="remark" label="備註"  />
                <el-table-column prop="action" label="操作" width="300" fixed="right" align="left">
                <template v-slot="scope" >
                    <el-button  type="warning" :icon="Tools" @click="handleMenuDialogValue(scope.row.id)" round>分配權限</el-button>
        
                    <el-button v-if="scope.row.code!='admin'" type="primary" :icon="Edit" @click="handleDialogValue(scope.row.id)" round/>
        
                    <el-popconfirm  v-if="scope.row.code!='admin'" title="您確定要刪除此角色嗎？" @confirm="handleDelete(scope.row.id)">
                        <template #reference>
                        <el-button  type="danger" :icon="Delete" round/>
                        </template>
                    </el-popconfirm>
        
                </template>
            </el-table-column>
        </el-table>
        <el-pagination
            v-model:currentPage="queryForm.pageNum"
            v-model:page-size="queryForm.pageSize"
            :page-sizes="[10, 20, 30, 40,50]"
            layout="total, sizes, prev, pager, next, jumper"
            :total="total"
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
        />
    </div>
    <Dialog v-model="dialogVisible" :dialogVisible="dialogVisible" :id="id" :dialogTitle="dialogTitle" @initRoleList="initRoleList" ></Dialog>
    <MenuDialog v-model="menuDialogVisible" :menuDialogVisible="menuDialogVisible" :id="id"  @initRoleList="initRoleList"></MenuDialog>
</template>



<script setup>
import { Search ,Delete,DocumentAdd ,Edit, Tools} from '@element-plus/icons-vue'
import { ref } from 'vue'
import requestUtil from "@/utils/request";
import { ElMessage } from 'element-plus'
import Dialog from './components/dialog'
import MenuDialog from './components/menuDialog'

const queryForm=ref({
    query:'',
    pageNum:1,
    pageSize:10
})

const total=ref(0)

const tableData = ref([])

const id=ref(-1)

const dialogVisible=ref(false)

const menuDialogVisible=ref(false)

const dialogTitle=ref('')

const multipleSelection=ref([])

const delBtnStatus=ref(true)

const handleSelectionChange=(selection)=>{
    console.log("已勾選")
    console.log(selection)
    multipleSelection.value = selection;
    delBtnStatus.value = selection.length == 0;
}


const initRoleList=async()=>{
    const res=await requestUtil.post("role/search",queryForm.value)
    tableData.value=res.data.roleList;
    total.value=res.data.total;
}


initRoleList();

const handleSizeChange=(pageSize)=>{
    queryForm.value.pageNum=1;
    queryForm.value.pageSize=pageSize;
    initRoleList();
}

const handleCurrentChange=(pageNum)=>{
    queryForm.value.pageNum=pageNum;
    initRoleList();
}

const handleDialogValue=(roleId)=>{
    if(roleId){
        id.value=roleId;
        dialogTitle.value="修改角色"
    }else{
        id.value=-1;
        dialogTitle.value="新增角色"
    }
    dialogVisible.value=true
}


const handleMenuDialogValue=(roleId)=>{
    if(roleId){
        id.value=roleId;
    }
    menuDialogVisible.value=true
}

const handleDelete = async (id)=>{
    var ids = []
    if(id){
        ids.push(id)
    }else{
        multipleSelection.value.forEach(row=>{
        ids.push(row.id)
        })
    }
    const res=await requestUtil.del("role/action",ids)
    if(res.data.code==200){
        ElMessage({
            type: 'success',
            message: '刪除成功'
        })
        initRoleList();
    }else{
        ElMessage({
            type: 'error',
            message: res.data.info,
        })
    }
}

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
