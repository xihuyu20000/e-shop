<template>
  <common-form></common-form>
</template>

<script>
import CommonForm from '@/components/CommonForm.vue'
export default {
  data() {
    return {}
  },
  methods: {
    quit: function() {
      window.sessionStorage.clear()
      this.$router.push('/login')
    }
  },
  components: { CommonForm }
}
</script>

<style lang="scss" scoped></style>
