<template>
  <div style="padding: 40px;">
    <h1 style="color: white; float: left;">위시리스트</h1>
    <WishList/>
  </div>
</template>

<script>
import WishList from '@/components/WishList.vue'
export default {
  name: 'WatchLaterView',
  components: {
    WishList,
  }
}
</script>

<style>

</style>