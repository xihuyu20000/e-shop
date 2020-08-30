<template>
  <div>Home</div>
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
