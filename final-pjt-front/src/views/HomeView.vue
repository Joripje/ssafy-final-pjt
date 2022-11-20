<template>
  <div>
    <h1>기본화면 입니다</h1>
    <TrendingMovie/>
    <RecommendMovie/>
  </div>
</template>

<script>
import RecommendMovie from '@/components/RecommendMovie.vue'
import TrendingMovie from '@/components/TrendingMovie.vue'
export default {
  name: 'HomeView',
  components: { 
    RecommendMovie,
    TrendingMovie
  },

}
</script>

<style>

</style>