<template>
  <div class="add-dialog">
    <el-dialog title="添加用户" :visible.sync="canshow" width="30%">
      <el-form :model="addForm" :rules="rules" ref="addForm" label-width="100px">
        <el-form-item label="标题" prop="title">
          <el-input v-model="addForm.title"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="canshow = false">取 消</el-button>
        <el-button type="primary" @click="submitForm('addForm')">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      canshow: false,
      addForm: {
        title: ''
      },
      rules: {
        title: [{ required: true, message: '请输入标题', trigger: 'blur' }]
      }
    }
  },
  methods: {
    show: function() {
      this.canshow = true
    },
    hide: function() {
      this.canshow = false
    },
    submitForm(formName) {
      this.$refs[formName].validate(async valid => {
        if (!valid) return this.$message('验证失败')
        const { data: res } = await this.$http.post('/users/', this.addForm)
        if (res.meta.status !== 200) return this.$message.error(res.meta.msg)
        this.$message({
          message: res.meta.msg,
          type: 'success'
        })
        this.$emit('flushTable')
      })
      this.canshow = false
      this.$emit('refresh')
    }
  }
}
</script>

<style lang="scss" scoped></style>
