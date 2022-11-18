<template>
  <div>
    <h1>영화 디테일 페이지입니다</h1>
    <img :src="movieItemDetailPoster">
    <h1>{{movieItemDetail.title}}</h1>
    <ActorList/>
    <ReviewList/>
  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList.vue'
import ActorList from '@/components/ActorList.vue'
export default {
  name: 'MovieItemDetailView',
  components: {
    ReviewList,
    ActorList,
  },
  created() {
    this.getMovieDetail()
  },
  methods: {
    getMovieDetail() {
      this.$store.dispatch('getMovieDetail', this.$route.params.movieId)
    },
  },
  computed: {
    movieItemDetail() {
      return this.$store.state.movieItemDetail
    },
    movieItemDetailPoster() {
      const BASE_URL = 'https://image.tmdb.org/t/p/w500'
      const poster_path = this.movieItemDetail.poster_path
      return BASE_URL + poster_path
    },
  }
}
</script>

<style>

</style>