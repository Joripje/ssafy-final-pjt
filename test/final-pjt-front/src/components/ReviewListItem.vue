<template>
  <div>
    <button v-if="review.user === userInfo.username" @click="deleteReview">리뷰삭제</button>
    <!-- <button v-if="review.user === userInfo.username" @click="updateReview">리뷰수정</button> -->
    <h1> {{ review.content }}</h1>
    <h1> {{ review.rate }}</h1>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewListItem',
  props: {
    review: Object,
  },
  // data() {
  //   return {
  //     content: null,
  //     rate: null,
      
  //   }
  // },
  computed: {
    userInfo() {
      return this.$store.state.user_info
    }
  },
  methods: {
    deleteReview() {
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/movies/review/${this.review.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(res => {
          console.log(res)
          this.$store.dispatch('getMovieReview', this.review.movie)
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>