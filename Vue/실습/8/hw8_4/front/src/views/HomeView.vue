<template>
  <div>
    <h1>게시글 목록 페이지</h1>
    <RouterLink :to="{ name : 'create' }">게시글 생성</RouterLink>
    <ArticleList />
  </div>
  <RouterView />
</template>

<script setup>
import ArticleList from '@/components/ArticleList.vue';
import { RouterView, RouterLink } from 'vue-router'




</script>

<style scoped>

</style>