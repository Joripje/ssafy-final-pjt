<template>
  <div>
    <router-link to="/watchlater">WatchLater</router-link>
    <h1>{{ userInfo }}</h1>
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
    userInfo() {
      return this.$store.state.user_info
    }
  }
}
</script>

<style>

</style>