<template>
  <div>
    <h1>기본화면 입니다</h1>
    <TrendingMovie/>
    <RecommendMovie/>
    <h1>{{ userinfo }}</h1>
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
    }
  },

}
</script>

<style>

</style>