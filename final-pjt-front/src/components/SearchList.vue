<template>
  <div>
    <div align="center">
    <SearchListItem
      v-for="(movie, index) in movies"
      :key="index"
      :movie="movie"
    />
    <v-divider></v-divider>
  </div>
  </div>
</template>

<script>
import SearchListItem from '@/components/SearchListItem';

export default {
  name: 'SearchList',
  components: {
    SearchListItem,
  },
  computed: {
    movies() {
      return this.$store.state.movie_list
    }
  },

}
</script>

<style>

</style>