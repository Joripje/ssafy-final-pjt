<template>
  <div>
    <h1>영화 디테일 페이지입니다</h1>
    <h1>{{ addWishListUserNumber }}</h1>
    <button @click="addToWishList">위시리스트 추가</button>
    <img :src="movieItemDetailPoster">
    <h1>{{ movieItemDetail.title }}</h1>
    <li v-for="(genre, idx) in genres" :key="idx">{{genre.name}}</li>
    <div v-if="isLoggedIn === true">
      <h1>리뷰작성</h1>
      <form>
        <label for="review_content">내용</label>
        <input type="text" v-model="review_content" id="review_content">
        <br>
        <label for="review_rate">점수</label>
        <input type="number" v-model="review_rate" id="review_rate">
        <button @click.prevent="createReview">작성하기</button>
        
      </form>
    </div>
    <h1>{{ review_content }} {{review_rate}}</h1>
    <ActorList/>
    <ReviewList/>
  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList.vue'
import ActorList from '@/components/ActorList.vue'
export default {
  name: 'MovieItemDetailView',
  data() {
    return {
      review_content: null,
      review_rate: null,
    }
  },
  components: {
    ReviewList,
    ActorList,
  },
  created() {
    this.getMovieDetail()
    this.getMovieGenre()
    this.getMovieReview()
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
    },
    createReview() {
      const review_content = this.review_content
      const review_rate = this.review_rate
      const movieId = this.$route.params.movieId
      const payload = {
        review_content: review_content,
        review_rate: review_rate,
        movieId: movieId
      }
      this.$store.dispatch('createReview', payload)
      this.review_content = null
      this.review_rate = null
    },
    getMovieReview() {
      this.$store.dispatch('getMovieReview', this.$route.params.movieId)
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
    genres() {
      return this.$store.state.genres.genres
    },
    addWishListUserNumber() {
      return this.$store.getters.addWishListUserNumber
    },
    isLoggedIn() {
      return this.$store.getters.isLoggedIn
    }
    
  }
}
</script>

<style>

</style>