<template>
  <div id="app">
    <nav>
      <!-- 로그인 상태일때는 로그아웃 라우터 링크가 표시되도록 작성 -->
      <router-link to="/">Home</router-link>
      <router-link to="/Search">Search</router-link> 
      <router-link v-if="isLoggedIn === false" to="/SignUp">SignUp</router-link> 
      <router-link v-if="isLoggedIn === false" to="/LogIn">LogIn</router-link> 
      <router-link v-if="isLoggedIn === true" to="/Profile">Profile</router-link>
      <button v-if="isLoggedIn === true" @click="logOut">logout</button>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn
    }
  },
  created() {
    this.getMovieList()
  },
  methods: {
    logOut() {
      this.$store.dispatch('logOut')
    },
    getMovieList() {
      this.$store.dispatch('getMovieList')
    }
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
