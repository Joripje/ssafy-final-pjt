<template>
  <div>
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
    <div id="app" style="padding: 20px; height: 50px;">
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
  </div>
  <div id="app" style="height: 200px;">
    <v-app id="inspire" style="height: 200px;">
      <v-card
        class="mx-auto elevation-20"
        color="red"
        dark
        style="width: 400px; "
      >
        <v-row justify="space-between">
          <v-col cols="8">
            <v-card-title>
              <div>
                <v-app id="inspire" style="height: 150px;">
                  <v-container fluid>
                    <v-row>
                      
                        <v-textarea
                          style="width: 370px; height: 300px;"
                          solo
                          name="input-7-4"
                          label="Solo textarea"
                          v-model="review_content"
                          background-color="red"
                        ></v-textarea>
                      
                    </v-row>
                  </v-container>
                </v-app>
                
              </div>
            </v-card-title>
          </v-col>
        </v-row>
        <v-divider dark></v-divider>
        <v-card-actions class="pa-4">
          <v-btn @click="createReview"
            
            color="red"
          >
            리뷰 작성
          </v-btn>
          <v-spacer></v-spacer>
          <span class="grey--text text--lighten-2 text-caption mr-2">
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
        </v-card-actions>
      </v-card>
    </v-app>
  </div>
    <li v-for="(genre, idx) in genres" :key="idx">{{genre.name}}</li>
    <ReviewList/>
    <ActorList/>
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
      if(this.isLoggedIn !== true) {
        alert('리뷰를 작성하려면 로그인이 필요합니다')
        this.$router.push({ name: 'login'})
      }
      this.$store.dispatch('addToWishList', this.$route.params.movieId)
    },
    createReview() {
      if(this.isLoggedIn !== true) {
        alert('리뷰를 작성하려면 로그인이 필요합니다')
        this.$router.push({ name: 'login'})
      }
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
}
</script>

<style>

</style>