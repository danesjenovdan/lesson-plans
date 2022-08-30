// const api = "http://localhost:8000/api/v1";
const api = 'https://lesson-plans-backend.lb.djnd.si/api/v1';

export const state = () => ({
  lesson_length: 0,
  filters: {},
  filterCount: 0,
  lesson: {},
  lessonUpdate: 0
})

export const getters = {
  lesson_length (state) {
    return state.lesson_length
  },
  getFilters (state) {
    return state.filters
  },
  getFilterCount (state) {
    return state.filterCount
  }
}

export const mutations = {
  lesson_length (state, count) {
    state.lesson_length = count;
  },
  addFilter (state, payload) {
    state.filters[payload.filterName] = payload.filterValue;
  },
  removeFilter (state, payload) {
    delete state.filters[payload.filterName];
  },
  clearFilters (state) {
    state.filters = {};
  },
  incrementFilterCount (state) {
    state.filterCount++;
  },
  resetFilterCount (state) {
    state.filterCount = 0;
  }
}

const mapFilters = (filters) => {
  let filterString = ''
  Object.keys(filters).forEach((key, index) => {
    if(index !== 0) filterString += '&'
    if (key === 'languageFilter') filterString += 'language='
    if (key === 'materialTypeFilter') filterString += 'material_type='
    if (key === 'topicFilter') filterString += 'topic='
    if (key === 'ageAndDifficultyFilter') filterString += 'age_and_difficulty='
    if (key === 'activityTypeFilter') filterString += 'activity_type='
    if (key === 'durationFilter') filterString += 'duration_prep='
    if (key === 'id') filterString += 'id='

    if(Array.isArray(filters[key])) {
      filters[key].forEach((value, index) => {
        if(!value.id) filterString += (index+1) !== filters[key].length ? value + ',' : value
        else filterString += (index+1) !== filters[key].length ? value.id + ',' : value.id
      })
    } else {
      filterString += filters[key]
    }

  })
  return filterString
}

Date.prototype.addHours = function(h) {
  this.setTime(this.getTime() + (h*60*60*1000));
  return this;
}

export const actions = {
  async getLessonLength ({ getters }) {
    return getters.lesson_length
  },
  async getLessons ({ getters, commit }, payload) {
    try {
      const filters = mapFilters(getters.getFilters)
      const result = await fetch(`${api}/lessons/?page=${payload.page}&${filters}`, {
          method: 'get',
          headers: {
            'content-type': 'application/json'
          }
        })
      return await result.json();
    } catch (error) {
      return error
    }
  },
  async getCategoryLessons ({ getters, commit }, payload) {
    try {
      let response = await fetch(`${api}/lessons/?page=${payload.page}&${payload.filters}`, {
        method: 'get',
        headers: {
          'content-type': 'application/json'
        }
      })
      return await response.json();
    } catch (error) {
      return error
    }
  },
  async getLesson (context, payload) {
    try {
      const result = await fetch(`${api}/lessons/${payload.id}`, {
          method: 'get',
          headers: {
            'content-type': 'application/json'
          }
        })
      const body = await result.json(); // .json() is asynchronous and therefore must be awaited
      return body;
    } catch (error) {
      return error
    }
  },
  async getLessonAttributes (context, payload) {
    let filters = ''
    if (payload.filters) filters = mapFilters(payload.filters)
    try {
      const result = await fetch(`${api}/lessons/${payload.type}?${filters}`, {
        method: 'get',
        headers: {
          'content-type': 'application/json'
        }
      });
      const body = await result.json();
      return body;
    } catch (error) {
      console.log(error);
    }
  },
}

const store = {
  state,
  mutations,
  actions,
  getters
}

export default store

