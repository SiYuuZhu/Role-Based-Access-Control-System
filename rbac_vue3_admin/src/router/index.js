import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'


const routes = [
  {
    path: '/',
    name: '主頁',
    component: () => import('../layout/index.vue'),
    meta: { title :'後台權限管理系統 | 主頁' },
    redirect: '/index',
    children: [
      {
        path: '/index',
        name: '首頁',
        component: () => import('../views/index/index.vue'),
        meta: { title :'後台權限管理系統 | 首頁' }
      },
      {
        path: '/sys/user',
        name: '使用者管理',
        component: () => import('../views/sys/user/index.vue'),
        meta: { title :'後台權限管理系統 | 使用者管理' }
      },
      {
        path: '/sys/role',
        name: '角色管理',
        component: () => import('../views/sys/role/index.vue'),
        meta: { title :'後台權限管理系統 | 角色管理' }
      },
      {
        path: '/sys/menu',
        name: '選單管理',
        component: () => import('../views/sys/menu/index.vue'),
        meta: { title :'後台權限管理系統 | 選單管理' }
      },
      {
        path: '/bsns/department',
        name: '部門管理',
        component: () => import('../views/bsns/Department.vue'),
        meta: { title :'後台權限管理系統 | 部門管理' }
      },
      {
        path: '/bsns/post',
        name: '職位管理',
        component: () => import('../views/bsns/Post.vue'),
        meta: { title :'後台權限管理系統 | 職位管理' }
      },
      {
        path: '/userCenter',
        name: '帳號中心',
        component: () => import('../views/userCenter/index.vue'),
        meta: { title :'後台權限管理系統 | 帳號中心' }
      },
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login.vue'),
    meta: { title :'後台權限管理系統 | 登入' }
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  window.document.title = to.meta.title
  next()
})


export default router
