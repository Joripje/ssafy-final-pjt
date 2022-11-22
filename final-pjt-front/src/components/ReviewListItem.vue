<template>
  <div>
    <h1> {{ review.content }}</h1>
    <h1> {{ review.rate }}</h1>
  </div>
</template>

<script>
export default {
  name: 'ReviewListItem',
  props: {
    review: Object,
  },
  
}
</script>

<style>

</style>