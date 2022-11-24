<template>

  <div id="app">
    <v-app id="inspire" style="height: 100px;">
      <v-card style="height: 100px;">
        <v-app-bar
          absolute
          color="red"
          style="height: 100px;"
          src="../assets/navbar.png"
        >
          <img @click="$router.push('/')" class="mr-3 mt-9" :src="require('@/assets/navbar.png')" height="100"/>
          <v-spacer></v-spacer>
    
          <v-form @submit.prevent="search" class="mt-12">
            <v-container>
              <v-row>         
                <v-col
                  cols="12"
                  sm="12"
                  md="12"
                >
                  <v-text-field
                    v-model="inputData"
                    label="검색"
                    append-icon="mdi-magnify"
                  ></v-text-field>
      
                </v-col>
              </v-row>
            </v-container>
          </v-form>
          <v-btn icon @click="$router.push('/')" class="mt-9">
            <v-icon>mdi-home</v-icon>
          </v-btn>
    
          <v-btn v-if="isLoggedIn === true" icon @click="$router.push('/profile')" class="mt-9">
            <v-icon>mdi-account-box</v-icon>
          </v-btn>

          <v-btn v-if="isLoggedIn === false" icon @click="$router.push('/login')" class="mt-9">
            <v-icon>mdi-login</v-icon>
          </v-btn>

          <v-btn v-if="isLoggedIn === true" icon @click="logOut" class="mt-9">
            <v-icon>mdi-logout</v-icon>
          </v-btn>

        </v-app-bar>
      </v-card>
    </v-app>
    <router-view/>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputData: null
    }
  },
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
    },
    search() {
      // console.log(this.inputData)
      // this.inputData = this.inputData
      this.$store.dispatch('searchMovies', this.inputData)
      this.$router.push({name: 'search', params: {keyWord: this.inputData}})
      this.inputData = null
    },
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
