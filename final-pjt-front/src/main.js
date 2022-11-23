import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Vuetify from 'vuetify' //Vuetify 1
import 'vuetify/dist/vuetify.min.css' //Vuetify 2

Vue.config.productionTip = false
Vue.use(Vuetify) //Vuetify 3


new Vue({
  router,
  store,
  vuetify: new Vuetify(), //Vuetify 4
  render: h => h(App)
}).$mount('#app')
