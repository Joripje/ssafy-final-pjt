import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

const API_URL = 'http://127.0.0.1:8000'
Vue.use(Vuex)

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
    movieItemDetail:[

    ],
    actors: [

    ],
    genres: [

    ],
    movieDetail: [
      {
        "id": 11,
        "title": "스타워즈 에피소드 4: 새로운 희망",
        "overview": "공화국이 붕괴하고 제국이 수립된 뒤 20년, 제다이 기사단은 전멸하고 강력한 제국군의 횡포에 은하계는 공포에 휩싸여 있다. 그러던 중 공화국 재건을 노리는 반란군이 제국군의 비밀병기 데스스타 설계도를 훔쳐 달아나고 제국군은 이를 쫓는다. 하지만 결국 제국의 손에 붙잡히게 된 그들은 드로이드 R2-D2에 설계도를 넣어서 R2의 친구 C-3PO와 탈출시키는 데 성공하고, 두 드로이드 콤비는 타투인의 시골 마을에서 숙부와 함께 살고 있던 청년 루크 스카이워커에게 오게 되는데...",
        "release_date": "1977-05-25",
        "poster_path": "/7XFfURIFCJxN1mfBg0SAjk5yGzg.jpg",
        "backdrop_path": "/yrdAamkeqXHm0UYukk8xgoCvc7G.jpg",
        "vote_count": 17899,
        "vote_average": 8.2,
        "genre_ids": [
          12,
          28,
          878
        ],
        "actors": [
          2,
          3,
        ]
      },
      {
        "id": 12,
        "title": "킹스맨",
        "overview": "매너 매이킷드 맨",
        "release_date": "2015-07-15",
        "poster_path": "/7XFfURIFCJxN1mfBg0SAjk5yGzg.jpg",
        "backdrop_path": "/yrdAamkeqXHm0UYukk8xgoCvc7G.jpg",
        "vote_count": 17899,
        "vote_average": 8.6,
        "genre_ids": [
          11,
          15,
          88
        ],
        "actors": [
          1,
          4,
        ]
      }
    ],
  },
  getters: {
    isLoggedIn(state) {
      return state.token ? true : false
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
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then(res => {
          context.commit('SAVE_TOKEN', res.data.key)

        })
        .catch(err => console.log(err))
    },
    logIn(context, payload) {
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/accounts/login/`,
        data: {
          username, password
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

        })
        .catch(err => {
          console.log(err)
        })
    },
    getMovieReview(context, movieId) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${movieId}/review/`,
        headers: {
          Authorization: `Token ${this.state.token}`
        }
      })
        .then(res => {
          context.commit('GET_MOVIE_REVIEW', res.data.movie_review)

        })
        .catch(err => {
          console.log(err)
        })
    }
    
  },
  modules: {
  }
})
