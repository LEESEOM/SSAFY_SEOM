<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()
</script>

<template>
  <header>
    <div class="wrapper">
      <nav v-if="store.isLogin">
        <RouterLink to="/">Home</RouterLink> | 
      </nav>
      <nav v-else>
        <RouterLink to="/">Home</RouterLink> | 
        <RouterLink to="/signup">SignUp</RouterLink> | 
        <RouterLink to="/signin">SignIn</RouterLink> | 
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
</style>
