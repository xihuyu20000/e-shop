<template>
  <div class="common-table">
    <div class="query-form">
      <el-form :inline="true" :model="form">
        <el-form-item label="标题">
          <el-input clearable v-model="form.title" placeholder="标题"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="queryData">查询</el-button>
          <el-button type="primary" @click="toadd">添加</el-button>
        </el-form-item>
      </el-form>
    </div>
    <el-table :data="tableData" border style="width: 100%">
      <el-table-column type="selection" width="55"></el-table-column>
      <el-table-column prop="id" label="编号" width="150"> </el-table-column>
      <el-table-column prop="title" label="标题" sortable> </el-table-column>
      <el-table-column prop="author" label="作者" width="120" sortable> </el-table-column>
      <el-table-column prop="organ" label="机构" width="120" sortable> </el-table-column>
      <el-table-column prop="source" label="来源" width="120" sortable> </el-table-column>
      <el-table-column prop="keyword" label="关键词" width="120" sortable> </el-table-column>
      <el-table-column fixed="right" label="操作" width="100">
        <template slot-scope="scope">
          <el-button @click="handleTableRow('show', scope.row)" type="text" size="small">查看</el-button>
          <el-button @click="handleTableRow('edit', scope.row)" type="text" size="small">编辑</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination background layout="prev, pager, next" :total="total" @current-change="handleCurrentChange"> </el-pagination>
    <common-add ref="add-dialog" v-on:flushTable="queryData"></common-add>
  </div>
</template>

<script>
import CommonAdd from '@/components/CommonAdd.vue'
export default {
  data() {
    return {
      form: {
        title: '',
        pageNo: 1,
        pageSize: 10
      },

      total: 0,
      tableData: []
    }
  },
  methods: {
    toadd: function() {
      this.$refs['add-dialog'].show()
    },
    queryData: async function() {
      const { data: res } = await this.$http.get('/users/', { params: this.form })
      this.total = res.data.total
      this.tableData = res.data.data
      this.$message({
        message: res.meta.msg,
        type: 'success'
      })
    },
    handleTableRow: function(flag, row) {
      if (flag == 'show') {
        this.$message('查看   ' + row)
      }
      if (flag == 'edit') {
        this.$message('编辑   ' + row)
      }
    },
    handleCurrentChange: function(currentPage) {
      this.form.pageNo = currentPage
      this.queryData()
    }
  },
  created: function() {
    this.queryData()
  },
  components: { CommonAdd }
}
</script>

<style lang="scss" scoped>
.common-table {
  margin-top: 20px;
  .query-form {
    .el-form {
      width: 100%;
      display: flex;

      .el-form-item {
        display: flex;
      }
    }
  }
}
</style>
