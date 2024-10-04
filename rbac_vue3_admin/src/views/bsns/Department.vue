<template>
    <div class="app-container">
    <el-row :gutter="20">
        <el-col :span="24">
            <el-card>
                <template v-slot:header>
                    <div class="clearfix">
                    <span>管轄部門</span>
                    </div>
                </template>
                <el-tabs v-model="activeTab">
                    <el-tab-pane label="行銷部門" name="department-A">
                        [INFO]行銷部門
                    </el-tab-pane>
                    <el-tab-pane label="業務部門" name="department-B">
                        [INFO]業務部門
                    </el-tab-pane>
                    <el-tab-pane label="研發部門" name="department-C">
                        [INFO]研發部門
                    </el-tab-pane>
                    <el-tab-pane label="產品部門" name="department-D">
                        [INFO]產品部門
                    </el-tab-pane>
                    <el-tab-pane label="財務部門" name="department-E">
                        [INFO]財務部門
                    </el-tab-pane>
                    <el-tab-pane label="行政部門" name="department-F">
                        [INFO]行政部門
                    </el-tab-pane>
                    <el-tab-pane label="客服部門" name="department-G">
                        [INFO]客服部門
                    </el-tab-pane>
                    <el-tab-pane label="人資部門" name="department-H">
                        [INFO]人資部門
                    </el-tab-pane>
                </el-tabs>
            </el-card>
        </el-col>
    </el-row>
</div>

</template>

<script setup>

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


::v-deep .el-card__body{
height: 350px;
}


</style>