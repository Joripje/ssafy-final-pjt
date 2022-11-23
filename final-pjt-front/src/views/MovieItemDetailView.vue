<template>
  <div align ="center">
    <v-card
      class="mx-auto my-12"
      max-width="374"
    >
    <v-img
      height="250"
      :src="movieItemDetailPoster"
    ></v-img>
    <v-card-title>{{ movieItemDetail.title }}</v-card-title>
    <v-card-text>
      <v-row
        align="center"
        class="mx-0"
      >
      <v-rating :value="movieItemDetail.vote_average / 2" color="amber" dense half-increments readonly size="14"></v-rating>
        <div>
          {{ movieItemDetail.vote_average }}
          <br>
          <br>
        </div>
      </v-row>
      <div>{{ movieItemDetail.overview }}</div>
    </v-card-text>
  </v-card>


  <!-- 위시리스트 추가 버튼 -->
  <div id="app">
    <v-app id="inspire">
      <v-row
        justify="space-around"
      >
        <v-btn @click="addToWishList"
          depressed
          color="red"
        >
          위시리스트에 추가
        </v-btn>
      </v-row>
    </v-app>
  </div>

<!-- 리뷰 작성 -->

  <div id="app">
    <v-app id="inspire">
      <v-card
        class="mx-auto elevation-20"
        color="red"
        dark
        style="width: 800px; height: 400px;"
      >
        <v-card-actions class="pa-4">
          리뷰를 작성해주세요
          <v-spacer></v-spacer>
          <span class="text--lighten-2 text-caption mr-2">
            ({{ review_rate }})
          </span>
          <v-rating
            v-model="review_rate"
            background-color="white"
            color="yellow accent-4"
            dense
            half-increments
            hover
            size="18"
          ></v-rating>
          <input type="text" v-model="review_content" id="review_content">
          <!-- <br><br>
          <v-container>
            <v-row>
              <v-col
                cols="12"
                md="6"
              >
                <v-textarea
                  solo
                  name="input-7-4"
                  label="Solo textarea"
                ></v-textarea>
              </v-col>
            </v-row>
          </v-container> -->
        </v-card-actions>
        
      </v-card>
  </v-app>
</div>


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