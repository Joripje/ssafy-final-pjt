<template>
  <div>
    <h1>출연배우</h1>
    <ActorListItem
      v-for="(actor, id) in actors"
      :key="id"
      :actor="actor"
    />
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
    actors() {
      return this.$store.state.actors.actors
    }
  }
}
</script>

<style>

</style>