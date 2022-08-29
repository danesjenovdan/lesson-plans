import Vuex from 'vuex'
import index from './index'
import VuexPersistence from 'vuex-persist'

const store = new Vuex.Store({
  modules: {
    lessons: index
  },
  plugins: [new VuexPersistence().plugin]
})

export default store