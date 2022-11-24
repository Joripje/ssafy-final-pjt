<template>
  <div>
    <Flicking :options="{ align: 'prev', circular: true, bound: false, duration: 500, moveType: ['strict', { count: 5 }]}" :plugins="plugins">
      <MovieListItem
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
import MovieListItem from '@/components/MovieListItem.vue'
import { Flicking } from "@egjs/vue-flicking"
import "@egjs/flicking-plugins/dist/arrow.css"
import { AutoPlay, Arrow } from "@egjs/flicking-plugins"

const plugins = [new AutoPlay({ duration: 2500, direction: "NEXT", stopOnHover: true, delayAfterHover:500}), new Arrow(({ parentEl: document.body }))];

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
    Flicking: Flicking,
  },
  computed: {
    movies() {
      return this.$store.state.movie_list
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