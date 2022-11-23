<template>
  <div>
    <h1>선호도입니다</h1>
    <div class="small">
    <DoughnutChart :chart-data="dataCollection"></DoughnutChart>
    <button @click="fillData()">Randomize</button>
  </div>
  </div>
</template>

<script>
import DoughnutChart from '@/components/DoughnutChart'

export default {
  name: 'PreferenceUser',
  components: {
    DoughnutChart,
  },
  data() {
    return {
      dataCollection: null,
    };
  },
  created() {
    this.fillData();
  },
  methods: {
    fillData() {
      this.dataCollection = {
        labels: [this.getRandomInt(), this.getRandomInt()],
        datasets: [
          {
            label: 'Main One',
            backgroundColor: '#f87979',
            data: [this.getRandomInt(), this.getRandomInt()],
          }, {
            label: 'Main One',
            backgroundColor: '#f87979',
            data: [this.getRandomInt(), this.getRandomInt()],
          },
        ],
      };
      console.log('ChartTestMain', this.dataCollection);
    },
    getRandomInt() {
      return Math.floor(Math.random() * (50 - 4)) + 5;
    },
  },
}
</script>

<style>
.small {
    max-width: 600px;
    margin:  150px auto;
  }
</style>