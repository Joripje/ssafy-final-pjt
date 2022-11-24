<template>
  <div>
    <Flicking :options="{ align: 'prev', circular: true, bound: false, duration: 800, moveType: ['strict', { count: 5 }]}" :plugins="plugins">
      <RecommendMovieListItem
        v-for="(movie, index) in movies"
        :key="index"
        :movie="movie"
      />
    </Flicking>
    <span class="flicking-arrow-prev is-outside"></span>
    <span class="flicking-arrow-next is-outside"></span>

  </div>
</template>

<script>
import RecommendMovieListItem from '@/components/RecommendMovieListItem.vue'
import { Flicking } from "@egjs/vue-flicking"
import "@egjs/flicking-plugins/dist/arrow.css"
import { AutoPlay, Arrow } from "@egjs/flicking-plugins"

const plugins = [new AutoPlay({ duration: 5000, direction: "NEXT", stopOnHover: true, delayAfterHover:5000}), new Arrow(({ parentEl: document.body }))];

export default {
  name: 'MovieList',
  components: {
    RecommendMovieListItem,
    Flicking: Flicking,
  },
  computed: {
    movies() {
      return this.$store.state.recommend_movie_list
    }
  },
  data() {
    return {
      plugins
    }
  }
}
</script>

<style>

</style>