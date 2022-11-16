<template>
  <div>
    <router-link to="/watchlater">WatchLater</router-link>
    <h1>프로필화면 입니다</h1>
    <PreferenceUser/>
    <ReviewList/>
  </div>
</template>

<script>
import PreferenceUser from '@/components/PreferenceUser.vue'
import ReviewList from '@/components/ReviewList.vue'
export default {
  components: {
    PreferenceUser,
    ReviewList,
  }
}
</script>

<style>

</style>