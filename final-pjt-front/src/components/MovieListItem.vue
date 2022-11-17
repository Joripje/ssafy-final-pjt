<template>
  <div>
    <h1>{{ movie.title }}</h1>
    <img :src="moviePoster" @click="goToDetail">
    <br>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  },
  computed: {
    movieDetail() {
      return this.$store.state.movieDetail
    },
    moviePoster() {
      const BASE_URL = 'https://image.tmdb.org/t/p/w500'
      const poster_path = this.movie.poster_path
      return BASE_URL + poster_path
    },
  },
  methods: {
    goToDetail() {
      
      this.$router.push({ name: 'movieitemdetail', params: { movieId: this.movie.id } })
    }
  }
}
</script>

<style>

</style>