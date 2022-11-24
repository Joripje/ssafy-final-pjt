import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

const API_URL = 'http://127.0.0.1:8000'
Vue.use(Vuex)
const TMDB_API_KEY="c77ef5df652e2127c8855d6cae700acb"
export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    token: null,
    user_info: [

    ],
    movie_review: [

    ],
    movie_list: [

    ],
    movieItemDetail:[

    ],
    actors: [

    ],
    genres: [

    ],
    recommend_movie_list: [

    ],
    prefer_list : [

    ],
    user_review: [

    ],
  },
  getters: {
    isLoggedIn(state) {
      return state.token ? true : false
    },
    addWishListUserNumber(state) {
      return state.movieItemDetail.wish_user.length
    }
  },
  mutations: {
    GET_MOVIE_DETAIL(state, movieItemDetail) {
      state.movieItemDetail = movieItemDetail
    },
    GET_ACTORS_WITH_MOVIE_ID(state, actors) {
      state.actors = actors
    },
    GET_MOVIE_GENRE(state, genres) {
      state.genres = genres
    },
    SAVE_TOKEN(state, token) {
      state.token = token
    },
    GET_USER_INFO(state, userInfo) {
      state.user_info = userInfo
    },
    LOG_OUT(state) {
      state.token = null
      state.user_info = null
    },
    GET_MOVIE_REVIEW(state, movie_review) {
      state.movie_review = movie_review
    },
    GET_MOVIE_LIST(state, movie_list) {
      state.movie_list = movie_list
    },
    GET_RECOMMEND_LIST(state, movie_list) {
      state.recommend_movie_list = movie_list
    },
    GET_PREFER_LIST(state, prefer_list) {
      state.prefer_list = prefer_list
    },
    GET_USER_REVIEW(state, review_movie) {
      state.user_review = review_movie
    }
  },
  actions: {
    getMovieDetail(context, movieId) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${movieId}/`
      })
        .then(res =>
          context.commit('GET_MOVIE_DETAIL', res.data)
        )
        .catch(err => console.log(err))
    },
    getActorsWithMovieId(context, movieId) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${movieId}/actors/`
      })
        .then(res => 
          context.commit('GET_ACTORS_WITH_MOVIE_ID', res.data) 
        )
        .catch(err => console.log(err))
    },
    getMovieGenre(context, movieId) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${movieId}/genre/`
      })
        .then(res => 
          context.commit('GET_MOVIE_GENRE', res.data) 
        )
        .catch(err => console.log(err))
    },
    addToWishList(context, movieId) {
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${movieId}/add_wishlist/`,
        headers: {
          Authorization: `Token ${this.state.token}`
        }
      })
        .then(res => {
          console.log(res)
        })
        .catch(err => console.log(err))
    },
    signUp(context, payload) {
      const email = payload.email
      const password1 = payload.password1
      const password2 = payload.password2
      const username = payload.username
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/accounts/signup/`,
        data: {
          email, username, password1, password2
        }
      })
        .then(res => {
          console.log(res)

        })
        .catch(err => console.log(err))
    },
    logIn(context, payload) {
      const email = payload.email
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/accounts/login/`,
        data: {
          email, password
        }
      })
        .then(res => {
          context.commit('SAVE_TOKEN', res.data.key)
          axios({
            method: 'get',
            url: `${API_URL}/api/v1/accounts/user/`,
            headers: {
              Authorization: `Token ${this.state.token}`
            }
          })
            .then((res) => {
                context.commit('GET_USER_INFO', res.data)
                console.log(res.data)
            })
            .catch((err) => {
              console.log(err)
            })
        })
        .catch(err => console.log(err))
    },
    logOut(context) {
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/accounts/logout/`,
        headers: {
          Authorization: `Token ${this.state.token}`
        }
      })
        .then((res)=> {
          console.log(res.detail)
          context.commit('LOG_OUT')
        })
    },
    createReview(context, payload) {
      const content = payload.review_content
      const rate = payload.review_rate
      const movieId = payload.movieId
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${movieId}/create_review/`,
        data: {
          content, rate
        },
        headers: {
          Authorization: `Token ${this.state.token}`
        }
      })
        .then(res => {
          console.log(res)
          context.dispatch('getMovieReview', movieId)
        })
        .catch(err => {
          console.log(err)
        })
    },
    getMovieReview(context, movieId) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${movieId}/review/`,
        // headers: {
        //   Authorization: `Token ${this.state.token}`
        // }
      })
        .then(res => {
          context.commit('GET_MOVIE_REVIEW', res.data.movie_review)

        })
        .catch(err => {
          console.log(err)
        })
    },
    getMovieList(context) {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/popular?api_key=${TMDB_API_KEY}&language=ko-KR&page=1&region=KR`,
        // headers: {
        //   Authorization: `Token ${this.state.token}`
        // }
      })
        .then(res => {
          context.commit('GET_MOVIE_LIST', res.data.results)
          console.log(res.data.results)
        })
        .catch(err => {
          console.log(err)
          console.log(TMDB_API_KEY)
        })
    },
    getWishList(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/accounts/profile/`,
        headers: {
          Authorization: `Token ${this.state.token}`
        }
      })
        .then(res => {
          context.commit('GET_MOVIE_LIST', res.data.wish_movie)
          console.log(res.data.wish_movie)
        })
        .catch(err => {
          console.log(err)
        })
    },
    getRecommendMovie(context) {
      if (this.state.token) {
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/accounts/recommend/`,
          headers: {
            Authorization: `Token ${this.state.token}`
          }
        })
          .then(res => {
            res.data
            context.commit('GET_RECOMMEND_LIST', res.data)
            console.log(res.data)
          })
          .catch(err => {
            console.log(err)
          })
      } else {
        console.log('없음')
      }
      
    },
    getPreferList(context) {
      if (this.state.token) {
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/accounts/genre_prefer/`,
          headers: {
            Authorization: `Token ${this.state.token}`
          }
        })
          .then(res => {
            res.data
            context.commit('GET_PREFER_LIST', res.data)
            console.log(res.data)
          })
          .catch(err => {
            console.log(err)
          })
      } else {
        console.log('없음')
      }
      
    },
    getUserReview(context) {
      if (this.state.token) {
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/accounts/profile/`,
          headers: {
            Authorization: `Token ${this.state.token}`
          }
        })
          .then(res => {
            res.data
            context.commit('GET_USER_REVIEW', res.data.review_user)
          })
          .catch(err => {
            console.log(err)
          })
      } else {
        console.log('없음')
      }
      
    },
    searchMovies(context, keyWord) {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/search/movie?api_key=${TMDB_API_KEY}&language=ko-KR&query=${keyWord}&page=1&include_adult=false&region=KR`,
      })
        .then(res => {
          context.commit('GET_MOVIE_LIST', res.data.results)
          console.log(res.data.results)
        })
        .catch(err => {
          console.log(err)
          console.log(TMDB_API_KEY)
        })
    }

  },
  modules: {
  }
})
