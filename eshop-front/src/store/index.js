import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const breadcrumb = {
  namespaced: true,
  state: {
    path: ''
  },
  mutations: {
    changeMenu(state, path) {
      state.path = path
      console.log('改变菜单', path)
    }
  },
  actions: {}
}

export default new Vuex.Store({
  modules: { breadcrumb }
})
