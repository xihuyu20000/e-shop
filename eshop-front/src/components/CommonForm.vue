<template>
  <el-form :model="form" label-width="100px">
    <template v-for="(meta, i) in metaTable">
      <!--input类型-->
      <el-form-item v-if="'input' == meta.style" :label="meta.label" :key="i">
        <el-input v-model="form[meta.field]" :placeholder="meta.tip"></el-input>
      </el-form-item>
      <!--select类型-->
      <el-form-item v-if="'select' == meta.style" :label="meta.label" :key="i">
        <el-select v-model="form[meta.field]" :placeholder="meta.tip">
          <el-option v-for="subitem in meta.subdata" :key="subitem.value" :label="subitem.label" :value="subitem.value"></el-option>
        </el-select>
      </el-form-item>
      <!--date类型-->
      <el-form-item v-if="'date' == meta.style" :label="meta.label" :key="i">
        <el-date-picker type="date" v-model="form[meta.field]" :placeholder="meta.tip"></el-date-picker>
      </el-form-item>
      <!--time类型-->
      <el-form-item v-if="'time' == meta.style" :label="meta.label" :key="i">
        <el-time-picker type="fixed-time" v-model="form[meta.field]" :placeholder="meta.tip"></el-time-picker>
      </el-form-item>
      <!--switch类型-->
      <el-form-item v-if="'switch' == meta.style" :label="meta.label" :key="i">
        <el-switch v-model="form[meta.field]" :placeholder="meta.tip"></el-switch>
      </el-form-item>
      <!--checkbox类型-->
      <el-form-item v-if="'checkbox' == meta.style" :label="meta.label" :key="i">
        <el-checkbox-group v-model="form[meta.field]">
          <el-checkbox v-for="(subitem, j) in meta.subdata" :label="subitem.label" :name="meta.field" :key="j"></el-checkbox>
        </el-checkbox-group>
      </el-form-item>
      <!--radio类型-->
      <el-form-item v-if="'radio' == meta.style" :label="meta.label" :key="i">
        <el-radio-group v-model="form[meta.field]">
          <el-radio v-for="(subitem, j) in meta.subdata" :label="subitem.label" :key="j"></el-radio>
        </el-radio-group>
      </el-form-item>
      <!--textarea类型-->
      <el-form-item v-if="'textarea' == meta.style" :label="meta.label" :key="i">
        <el-input type="textarea" v-model="form[meta.field]" :placeholder="meta.tip"></el-input>
      </el-form-item>
    </template>
  </el-form>
</template>

<script>
export default {
  data() {
    return {
      form: {},
      metaTable: [
        { label: '活动名称', field: 'name', style: 'input', tip: '请输入活动名称' },
        {
          label: '活动区域',
          field: 'region',
          style: 'select',
          tip: '请选择活动区域',
          subdata: [
            { label: '上海市', value: 'shanghai' },
            { label: '北京市', value: 'beijing' },
            { label: '天津市', value: 'tianjin' }
          ]
        },
        { label: '活动日期', field: 'date1', style: 'date', tip: '请输入开始日期' },
        { label: '活动时间', field: 'date2', style: 'time', tip: '请输入开始时间' },
        { label: '即时配送', field: 'delivery', style: 'switch' },
        { label: '活动性质', field: 'type', style: 'checkbox', subdata: [{ label: '美食' }, { label: '地推活动' }, { label: '线下主题活动' }, { label: '单纯品牌曝光' }] },
        { label: '特殊资源', field: 'resource', style: 'radio', subdata: [{ label: '线上品牌赞助' }, { label: '线下场地免费' }] },
        { label: '活动形式', field: 'desc', style: 'textarea', tip: '活动形式' }
      ]
    }
  }
}
</script>

<style lang="scss" scoped></style>
