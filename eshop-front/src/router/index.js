import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: () => import('@/views/Login.vue') },
  { path: '/home', component: () => import('@/views/Home.vue') }
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  // 如果访问登录页，放行
  if (to.path === '/login') return next()
  // 客户端是否有token
  const uid = window.sessionStorage.getItem('token')
  // 如果没有token，跳转到登录
  if (!uid) return next('/login')
  // 如果有token，直接放行
  next()
})

export default router
