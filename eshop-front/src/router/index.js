import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}

const routes = [
  { path: '/login', component: () => import('@/views/Login.vue') },
  {
    path: '/',
    component: () => import('@/views/Layout.vue'),
    children: [
      { path: '/', redirect: '/home' },
      { path: '/home', component: () => import('@/views/Home.vue') },
      { path: '/users', component: () => import('@/views/Users.vue') },
      { path: '/roles', component: () => import('@/views/Roles.vue') },
      { path: '/rights', component: () => import('@/views/Rights.vue') }
    ]
  }
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
