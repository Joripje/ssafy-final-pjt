<template>
      <div id="app">
    <v-app id="inspire">
    <v-card
      class="mx-auto my-12"
      max-width="374"
      @click="goToDetail"
    >
      <template slot="progress">
        <v-progress-linear
          color="deep-purple"
          height="10"
          indeterminate
        ></v-progress-linear>
      </template>
  
      <v-img
        height="250"
        :src="moviePoster"
      ></v-img>
  
      <v-card-title>{{ movie.title }}</v-card-title>
  
      <v-card-text>
        <v-row
          align="center"
          class="mx-0"
        >
          <v-rating
            :value="vote_average / 2"
            color="amber"
            dense
            half-increments
            readonly
            size="14"
          ></v-rating>
  
          <div class="grey--text ms-4">
            {{ movie.vote_average }}
          </div>
        </v-row>
  
        <div class="my-4 text-subtitle-1">
          <li v-for="(genre, idx) in genres" :key="idx">{{genre.name}}</li>
        </div>
  
        <div>{{ movie.overview }}</div>
      </v-card-text>
  
      <v-divider class="mx-4"></v-divider>
    </v-card>
  </v-app>
</div>
</template>

<script>
export default {
  name: 'RecommendMovieListItem',
  props: {
    movie: Object,
  },
  computed: {
    moviePoster() {
      const BASE_URL = 'https://image.tmdb.org/t/p/w500'
      const poster_path = this.movie.poster_path
      return BASE_URL + poster_path
    },
  },
  data() {
    return {
      vote_average: this.movie.vote_average
    }
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