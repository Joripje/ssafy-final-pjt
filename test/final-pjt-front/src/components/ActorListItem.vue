<template>
  <div>
    <img :src="actorProfile">
    <h1>{{ actor.name }}</h1>
  </div>
</template>

<script>
export default {
  name: 'ActorListItem',
  props: {
    actor: Object,
  },
  computed: {
    actorProfile() {
      const BASE_URL = 'https://image.tmdb.org/t/p/w200'
      const profile_path = this.actor.profile_path
      if (profile_path === null) {
        return 'data:image/png;base64,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'
      }
      return BASE_URL + profile_path
    },
  },
  methods: {
    
  }
}
</script>

<style>

</style>