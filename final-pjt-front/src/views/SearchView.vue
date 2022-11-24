<template>
  <div>
    <h1 style="color: white;">검색화면 입니다</h1>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'
export default {
  name: 'SearchView',
  components: {
    MovieList,
  }
}
</script>

<style>

</style>