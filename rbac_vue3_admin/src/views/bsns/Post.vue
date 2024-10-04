<template>
    <div class="app-container">
    <el-row :gutter="20">
        <el-col :span="24">
            <el-card>
                <template v-slot:header>
                    <div class="clearfix">
                    <span>管轄職位</span>
                    </div>
                </template>
                <el-tabs v-model="activeTab">
                    <el-tab-pane label="助理" name="post-J">
                        <el-descriptions
                            title="助理"
                            direction="vertical"
                            :column="4"
                            :size="size"
                            border
                        >
                            <el-descriptions-item label="職位名稱">助理</el-descriptions-item>
                            <el-descriptions-item label="職位需求">-</el-descriptions-item>
                            <el-descriptions-item label="工作資歷">-</el-descriptions-item>
                            <el-descriptions-item label="薪資範圍" :span="2">-</el-descriptions-item>
                            <el-descriptions-item label="所屬單位">
                                <div class="flex gap-2">
                                    <el-tag size="small">行銷部</el-tag>
                                    <el-tag size="small">業務部</el-tag>
                                    <el-tag size="small">財務部</el-tag>
                                    <el-tag size="small">行政部</el-tag>
                                    <el-tag size="small">產品部</el-tag>
                                </div>
                            </el-descriptions-item>
                            <el-descriptions-item label="職位工作內容">
                                -
                            </el-descriptions-item>
                        </el-descriptions>
                    </el-tab-pane>
                    <el-tab-pane label="專員" name="post-I">
                        <el-descriptions
                            title="專員"
                            direction="vertical"
                            :column="4"
                            :size="size"
                            border
                        >
                            <el-descriptions-item label="職位名稱">專員</el-descriptions-item>
                            <el-descriptions-item label="職位需求">-</el-descriptions-item>
                            <el-descriptions-item label="工作資歷">-</el-descriptions-item>
                            <el-descriptions-item label="薪資範圍" :span="2">-</el-descriptions-item>
                            <el-descriptions-item label="所屬單位">
                                <div class="flex gap-2">
                                    <el-tag size="small">-</el-tag>
                                </div>
                            </el-descriptions-item>
                            <el-descriptions-item label="職位工作內容">
                                -
                            </el-descriptions-item>
                        </el-descriptions>
                    </el-tab-pane>
                    <el-tab-pane label="資深專員" name="post-H">
                        <el-descriptions
                            title="資深專員"
                            direction="vertical"
                            :column="4"
                            :size="size"
                            border
                        >
                            <el-descriptions-item label="職位名稱">資深專員</el-descriptions-item>
                            <el-descriptions-item label="職位需求">-</el-descriptions-item>
                            <el-descriptions-item label="工作資歷">-</el-descriptions-item>
                            <el-descriptions-item label="薪資範圍" :span="2">-</el-descriptions-item>
                            <el-descriptions-item label="所屬單位">
                                <div class="flex gap-2">
                                    <el-tag size="small">-</el-tag>
                                </div>
                            </el-descriptions-item>
                            <el-descriptions-item label="職位工作內容">
                                -
                            </el-descriptions-item>
                        </el-descriptions>
                    </el-tab-pane>
                    <el-tab-pane label="組長" name="post-G">
                        <el-descriptions
                            title="組長"
                            direction="vertical"
                            :column="4"
                            :size="size"
                            border
                        >
                            <el-descriptions-item label="職位名稱">組長</el-descriptions-item>
                            <el-descriptions-item label="職位需求">-</el-descriptions-item>
                            <el-descriptions-item label="工作資歷">-</el-descriptions-item>
                            <el-descriptions-item label="薪資範圍" :span="2">-</el-descriptions-item>
                            <el-descriptions-item label="所屬單位">
                                <el-tag size="small">-</el-tag>
                            </el-descriptions-item>
                            <el-descriptions-item label="職位工作內容">
                                -
                            </el-descriptions-item>
                        </el-descriptions>
                    </el-tab-pane>
                    <el-tab-pane label="主任" name="post-F">
                        <el-descriptions
                            title="主任"
                            direction="vertical"
                            :column="4"
                            :size="size"
                            border
                        >
                            <el-descriptions-item label="職位名稱">主任</el-descriptions-item>
                            <el-descriptions-item label="職位需求">-</el-descriptions-item>
                            <el-descriptions-item label="工作資歷">-</el-descriptions-item>
                            <el-descriptions-item label="薪資範圍" :span="2">-</el-descriptions-item>
                            <el-descriptions-item label="所屬單位">
                                <el-tag size="small">-</el-tag>
                            </el-descriptions-item>
                            <el-descriptions-item label="職位工作內容">
                                -
                            </el-descriptions-item>
                        </el-descriptions>
                    </el-tab-pane>
                    <el-tab-pane label="專案經理" name="post-E">
                        <el-descriptions
                            title="專案經理"
                            direction="vertical"
                            :column="4"
                            :size="size"
                            border
                        >
                            <el-descriptions-item label="職位名稱">專案經理</el-descriptions-item>
                            <el-descriptions-item label="職位需求">-</el-descriptions-item>
                            <el-descriptions-item label="工作資歷">-</el-descriptions-item>
                            <el-descriptions-item label="薪資範圍" :span="2">-</el-descriptions-item>
                            <el-descriptions-item label="所屬單位">
                                <el-tag size="small">-</el-tag>
                            </el-descriptions-item>
                            <el-descriptions-item label="職位工作內容">
                                -
                            </el-descriptions-item>
                        </el-descriptions>
                    </el-tab-pane>
                    <el-tab-pane label="協理" name="post-D">
                        <el-descriptions
                            title="協理"
                            direction="vertical"
                            :column="4"
                            :size="size"
                            border
                        >
                            <el-descriptions-item label="職位名稱">協理</el-descriptions-item>
                            <el-descriptions-item label="職位需求">-</el-descriptions-item>
                            <el-descriptions-item label="工作資歷">-</el-descriptions-item>
                            <el-descriptions-item label="薪資範圍" :span="2">-</el-descriptions-item>
                            <el-descriptions-item label="所屬單位">
                                <el-tag size="small">-</el-tag>
                            </el-descriptions-item>
                            <el-descriptions-item label="職位工作內容">
                                -
                            </el-descriptions-item>
                        </el-descriptions>
                    </el-tab-pane>
                    <el-tab-pane label="副理" name="post-C">
                        <el-descriptions
                            title="副理"
                            direction="vertical"
                            :column="4"
                            :size="size"
                            border
                        >
                            <el-descriptions-item label="職位名稱">副理</el-descriptions-item>
                            <el-descriptions-item label="職位需求">-</el-descriptions-item>
                            <el-descriptions-item label="工作資歷">-</el-descriptions-item>
                            <el-descriptions-item label="薪資範圍" :span="2">-</el-descriptions-item>
                            <el-descriptions-item label="所屬單位">
                                <el-tag size="small">-</el-tag>
                            </el-descriptions-item>
                            <el-descriptions-item label="職位工作內容">
                                -
                            </el-descriptions-item>
                        </el-descriptions>
                    </el-tab-pane>
                    <el-tab-pane label="經理" name="post-B">
                        <el-descriptions
                            title="經理"
                            direction="vertical"
                            :column="4"
                            :size="size"
                            border
                        >
                            <el-descriptions-item label="職位名稱">經理</el-descriptions-item>
                            <el-descriptions-item label="職位需求">-</el-descriptions-item>
                            <el-descriptions-item label="工作資歷">-</el-descriptions-item>
                            <el-descriptions-item label="薪資範圍" :span="2">-</el-descriptions-item>
                            <el-descriptions-item label="所屬單位">
                                <el-tag size="small">-</el-tag>
                            </el-descriptions-item>
                            <el-descriptions-item label="職位工作內容">
                                -
                            </el-descriptions-item>
                        </el-descriptions>
                    </el-tab-pane>
                    <el-tab-pane label="總監" name="post-A">
                        <el-descriptions
                            title="總監"
                            direction="vertical"
                            :column="4"
                            :size="size"
                            border
                        >
                            <el-descriptions-item label="職位名稱">總監</el-descriptions-item>
                            <el-descriptions-item label="職位需求">-</el-descriptions-item>
                            <el-descriptions-item label="工作資歷">-</el-descriptions-item>
                            <el-descriptions-item label="薪資範圍" :span="2">-</el-descriptions-item>
                            <el-descriptions-item label="所屬單位">
                                <el-tag size="small">決策者</el-tag>
                            </el-descriptions-item>
                            <el-descriptions-item label="職位工作內容">
                                -
                            </el-descriptions-item>
                        </el-descriptions>
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

.el-descriptions {
  margin-top: 20px;
}


</style>