<template>
  <div>
    <h1 style="color: white; float: left;">배우목록</h1>
    <horizontal-scroll class="horizontal-scroll" style="overflow-x:hidden">
      <ActorListItem
        v-for="(actor, id) in actors"
        :key="id"
        :actor="actor"
      />
    </horizontal-scroll>
  </div>
</template>

<script>
import ActorListItem from '@/components/ActorListItem.vue'
import HorizontalScroll from 'vue-horizontal-scroll'
import 'vue-horizontal-scroll/dist/vue-horizontal-scroll.css'

export default {
  name: 'ActorList',
  components: {
    ActorListItem,
    HorizontalScroll,
  },
  created() {
    this.getActorsWithMovieId()
    
  },
  methods: {
    getActorsWithMovieId() {
      this.$store.dispatch('getActorsWithMovieId', this.$route.params.movieId)
    },
  },
  computed: {
    actors() {
      return this.$store.state.actors.actors
    }
  }
}
</script>

<style>
.horizontal-scroll {
    display: flex;
    width: 100%;
    height: 250pt;
    margin: 10pt;
    border: none;
}
</style>