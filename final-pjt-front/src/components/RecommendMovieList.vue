<template>
  <div>
    <horizontal-scroll class="horizontal-scroll">
      <RecommendMovieListItem
        v-for="(movie, index) in movies"
        :key="index"
        :movie="movie"
      />
    </horizontal-scroll>
  </div>
</template>

<script>
import RecommendMovieListItem from '@/components/RecommendMovieListItem.vue'
import HorizontalScroll from 'vue-horizontal-scroll'
import 'vue-horizontal-scroll/dist/vue-horizontal-scroll.css'

export default {
  name: 'RecommendMovieList',
  components: {
    RecommendMovieListItem,
    HorizontalScroll,
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