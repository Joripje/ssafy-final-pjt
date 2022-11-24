import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Vuetify from 'vuetify' //Vuetify 1
import 'vuetify/dist/vuetify.min.css' //Vuetify 2
import Flicking from "@egjs/vue-flicking";
import "@egjs/vue-flicking/dist/flicking.css";
// Or, if you have to support IE9
import "@egjs/vue-flicking/dist/flicking-inline.css";

Vue.config.productionTip = false
Vue.use(Vuetify) //Vuetify 3
Vue.use(Flicking)

new Vue({
  router,
  store,
  vuetify: new Vuetify(), //Vuetify 4
  render: h => h(App)
}).$mount('#app')
