<template>
  <div class="common-table">
    <common-table v-on:refresh="loadData"></common-table>
  </div>
</template>

<script>
import CommonTable from '@/components/CommonTable.vue'
export default {
  data() {
    return {}
  },
  methods: {
    loadData: async function() {
      const { data: res } = await this.$http.get('/users/')
      console.log('加载数据', res)
    }
  },
  components: { CommonTable },
  created: function() {
    this.loadData()
  }
}
</script>

<style lang="scss" scoped>
.common-table {
}
</style>
