<template>
  <div>
    <h1>맞춤 추천 영화</h1>
    <hr>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'
export default {
  name: 'RecommendMovie',
  components: {
    MovieList,
  }
}
</script>

<style>

</style>