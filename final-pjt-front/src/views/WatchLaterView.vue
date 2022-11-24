<template>
  <div style="padding: 40px;">
    <h1 style="color: white; float: left;">위시리스트</h1>
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