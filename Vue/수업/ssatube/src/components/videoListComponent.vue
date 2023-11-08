<template>
  <div>
    <h1>리스트</h1>
  
  <ul>
    <videoListItemComponent 
    v-for="video of videoList"
    :key="video.id.videoId"
    :video="video"
    @item-select="onItemSelect"
    />
  </ul>
  </div>
</template>

<script setup>
  import videoListItemComponent from '@/components/videoListItemComponent.vue';
  defineProps(
    {videoList:Array},
  )
  const emit = defineEmits(['itemSelect'])
  const onItemSelect = function (video) {
    emit('itemSelect',video)
  }
</script>

<style scoped>

</style>