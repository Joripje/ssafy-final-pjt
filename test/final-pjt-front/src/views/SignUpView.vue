<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="email">email : </label>
      <input type="text" id="email" v-model="email"><br>

      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      email: null,
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const email = this.email
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        // email,
        // password1,
        // password2,
        email: email,
        username: username,
        password1: password1,
        password2: password2,
      }

      this.$store.dispatch('signUp', payload)
      this.$router.push({ name: 'home'})
    }
  }
}
</script>
