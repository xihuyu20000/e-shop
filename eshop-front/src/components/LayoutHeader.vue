<template>
  <div class="common-header">
    <div class="left-header">电商后台系统</div>
    <div class="right-header">
      <el-dropdown trigger="click" @command="handleUserImage">
        <span class="el-dropdown-link"><img src="../assets/image/user.jpg"/></span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="setting">用户设置</el-dropdown-item>
          <el-dropdown-item command="quit">退出</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {}
  },
  methods: {
    handleUserImage: function(cmd) {
      if (cmd === 'setting') {
        this.$message('click on item ' + cmd)
      }
      if (cmd === 'quit') {
        window.sessionStorage.clear()
        this.$router.push('/login')
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.common-header {
  display: flex;
  justify-content: space-between;
  background-color: #ffe;
  .left-header {
    font-family: 'Courier New', Courier, monospace;
    font-size: 2em;
  }
  .right-header {
    .el-dropdown-link {
      cursor: pointer;
      color: #409eff;
    }
    img {
      height: 60px;
      width: 60px;
      border-radius: 50%;
    }
  }
}
</style>
