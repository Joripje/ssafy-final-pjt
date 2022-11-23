<template>
  <div>
    <horizontal-scroll class="horizontal-scroll">
      <MovieListItem
        v-for="(movie, index) in movies"
        :key="index"
        :movie="movie"
      />
    </horizontal-scroll>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'
import HorizontalScroll from 'vue-horizontal-scroll'
import 'vue-horizontal-scroll/dist/vue-horizontal-scroll.css'

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
    HorizontalScroll,
  },
  computed: {
    movies() {
      return this.$store.state.movie_list
    }
  }
}
</script>

<style>
.horizontal-scroll {
    display: flex;
    width: 100%;
    height: 500pt;
    margin: 10pt;
    border: solid 2px #2c3e50;
}
</style>