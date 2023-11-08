<template>
  <div>
    <input type="text" v-model="keyword">
    <button @click="onSearch">검색</button>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  const emit = defineEmits('searchVideo')
  const keyword = ref('')
  const onSearch = function() {
    emit('searchVideo', keyword)
  }
</script>

<style scoped>

</style>