import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ArticleCreateView from '../views/ArticleCreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import SignInView from '@/views/SignInView.vue'
import { useArticleStore } from '../stores/articles'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/create',
      name: 'create',
      component: ArticleCreateView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView,
      beforeEnter: (to, from) => {
        const store = useArticleStore()
        if (to.name === 'signup' && (store.isLogin)) {
          window.alert('이미 로그인')
          return { name: 'home' }
        }
      }
    },
    {
      path: '/signin',
      name: 'signin',
      component: SignInView,
      beforeEnter: (to, from) => {
        const store = useArticleStore()
        if (to.name === 'signin' && (store.isLogin)) {
          window.alert('이미 로그인')
          return { name: 'home' }
        }
    }
  }]
})

router.beforeEach((to, from) => {
  const store = useArticleStore()
  if (to.name === 'home' && !store.isLogin) {
    window.alert('로그인 필요')
    return { name: 'signin'}
  }
})
export default router
