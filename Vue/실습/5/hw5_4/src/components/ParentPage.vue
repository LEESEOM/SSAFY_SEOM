<template>
  <div >
    <h1>부모 페이지입니다.</h1>
    <ChildPage 
    v-for="child of children"
    :key="child.name"
    :child="child"
    @giveMeAllowance="updateBalance"
    />
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import ChildPage from '@/components/ChildPage.vue'
  defineProps(
    {children:Array},
  )
  const children = ([
    { name: '김하나',
      age: 30,
      balance:ref(100000)
    },
    { name: '김두리',
      age: 20,
      balance:ref(10000)
    },
    { name: '김서이',
      age: 10,
      balance:ref(1000)
    },
  ])

    const updateBalance = function(child) {
      child.balance.value += 1000
    }
</script>

<style scoped>

</style>