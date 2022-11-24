<template>
  <div>
    <UserReviewItem
    v-for="(review, index) in reviews"
    :key="index"
    :review="review"
    />
  </div>
</template>

<script>
import UserReviewItem from '@/components/UserReviewItem.vue'
export default {
  name: 'UserReview',
  components: {
    UserReviewItem,
  },
  computed: {
    reviews() {
      return this.$store.state.user_review
    }
  },
  created() {
    this.getUserReview()
  },
  methods: {
    getUserReview() {
      this.$store.dispatch('getUserReview')
      console.log(this.reviews)
    }
  }

}
</script>

<style>

</style>


