
  <!-- <div>
    <button v-if="review.user === userInfo.username" @click="deleteReview">리뷰삭제</button>
    <h1> {{ review.content }}</h1>
    <h1> {{ review.rate }}</h1>
    <hr>
  </div> -->
  <template>
    <div>
    <div>
    <v-card
      class="mx-auto"
      max-width="374"
    >
  
      <v-card-text>
        <v-row
          align="center"
          class="mx-0"
        >
          <v-rating
            :value="review.rate"
            color="amber"
            dense
            half-increments
            readonly
            size="14"
          ></v-rating>
        
        </v-row>
        <div></div>
      </v-card-text>
  
      <v-divider class="mx-4"></v-divider>
  
      <v-card-title>{{ review.content }}</v-card-title>
      
  
   
    </v-card></div>
    <p>fasdasdf</p>
  </div>
  </template>
  <script>
 

  
  export default {
    name: 'UserReviewItem',
    props: {
      review: Object,
    },
    // data() {
    //   return {
    //     content: null,
    //     rate: null,
        
    //   }
    // },
    computed: {
      userInfo() {
        return this.$store.state.user_info
      }
    },
    methods: {
      
    }
  }
  </script>
  
  <style>
  
  </style>