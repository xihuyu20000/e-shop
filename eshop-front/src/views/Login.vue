<template>
  <div class="login-container">
    <div class="login-box">
      <!--头像区域-->
      <div class="avator-box">
        <img src="../assets/image/logo.png" />
      </div>
      <!--登录区域-->
      <el-form :model="loginForm" status-icon :rules="rules" ref="loginForm" label-width="100px" class="login-form">
        <el-form-item label="用户名" prop="username">
          <el-input v-model="loginForm.username" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" v-model="loginForm.password" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm('loginForm')">提交</el-button>
          <el-button @click="resetForm('loginForm')">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loginForm: {
        username: 'root',
        password: 'admin'
      },
      rules: {
        username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
        password: [{ required: true, message: '请输入密码', trigger: 'blur' }]
      }
    }
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('/login/', this.loginForm)
        if (res.meta.status != 200) return this.$message.error(res.meta.msg)
        this.$message({
          message: res.meta.msg,
          type: 'success'
        })
        window.sessionStorage.setItem('token', res.data.token)
        this.$router.push('/home')
      })
    },
    resetForm(formName) {
      this.$refs[formName].resetFields()
    }
  }
}
</script>

<style lang="scss" scoped>
.login-container {
  height: 100%;
  background-color: #2b4b6b;
  .login-box {
    width: 450px;
    height: 300px;
    background-color: #fff;
    border-radius: 5px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);

    .avator-box {
      height: 130px;
      width: 130px;
      border: 1px solid #eee;
      background-color: #fff;
      border-radius: 50%;
      padding: 10px;
      box-shadow: 0 0 20px #ddd;
      position: absolute;
      left: 50%;
      transform: translate(-50%, -50%);
      img {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background-color: #eee;
      }
    }
  }
}
.login-form {
  position: absolute;
  bottom: 0;
  box-sizing: border-box;
  width: 100%;
  padding: 20px;
}
.btns {
  display: flex;
  justify-content: flex-end;
}
</style>
