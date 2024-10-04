<template>
    <div class="app-container">
        <el-row  class="header">
            <el-button type="success" :icon="DocumentAdd" @click="handleDialogValue()" round>新增選單</el-button>
        </el-row>

        <el-table
            :data="tableData"
            style="width: 100%; margin-bottom: 20px"
            row-key="id"
            border
            stripe
            default-expand-all
            :tree-props="{ children: 'children', hasChildren: 'hasChildren' }"
        >
            <el-table-column prop="name" label="選單名稱" width="240" />
            <el-table-column prop="icon" label="圖示" width="120" align="center">
                <template v-slot="scope">
                    <el-icon><svg-icon :icon="scope.row.icon" /></el-icon>
                </template>
            </el-table-column>
            <el-table-column prop="menu_type" label="選單類型"  width="120" align="center">
                <template v-slot="scope">
                    <el-tag size="small" v-if="scope.row.menuType === 'M'" type="danger" effect="dark">目錄</el-tag>
                        <el-tag size="small" v-else-if="scope.row.menuType === 'C'" type="success" effect="dark">選單</el-tag>
                </template>
            </el-table-column>
            <el-table-column prop="order_num" label="排序"  width="150" align="center"/>
            <el-table-column prop="path" label="組件路徑"  width="250" />
            <el-table-column prop="perms" label="權限標識"  width="250" />
            <el-table-column prop="action" label="操作" width="240" fixed="right" align="center">
            <template v-slot="scope" >
                <el-button type="primary" :icon="Edit" @click="handleDialogValue(scope.row.id)" circle/>
                <el-popconfirm title="確定要刪除此選單項嗎?" @confirm="handleDelete(scope.row.id)">
                    <template #reference>
                        <el-button  type="danger" :icon="Delete" circle/>
                    </template>
                </el-popconfirm>
            </template>
            </el-table-column>
        </el-table>
    </div> 

    <Dialog v-model="dialogVisible" :tableData="tableData" :dialogVisible="dialogVisible" :id="id" :dialogTitle="dialogTitle" @initMenuList="initMenuList"></Dialog>
</template>
  

<script setup>
import Dialog from './components/dialog'
import { Delete, DocumentAdd, Edit} from '@element-plus/icons-vue'
import { ref } from 'vue'
import requestUtil from "@/utils/request"
import { ElMessage } from 'element-plus'

const tableData = ref([])

const id=ref(-1)

const dialogVisible=ref(false)

const dialogTitle=ref('')

const initMenuList=async()=>{
    const res=await requestUtil.get("menu/treeList");
    tableData.value=res.data.treeList;
}

initMenuList();

const handleDialogValue=(menuId)=>{
    if(menuId){
        id.value=menuId;
        dialogTitle.value="修改選單"
    }else{
        id.value=-1;
        dialogTitle.value="新增選單"
    }
    dialogVisible.value=true
}

const handleDelete=async (id)=>{
    const res=await requestUtil.del("menu/action",id)
        if(res.data.code==200){
            ElMessage({
            type: 'success',
            message: '成功刪除該選單'
            })
            initMenuList();
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
  