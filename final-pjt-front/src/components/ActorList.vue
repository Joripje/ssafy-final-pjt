<template>
  <div>
    <h1 style="color: white; float: left;">배우목록</h1>
    <Flicking :options="{ align: 'prev', circular: false, bound: true, duration: 500, moveType: ['strict', { count: 3 }]}" :plugins="plugins">
      <ActorListItem
        v-for="(actor, id) in actors"
        :key="id"
        :actor="actor"
      />
    </Flicking>
    <span class="flicking-arrow-prev is-outside"></span>
    <span class="flicking-arrow-next is-outside"></span>
  </div>
</template>

<script>
import ActorListItem from '@/components/ActorListItem.vue'
import { AutoPlay, Arrow } from "@egjs/flicking-plugins"

const plugins = [new AutoPlay({ duration: 2500, direction: "NEXT", stopOnHover: true, delayAfterHover:500}), new Arrow(({ parentEl: document.body }))];

export default {
  name: 'ActorList',
  components: {
    ActorListItem,

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
  },
  data() {
    return {
      plugins
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