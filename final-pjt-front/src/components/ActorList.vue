<template>
  <div>
    <h1>출연배우</h1>
    <!-- <ActorListItem
      v-for="(actor, id) in actors"
      :key="id"
      :actor="actor"
    /> -->
    <h1>{{ actors }}</h1>
    <ActorListItem/>
  </div>
</template>

<script>
import ActorListItem from '@/components/ActorListItem.vue'
export default {
  name: 'ActorList',
  components: {
    ActorListItem,
  },
  created() {
    this.getActorsWithMovieId()
    
  },
  methods: {
    getActorsWithMovieId() {
      this.$store.dispatch('getActorsWithMovieId', this.$route.params.movieId)
    },
  },
  computed: {
    
    // movieItemDetailPoster() {
    //   const BASE_URL = 'https://image.tmdb.org/t/p/w500'
    //   const poster_path = this.movieItemDetail.poster_path
    //   return BASE_URL + poster_path
    // },
    actors() {
      console.log(this.$store.state.actors)
      return this.$store.state.actors
    }
  }
}
</script>

<style>

</style>