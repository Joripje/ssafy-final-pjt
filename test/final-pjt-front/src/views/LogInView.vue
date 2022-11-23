<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent="logIn">
      <label for="email">email :</label>
      <input type="text" id="email" v-model="email">
      <br>
      <label for="password">password :</label>
      <input type="password" id="password" v-model="password">
      <br>
      <input type="submit" value="logIn">
    </form>
  </div>
</template>

<script>

export default {
  name: 'LogInView',
  data() {
    return {
      email: null,
      password: null,
      user_info: null,
    }
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn
    }
  },
  methods: {
    logIn() {
      const email = this.email
      const password = this.password
      const payload = {
        email, password
      }
      this.$store.dispatch('logIn', payload)
      if (this.isLoggedIn === true) {
        this.$router.push({ name: 'home'})

      }
    },
  },

}
</script>

<style>

</style>