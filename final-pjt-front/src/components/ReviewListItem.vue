<template>
  <v-card
    class="mx-5 my-12"
    max-width="500"
  >

    <v-card-text>
      <v-row
        align="center"
        class="mx-0"
      >
        <v-rating
          :value="review.rate"
          color="amber"
          dense
          half-increments
          readonly
          size="14"
        ></v-rating>
        <v-btn @click="deleteReview" v-if="review.user === userInfo.username"
          absolute
          color="red"
          class="white--text"
          fab
          right
          center
        >
          <v-icon>mdi-delete</v-icon>
        </v-btn>

        <div class="grey--text ms-4">
          {{ review.user }}
        </div>
      </v-row>
    </v-card-text>
    <v-divider class="mx-4"></v-divider>
    <v-card-title>{{ review.content }}</v-card-title>
  </v-card>
</template>
<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewListItem',
  props: {
    review: Object,
  },
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