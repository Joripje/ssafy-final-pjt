<template>
  <div>
    <h1>최근 인기 영화</h1>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'
export default {
  name: 'TrendingMovie',
  components: {
    MovieList,
  }
}
</script>

<style>

</style>