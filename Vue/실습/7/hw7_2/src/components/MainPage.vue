<template>
  <div>
    <h1>pinia 연습하기</h1>
    <ParentPage 
    v-for="family in store.familyInfo"
    :key='family.familyName'
    :family-info="family"
    class="parentBox"
    />
  </div>
</template>

<script setup>
import ParentPage from '@/components/ParentPage.vue';
import { useFamilyStore } from '@/stores/family';

const store = useFamilyStore()

</script>

<style scoped>
.parentBox {
    border: #ccc solid 1px;
    text-align: center;
    background-color: #f7f4f4;
    margin: 20px;
    width: 1000px;
}
</style>

