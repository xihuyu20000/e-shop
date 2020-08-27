<template>
  <div><el-button type="info" @click="quit">退出</el-button></div>
</template>

<script>
export default {
  data() {
    return {}
  },
  methods: {
    quit: function() {
      window.sessionStorage.clear()
      this.$router.push('/login')
    }
  }
}
</script>

<style lang="scss" scoped></style>
