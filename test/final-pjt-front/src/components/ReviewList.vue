<template>
  <div>
    <ReviewListItem
    v-for="(review, index) in reviews"
    :key="index"
    :review="review"
    />
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem.vue'
export default {
  name: 'ReviewList',
  components: {
    ReviewListItem,
  },
  computed: {
    reviews() {
      return this.$store.state.movie_review
    }
  }
}
</script>

<style>

</style>


