<template>
  <div>
    <SearchListItem
        v-for="(movie, index) in movies"
        :key="index"
        :movie="movie"
      />
  </div>
</template>

<script>
import SearchListItem from '@/components/SearchListItem';

export default {
  name: 'SearchList',
  components: {
    SearchListItem,
  }

}
</script>

<style>

</style>