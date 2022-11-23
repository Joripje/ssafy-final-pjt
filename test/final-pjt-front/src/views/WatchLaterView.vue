<template>
  <div>
    <h1>나중에 볼 영화 목록입니다</h1>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'
export default {
  name: 'WatchLaterView',
  components: {
    MovieList,
  }
}
</script>

<style>

</style>