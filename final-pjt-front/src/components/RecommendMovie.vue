<template>
  <div>
    <h1>맞춤 추천 영화</h1>
    <RecommendMovieList/>
  </div>
</template>

<script>
import RecommendMovieList from '@/components/RecommendMovieList.vue'
export default {
  name: 'RecommendMovie',
  components: {
    RecommendMovieList,
  }
}
</script>

<style>

</style>