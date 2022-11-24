<template>
  <div>
    <div class="card mb-3" style="max-width: 60%;">
      <div class="row g-0">
        <div class="col-md-4">
          <img @click="goToDetail" style="cursor: pointer" :src="moviePoster" class="img-fluid rounded-start" alt="">
        </div>
        <div class="col-md-8">
          <div class="card-body">
            <h3 @click="goToDetail" style="cursor: pointer" class="card-title my-3">{{ movie.title }}</h3>
            <p class="card-text"><small class="text-muted">
              <v-row align="center" class="mx-0">
                          <v-rating :value="movie.vote_average / 2" color="amber" dense half-increments readonly size="14">{{ movie.vote_average }}</v-rating>
                            
                            </v-row>

            </small></p>
            <p class="card-text">{{ movie.overview }}</p>
            <v-card-text
              class="pt-6"
              
            >
          <v-btn @click="addToWishList"
            absolute
            color="red"
            class="white--text"
            fab
            right
            bottom
            min-height="pt-5"
          >
            <v-icon>mdi-plus</v-icon>
          </v-btn>
        </v-card-text>
          </div>
        </div>
      </div>
    </div>
    <br>
  </div>
</template>

<script>
export default {
  name: 'SearchListItem',
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
  methods: {
    goToDetail() {
      
      this.$router.push({ name: 'movieitemdetail', params: { movieId: this.movie.id } })
    },
    addToWishList() {
      this.$store.dispatch('addToWishList', this.movie.id)
    },
  }
}
</script>

<style>

</style>