<template>
  <el-aside width="collapsable?'64px':'200px'">
    <div class="toggle-button" @click="toggleCollapse">|||</div>
    <el-menu background-color="#545c64" text-color="#fff" active-text-color="#ffd04b" :router="true" :default-active="activeMenu" :unique-opened="true" :collapse="collapsable" :collapse-transition="false">
      <template v-for="item in asideMenu">
        <el-menu-item :index="item.label" v-if="!Object.prototype.hasOwnProperty.call(item, 'children')" :key="item.label" @click="selectMenu(item)">
          <i :class="item.icon"></i><span slot="title">{{ item.label }}</span>
        </el-menu-item>
        <el-submenu :index="item.label" v-if="Object.prototype.hasOwnProperty.call(item, 'children')" :key="item.label" :router="true">
          <template slot="title">
            <i :class="item.icon"></i><span>{{ item.label }}</span>
          </template>
          <el-menu-item :index="subitem.label" v-for="subitem in item.children" :key="subitem.label" @click="selectMenu(subitem)"> <i :class="subitem.icon"></i>{{ subitem.label }} </el-menu-item>
        </el-submenu>
      </template>
    </el-menu>
  </el-aside>
</template>

<script>
export default {
  data() {
    return {
      collapsable: false,
      activeMenu: '/home',
      asideMenu: []
    }
  },
  methods: {
    toggleCollapse: function() {
      this.collapsable = !this.collapsable
    },
    selectMenu: function(menu) {
      console.log('选择菜单', menu)
      this.$router.push(menu.path)
      this.$store.commit('breadcrumb/changeMenu', menu.label)
      window.sessionStorage.setItem('active-menu', menu.label)
    },
    loadData: async function() {
      const { data: res } = await this.$http.get('/menus/')
      if (res.meta.status != 200) return this.$message.error(res.meta.msg)
      this.asideMenu = res.data
    }
  },
  created() {
    this.loadData()
    this.activeMenu = window.sessionStorage.getItem('active-menu')
  }
}
</script>

<style lang="scss" scoped>
.el-aside {
  height: 100vh;
  .toggle-button {
    background-color: #4a5064;
    font-size: 10px;
    line-height: 24px;
    text-align: center;
    letter-spacing: 0.2em;
    cursor: pointer;
  }
  .el-menu {
    height: 100%;
    border-right: none;
  }
}
</style>
