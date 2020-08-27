module.exports = {
  devServer: {
    port: 33333,
    open: false
    // proxy: {}
  },
  css: {
    loaderOptions: {
      sass: {
        prependData: `@import "@/assets/css/_variable.scss";`
      }
    }
  }
}
