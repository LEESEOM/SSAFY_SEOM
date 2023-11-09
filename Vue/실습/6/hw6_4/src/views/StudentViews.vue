<template>
  <div>
    <h1>학생 상세 정보 목록 입니다.</h1>
    <p
    v-for="student of students"
    :key="student.name"
    @click="getDetail(student.name)"
    >
    {{ student.name }} 학생 정보 보기
    </p>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const students = [
    { name : '김하나' },
    { name : '김두리' },
    { name : '김서이' },
  ]


const router = useRouter()

const getDetail = function (name) {
  router.push({ name: 'studentDetail', params: {name: name}})
}
</script>

<style scoped>

</style>