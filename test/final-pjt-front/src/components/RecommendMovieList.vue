<template>
  <div>
    <RecommendMovieListItem
      v-for="(movie, index) in movies"
      :key="index"
      :movie="movie"
    />
  </div>
</template>

<script>
import RecommendMovieListItem from '@/components/RecommendMovieListItem.vue'
export default {
  name: 'RecommendMovieList',
  components: {
    RecommendMovieListItem,
  },
  computed: {
    movies() {
      return this.$store.state.recommend_movie_list
    }
  }
}
</script>

<style>

</style>