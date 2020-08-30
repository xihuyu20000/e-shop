<template>
  <el-container style="height:100vh">
    <el-header><layout-header></layout-header></el-header>
    <el-container>
      <layout-aside></layout-aside>
      <el-main>
        <layout-breadcrumb></layout-breadcrumb>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import LayoutHeader from '@/components/LayoutHeader.vue'
import LayoutAside from '@/components/LayoutAside.vue'
import LayoutBreadcrumb from '@/components/LayoutBreadcrumb.vue'
export default {
  data() {
    return {}
  },
  components: { LayoutHeader, LayoutAside, LayoutBreadcrumb }
}
</script>

<style lang="scss" scoped>
.el-header {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  background-color: #d3dce6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 160px;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>
