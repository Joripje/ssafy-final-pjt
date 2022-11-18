<template>
  <div>
    <!-- <img :src="actorProfile">
    <h1>{{ actor.name }}</h1> -->
  </div>
</template>

<script>
export default {
  name: 'ActorListItem',
  props: {
    // actor: Object,
  },
  computed: {
    actorDetail() {
      return this.$store.state.actors
    },
    actorProfile() {
      const BASE_URL = 'https://image.tmdb.org/t/p/w500'
      const profile_path = this.actor.profile_path
      return BASE_URL + profile_path
    },
  },
  methods: {
    
  }
}
</script>

<style>

</style>