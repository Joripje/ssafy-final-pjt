<template>
  <div>
    <TrendingMovie style="height: 400pt"/>
    <RecommendMovie v-if="isLoggedIn === true" style="height: 200pt"/>
    
  </div>

  
</template>

<script>
import RecommendMovie from '@/components/RecommendMovie.vue'
import TrendingMovie from '@/components/TrendingMovie.vue'
export default {
  name: 'HomeView',
  components: { 
    RecommendMovie,
    TrendingMovie
  },
  computed: {
    userinfo(){
      return this.$store.state.user_info
    },
    isLoggedIn() {
      return this.$store.getters.isLoggedIn
    }
  },
  created() {
  this.$store.dispatch('getMovieList')
  this.$store.dispatch('getRecommendMovie')
}
}
</script>

<style>

</style>