<template>
  <header>
    <searchBarComponent 
    @search-video="onSearchVideo"
    />
  </header>

  <main class="container">
    <div class="d-flex flex-row justify-content-between">
      <div>
       <videoDetailComponent 
       :video-selected="selectedVideo"
       />
      </div>
      <div>
       <videoListComponent
        :video-list="videoList"
        @item-select="onItemSelect"
       />
      </div>
    </div>
  </main>
</template>

<script setup>
  import searchBarComponent from '@/components/searchBarComponent.vue'
  import videoDetailComponent from '@/components/videoDetailComponent.vue'
  import videoListComponent from '@/components/videoListComponent.vue'
  import axios from 'axios'
  import { onMounted, ref } from 'vue'
  const videoList = ref([])
  const API_URL = 'https://www.googleapis.com/youtube/v3/search'
  const onItemSelect = function(video) {
    selectedVideo.value = video
  }

  const selectedVideo = ref(null)
  const keyword = ref('')
  
  const onSearchVideo = function(keyword){
    searchVideo(keyword.value)
  }
  const searchVideo = function(keyword){
    axios({
      url:API_URL,
      params:{
        type:'video',
        part:'snippet',
        key:'AIzaSyDySIEhJJOb-oItTbS41-dglbTAwwsuVbk',
        q: keyword
      }
    })
    .then((response)=>{
      console.log(response.data)
      videoList.value = response.data.items
    })
  }

</script>

<style scoped>

</style>