<template>
  <div style="border: 1px black solid;">
    자식 페이지
    <p>{{ childInfo.name }}</p>
  </div>
</template>



<script setup>
defineProps({
  childInfo : Object
})

</script>

<style scoped>

</style>

