<template>
  <div>
    <router-link to="/watchlater">WatchLater</router-link>
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
}
</script>

<style>

</style>