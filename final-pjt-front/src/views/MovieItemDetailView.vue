<template>
  <div>
    <h1>영화 디테일 페이지입니다</h1>
    <button @click="addToWishList">위시리스트 추가</button>
    <img :src="movieItemDetailPoster">
    <h1>{{ movieItemDetail.title }}</h1>
    <li v-for="(genre, idx) in genres" :key="idx">{{genre.name}}</li>
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
    this.getMovieGenre()
  },
  methods: {
    getMovieDetail() {
      this.$store.dispatch('getMovieDetail', this.$route.params.movieId)
    },
    getMovieGenre() {
      this.$store.dispatch('getMovieGenre', this.$route.params.movieId)
    },
    addToWishList() {
      this.$store.dispatch('addToWishList', this.$route.params.movieId)
    }
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
    genres() {
      return this.$store.state.genres.genres
    }
  }
}
</script>

<style>

</style>