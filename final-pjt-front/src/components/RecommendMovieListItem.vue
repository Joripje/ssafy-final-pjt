<template>
  <div id="app">
  <v-app id="inspire">
    <v-hover v-slot="{ hover }">
      <v-card
        class="mx-1"
        color="grey lighten-4"
        width="300"
      >
        <v-img
          :aspect-ratio="3/4"
          :src="moviePoster"
        >
          <v-expand-transition>
            <div
              v-if="hover"
              class="d-flex v-card--reveal"
              style="height: 100%;"
            >
              

              <v-row align="center" justify="center">
                <v-col cols="12">
                  <v-hover v-slot="{ hover }">
                    <v-card @click="goToDetail" class="mx-auto my-12" max-width="374" :elevation="hover ? 12 : 2">
                      <template slot="progress">
                        <v-progress-linear color="deep-purple" height="10" indeterminate></v-progress-linear>
                      </template>
                      
                      <v-card-title>{{ movie.title }}</v-card-title>
                      <v-card-text>
                        <v-row align="center" class="mx-0">
                          <v-rating :value="vote_average / 2" color="amber" dense half-increments readonly size="14"></v-rating>
                          <div>
                            {{ vote_average }}
                            <br>
                            <br>
                          </div>
                        </v-row>
                        <div>
                          {{ movie.overview }}
                        </div>
                        </v-card-text>
                      </v-card>         
                  </v-hover>
                </v-col>
              </v-row>


            </div>
          </v-expand-transition>
        </v-img>
        <v-card-text
          class="pt-6"
          style="position: relative;"
        >
          <v-btn @click="addToWishList"
            absolute
            color="red"
            class="white--text"
            fab
            right
            top
          >
            <v-icon>mdi-plus</v-icon>
          </v-btn>
          
        </v-card-text>
      </v-card>
    </v-hover>
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
    },
    addToWishList() {
      this.$store.dispatch('addToWishList', this.movie.id)
    },
  }
}
</script>

<style>

</style>