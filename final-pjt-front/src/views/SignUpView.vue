<template>
  <div id="app" style="padding: 40px;">
  <v-app id="inspire">
    <v-card
      class="mx-auto"
      width="400"
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
            <v-text-field @keyup.enter="step++"
              label="Email"
              v-model="email"
            ></v-text-field>
            <span class="text-caption grey--text text--darken-1">
              Please enter an e-mail for your account
            </span>
          </v-card-text>
        </v-window-item>
  
        <v-window-item :value="2">
          <v-card-text>
            <v-text-field
              label="Password"
              type="password"
              v-model="password1"
            ></v-text-field>
            <v-text-field @keyup.enter="step++"
              label="Confirm Password"
              type="password"
              v-model="password2"
            ></v-text-field>
            <span class="text-caption grey--text text--darken-1">
              Please enter a password for your account
            </span>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="3">
          <v-card-text>
            <v-text-field @keyup.enter="signUp"
              label="username"
              v-model="username"
            ></v-text-field>
            <span class="text-caption grey--text text--darken-1">
              Please enter an username for your account
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
          v-if="step !== 3"
          color="primary"
          depressed
          @click="step++"
        >
          Next
        </v-btn>
        <v-btn
          v-if="step === 3"
          color="primary"
          depressed
          @click="signUp"
        >
          SIGNUP
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-app>
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
      step: 1,
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
    }
  },
  computed: {
      currentTitle () {
        switch (this.step) {
          case 1: return 'Sign-up'
          case 2: return 'Create a password'
          case 3: return 'Create a username'
          default: return 'Account created'
        }
      },
  },
}
</script>
