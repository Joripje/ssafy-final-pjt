<template>
  <div id="app" style="padding: 40px;">
    <v-app id="inspire">
      <v-container class="black">
        <v-row no-gutters>
          <v-col
            cols="12"
            sm="6"
            md="6"
          >
            
            <div>
              <div align ="center">
                <v-card
                  class="mx-5 my-7"
                  max-width="500"
                >
                  <v-img
                    height=100%
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
              </div>

              <!-- 위시리스트 추가 버튼 -->
              <div id="app" style="padding: 0px; height: 30px;">
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
          </v-col>
          <v-col
            cols="6"
            md="6"
          >
            <v-app id="inspire">
              <v-card
                class="elevation-16 mx-5 mt-7"
                width="500"
                
              >
                <v-card-title class="text-h5">
                  리뷰 작성
                </v-card-title>
                <v-textarea
                  style="width: 500px; height: 150px;"
                  class="mx-5"
                  label="리뷰 내용을 적어주세요"
                  v-model="review_content"
                  
                >

                </v-textarea>
                <v-card-text>
                  <div class="text-center mt-0">
                    <v-rating
                      v-model="review_rating"
                      color="yellow darken-3"
                      background-color="grey"
                      empty-icon="$ratingFull"
                      half-increments
                      hover
                      large
                    ></v-rating>
                  </div>
                </v-card-text>
                <v-card-actions class="justify-space-between">
                  <v-btn  
                    @click="createReview"
                    color="primary"
                    text
                  >
                    리뷰 제출
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-app>
            <!-- 장르 표기 -->
            <v-app id="inspire">
              <v-card
                class="mx-5 my-5"
                width="500"
              >
                <v-list dense>
                  <v-subheader>장르</v-subheader>
                  <v-list-item-group >
                    <v-list-item
                      v-for="(genre, idx) in genres"
                      :key="idx"
                    >
                      <v-list-item-content>
                        <v-list-item-title v-text="genre.name"></v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list-item-group>
                </v-list>
              </v-card>
            </v-app>
            <h1 class="mx-5" style="color: white; float:left;">리뷰 목록</h1>
            <ReviewList/>
          </v-col>
        </v-row>
      </v-container>
    </v-app>
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
      review_rating: null,
    }
  },
  components: {
    ReviewList,
    ActorList,
  },
  computed: {
    review_rate() {
      return this.review_rating * 2
    },
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
      this.review_rating = null
    },
    getMovieReview() {
      this.$store.dispatch('getMovieReview', this.$route.params.movieId)
    },
  },
}
</script>

<style>
.div {
  background-color: black;
}
</style>