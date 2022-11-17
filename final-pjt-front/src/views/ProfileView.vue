<template>
  <div>
    <router-link to="/watchlater">WatchLater</router-link>
    <h1>{{ userDetail.username }}</h1>
    <img :src="userImage">
    <h1></h1>
    <PreferenceUser/>
    <ReviewList/>
  </div>
</template>

<script>
import PreferenceUser from '@/components/PreferenceUser.vue'
import ReviewList from '@/components/ReviewList.vue'

export default {
  name: 'ProfileView',
  components: {
    PreferenceUser,
    ReviewList,
  },
  computed: {
    userDetail() {
      return this.$store.state.userDetail
    },
    userImage() {
      return this.$store.state.userDetail.user_image
    }
  }
}
</script>

<style>

</style>