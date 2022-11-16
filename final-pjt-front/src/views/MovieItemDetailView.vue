<template>
  <div>
    <h1>영화 디테일 페이지입니다</h1>
    <ActorList/>
    <ReviewList/>
  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList.vue'
import ActorList from '@/components/ActorList.vue'
export default {
  components: {
    ReviewList,
    ActorList,
  }
}
</script>

<style>

</style>