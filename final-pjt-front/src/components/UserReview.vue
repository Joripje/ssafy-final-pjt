<template>
  <div class="col-8">
    <v-expansion-panels
      multiple
    >
    <v-expansion-panel>
        <v-expansion-panel-header>작성한 리뷰</v-expansion-panel-header>
        <v-expansion-panel-content>
          <UserReviewItem
            v-for="(review, index) in reviews"
            :key="index"
            :review="review"
            />
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
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


