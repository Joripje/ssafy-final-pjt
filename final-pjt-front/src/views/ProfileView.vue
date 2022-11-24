<template>
  <div style="padding: 40px;">
    <v-container class="col-6 mx-auto">
    <v-row justify="space-around">
      <v-card width="100%">
        <v-img class='my-0'
          height="350px"
          src="https://image.tmdb.org/t/p/original/5Iw7zQTHVRBOYpA0V6z0yypOPZh.jpg"
          gradient="to bottom, rgba(255, 255, 255, 0), rgba(255, 255, 255, .4)"
          alt=""
        >
          </v-img>

        <v-card-text>
          <div class="font-weight-bold ml-8 mb-0">
            
          </div>
                <h1> {{userInfo.username}}님 안녕하세요. </h1>
                <br>
                <PreferenceUser/>
                <br>
                <v-app id="inspire">
                  <v-row
                    justify="space-around"
                  >
                    <v-btn @click="$router.push('/watchlater')"
                      depressed
                      color="red"
                    >
                      위시리스트 보러가기
                    </v-btn>
                  </v-row>
                </v-app>
                
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