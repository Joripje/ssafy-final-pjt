<template>
  <div>
    <br>
    <h1 style="color: white">검색 결과</h1>
    <br>
    <SearchList/>

  </div>
</template>

<script>
import SearchList from '@/components/SearchList'
export default {
  name: 'SearchView',
  components: {
    SearchList,
  }
}
</script>

<style>

</style>