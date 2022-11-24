<template>
  <div>
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
