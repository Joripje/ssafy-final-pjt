<template>
  <div>
    <horizontal-scroll class="horizontal-scroll" style="overflow-x:hidden">
      <MovieListItem
        v-for="(movie, index) in movies"
        :key="index"
        :movie="movie"
      />
    </horizontal-scroll>
    <Flicking :options="{ circular: true }">
      <div style="width: 120px;">1</div>
      <div style="width: 20%;">2</div>
      <div style="width: 500px;">3</div>
      <div style="width: 300px;">4</div>
      <div style="width: 100%;">5</div>
    </Flicking>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'
import HorizontalScroll from 'vue-horizontal-scroll'
import 'vue-horizontal-scroll/dist/vue-horizontal-scroll.css'
import Flicking from "@egjs/vue-flicking";

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
    HorizontalScroll,
    Flicking,
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
    height: 350pt;
    margin: 10pt;
    border: none;
}
</style>