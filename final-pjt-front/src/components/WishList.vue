<template>
  <div>
    <Flicking :options="{ align: 'prev', circular: true, bound: false, duration: 500, moveType: ['strict', { count: 5 }]}" :plugins="plugins">
      <WishListItem
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
import WishListItem from '@/components/WishListItem.vue'
import { Flicking } from "@egjs/vue-flicking"
import "@egjs/flicking-plugins/dist/arrow.css"
export default {
  name: 'WishList',
  components: {
    WishListItem,
    Flicking: Flicking,
  },
  computed: {
    movies() {
      return this.$store.state.movie_list
    }
  },
  data() {
    return {
    }
  }
}
</script>

<style>

</style>