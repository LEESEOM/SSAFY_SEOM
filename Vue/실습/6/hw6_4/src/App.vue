<template>
  <div>
    <MainPage />
    <p>
    <RouterLink :to="{ name : 'some' }">Some</RouterLink>
    |
    <RouterLink to="/other">Other</RouterLink>
    |
    <RouterLink :to="{ name : 'students' }">Students</RouterLink>
    </p>
  </div>
  <RouterView />
</template>

<script setup>
import MainPage from '@/components/MainPage.vue'
import { RouterLink, RouterView } from 'vue-router'


</script>

<style scoped>

</style>