<template>
  <div>
    <MovieListItem
      v-for="(movie, index) in movies"
      :key="index"
      :movie="movie"
    />
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'
export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  computed: {
    movies() {
      return this.$store.state.movie_list
    }
  }
}
</script>

<style>

</style>