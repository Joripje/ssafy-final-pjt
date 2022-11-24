<template>
  <div id="app">
    <v-app id="inspire" style="height: 50px;">
      <v-card style="height: 100px;">
        <v-app-bar
          absolute
          color="red"
          dark
          scroll-target="#scrolling-techniques-2"
          style="height: 50px;"
        >
    
          <v-app-bar-title style="height: 30px;">나의PS파트너</v-app-bar-title>
    
          <v-spacer></v-spacer>
    
          <v-btn icon @click="$router.push('/search')">
            <v-icon>mdi-magnify</v-icon>
          </v-btn>
    
          <v-btn icon @click="$router.push('/')">
            <v-icon>mdi-home</v-icon>
          </v-btn>
    
          <v-btn v-if="isLoggedIn === true" icon @click="$router.push('/profile')">
            <v-icon>mdi-account-box</v-icon>
          </v-btn>

          <v-btn v-if="isLoggedIn === false" icon @click="$router.push('/login')">
            <v-icon>mdi-login</v-icon>
          </v-btn>

          <v-btn v-if="isLoggedIn === true" icon @click="logOut">
            <v-icon>mdi-logout</v-icon>
          </v-btn>

        </v-app-bar>
        <v-sheet
          id="scrolling-techniques-2"
          class="overflow-y-auto"
          max-height="600"
        >
          <v-container style="height: 50px;"></v-container>
        </v-sheet>
      </v-card>
    </v-app>
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
  background-color: black;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}
</style>
