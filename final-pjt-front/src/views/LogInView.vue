
  <!-- <div>
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
  </div> -->
<template>
  <div id="app">
  <v-app id="inspire">
    <v-card
      class="mx-auto"
      max-width="500"
    >
      <v-card-title class="text-h6 font-weight-regular justify-space-between">
        <span>{{ currentTitle }}</span>
        <v-avatar
          color="primary lighten-2"
          class="subheading white--text"
          size="24"
          v-text="step"
        ></v-avatar>
      </v-card-title>
  
      <v-window v-model="step">
        <v-window-item :value="1">
          <v-card-text>
            <v-text-field
              label="Email"
              v-model="email"
            ></v-text-field>
            <span class="text-caption grey--text text--darken-1">
              Please enter an e-mail for Log-in
            </span>
          </v-card-text>
        </v-window-item>
  
        <v-window-item :value="2">
          <v-card-text>
            <v-text-field
              label="Password"
              type="password"
              v-model="password"
            ></v-text-field>
            <span class="text-caption grey--text text--darken-1">
              Please enter a password for Log-in
            </span>
          </v-card-text>
        </v-window-item>
      </v-window>
  
      <v-divider></v-divider>
  
      <v-card-actions>
        <v-btn
          :disabled="step === 1"
          text
          @click="step--"
        >
          Back
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn
          v-if="step === 1"
          color="primary"
          depressed
          @click="step++"
        >
          Next
        </v-btn>
        <v-btn
          v-if="step !== 1"
          color="primary"
          depressed
          @click="logIn"
        >
          LOGIN
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-app>
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
      step: 1,
    }
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn
    },
    currentTitle () {
        switch (this.step) {
          case 1: return '로그인'
          case 2: return '비밀번호 입력'
          case 3: return 'Create a username'
          default: return 'Account created'
        }
    },
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