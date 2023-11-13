<template>
  <div style="border: 1px black solid;">
    <h2>부모 컴포넌트</h2>
    <p>{{ familyInfo.father }}</p>
    <p>{{ familyInfo.mother }}</p>
    <ChildPage
    v-for="child in familyInfo.children" 
    :child-info="child"
    class="childPage"
    />
  </div>
</template>

<script setup>
import ChildPage from '@/components/ChildPage.vue';

defineProps({
  familyInfo : Object
})

</script> 

<style scoped>
.childPage {
    border: #ccc solid 1px;
    text-align: center;
    background-color: white;
    width: 800px;
    margin: 20px;
}
</style>

