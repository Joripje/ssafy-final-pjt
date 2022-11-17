<template>
  <div>
    <h1>영화 디테일 페이지입니다</h1>
    <h1 @click="addToWishlist">누르면 위시리스트에 추가</h1>
    <ActorList/>
    <ReviewList/>
  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList.vue'
import ActorList from '@/components/ActorList.vue'
export default {
  name: 'MovieItemDetailView',
  components: {
    ReviewList,
    ActorList,
  },
  methods: {
    addToWishlist() {
      this.$store.dispatch('addToWishList', this.movie.id)
    }
  }
}
</script>

<style>

</style>