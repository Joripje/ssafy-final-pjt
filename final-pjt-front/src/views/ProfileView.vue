<template>
  <div>
    <v-container class="col-6 mx-auto">
    <v-row justify="space-around">
      <v-card width="100%">
        <v-img
          height="350px"
          src="https://image.tmdb.org/t/p/original/5Iw7zQTHVRBOYpA0V6z0yypOPZh.jpg"
          alt=""
        >
          </v-img>

        <v-card-text>
          <div class="font-weight-bold ml-8 mb-2">
            
          </div>

                
                <h1> {{userInfo.username}}님 안녕하세요. </h1>
                <br>
                <PreferenceUser/>
                <br>
                <router-link to="/watchlater">위시리스트 확인</router-link>
                <br>
                <br>
                <div align="center">
                  <UserReview/>
                </div>
              
                <div class="font-weight-normal">
    
              </div>
            
          
        </v-card-text>
      </v-card>
    </v-row>
  </v-container>
  
    
  </div>
</template>

<script>
import PreferenceUser from '@/components/PreferenceUser.vue'
import UserReview from '@/components/UserReview.vue'

export default {
  name: 'ProfileView',
  components: {
    PreferenceUser,
    UserReview,
  },
  computed: {
    userInfo() {
      return this.$store.state.user_info
    },
    
  },
  methods: {
    movieImage() {
      const BASE_URL = 'https://image.tmdb.org/t/p/original'
      const poster_path = this.$store.state.movieItemDetail[0].backdrop_path
      
      console.log(poster_path)
      return BASE_URL + poster_path
    },
  }
}
</script>

<style>

</style>