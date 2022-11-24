<template>
  <div>
    <h2>선호 장르</h2>
    <br>
    <DoughnutChart
    :preferList='preferList'/>
  </div>
</template>

<script>
import DoughnutChart from '@/components/DoughnutChart'

export default {
  name: 'PreferenceUser',
  components: {
    DoughnutChart
  },
  data() {
    return {
      preferList: null
    }
  },
  created() {
    this.getPreferList()
  },
  methods: {
    getPreferList() {
      this.$store.dispatch('getPreferList')
      this.preferList = this.$store.state.prefer_list
    }
  }
}
</script>
