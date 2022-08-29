<template>
  <div v-if="lessons.length > 0 || hideAll" class="parent-container">
    <div class="lessons-container">
      <div class="lessons-title-bar">
        <h3>{{ title }}</h3>
        <button v-if="headers" class="mobile-filters-btn" @click="toggleFilters">Filters</button>
        <ul class="tags">
          <li class="tag" v-for="tag in tags" :key="tag">
            <span class="tag-text">{{ tag }}</span>
          </li>
        </ul>
      </div>
      <div class="lessons-list" v-for="lesson in lessons" :key="lesson.id">
        <div class="lesson-text-container">
          <router-link :to="'/lesson/' + lesson.id" class="lessons-title">{{ lesson.title }}</router-link>
          <div>
            <span v-for="topic in lesson.topic" :key="topic" class="lesson-topic">{{ $t(`filterOptions.topic.${topic}`) }}</span>
          </div>
        </div>
        <img src="../assets/back-arrow.svg" />
      </div>
      <div class="notFound" v-if="lessons.length === 0">
        <img src="../assets/filters-not-found.svg" />
        <span>
          No results found.
          <br />Please try different filters.
        </span>
      </div>
    </div>
    <div v-if="pagesNo > 1" class="pagination">
      <div>
        <button @click="changeSite(1)">
          <svg
            class="rotate-arrow"
            height="15"
            width="15"
            fill="#000000"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            viewBox="0 0 24 24"
            version="1.1"
            x="0px"
            y="0px"
          >
            <title>icon/double-chevron-right-solid</title>
            <desc>Created with Sketch Beta.</desc>
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <path
                d="M11.8789,2.6816 L13.2929,1.2676 L23.9999,11.9746 L13.2929,22.6816 L11.8789,21.2676 L21.1719,11.9746 L11.8789,2.6816 Z M5.293,22.6816 L3.879,21.2676 L13.172,11.9746 L3.879,2.6816 L5.293,1.2676 L16,11.9746 L5.293,22.6816 Z"
                fill="#000000"
              />
            </g>
          </svg>
        </button>
        <button @click="changeSite(page - 1)">
          <svg
            height="15"
            width="15"
            fill="#000000"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            viewBox="0 0 24 24"
            version="1.1"
            x="0px"
            y="0px"
          >
            <title>icon/chevron-left-solid</title>
            <desc>Created with Sketch Beta.</desc>
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <polygon
                fill="#000000"
                points="16.1211 21.2676 6.8281 11.9746 16.1211 2.6816 14.7071 1.2676 4.0001 11.9746 14.7071 22.6816"
              />
            </g>
          </svg>
        </button>
        <ul>
          <li
            v-for="p in pagesNo"
            :key="p"
            :class="{ 'active-page': p === page }"
            @click="changeSite(p)"
          >{{ p }}</li>
        </ul>
        <button @click="changeSite(page + 1)">
          <svg
            class="rotate-arrow"
            height="15"
            width="15"
            fill="#000000"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            viewBox="0 0 24 24"
            version="1.1"
            x="0px"
            y="0px"
          >
            <title>icon/chevron-left-solid</title>
            <desc>Created with Sketch Beta.</desc>
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <polygon
                fill="#000000"
                points="16.1211 21.2676 6.8281 11.9746 16.1211 2.6816 14.7071 1.2676 4.0001 11.9746 14.7071 22.6816"
              />
            </g>
          </svg>
        </button>
        <button @click="changeSite(pagesNo)">
          <svg
            height="15"
            width="15"
            fill="#ffffff"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            viewBox="0 0 24 24"
            version="1.1"
            x="0px"
            y="0px"
          >
            <title>icon/double-chevron-right-solid</title>
            <desc>Created with Sketch Beta.</desc>
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <path
                d="M11.8789,2.6816 L13.2929,1.2676 L23.9999,11.9746 L13.2929,22.6816 L11.8789,21.2676 L21.1719,11.9746 L11.8789,2.6816 Z M5.293,22.6816 L3.879,21.2676 L13.172,11.9746 L3.879,2.6816 L5.293,1.2676 L16,11.9746 L5.293,22.6816 Z"
                fill="#000000"
              />
            </g>
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['id', 'type', 'title', 'headers', 'hideAll', 'propsLessons', 'language'],
  data() {
    return {
      lessons: [],
      page: 1,
      refresh: true,
      isAuth: false,
      lessonsNo: 0,
      dateSortAscend: false,
      qualitySortAscend: false,
      lessonType: 'getLessons'
    }
  },
  computed: {
    pagesNo: function () {
      return Math.ceil(this.lessonsNo / 10)
    },
    tags: function () {
      let tags = []
      console.log("store")
        console.log(this.$store)
      Object.keys(this.$store.getters.getFilters).forEach(filter => {
        this.$store.getters.getFilters[filter].forEach((filterValue) => {
          // TODO: uredi translations (dobit <ime filtra> iz nekje)
          // tags.push(this.$t(`filterOptions.${<ime filtra>}.${filterValue.value}`))
          tags.push(filterValue.value)
        })
      })
      return tags;
    },
    filterCount: function () {
      return this.$store.getters.getFilterCount
    }
  },
  methods: {
    async changeSite(p) {
      if (p > 0 && p <= this.pagesNo) {
        try {
          const response = await this.$store.dispatch(this.lessonType, { page: p })
          if (response) {
            this.lessons = response.results
            this.lessonsNo = response.count
            this.page = p
          }
        } catch (error) {
          console.log(error)
        }
      }
    },
    toggleFilters() {
      this.$emit('toggle-filters')
    },
    toggleDateSort() {
      this.lessonType = 'getLessons'
      this.dateSortAscend = !this.dateSortAscend
      this.$store.commit('addFilter', { filterName: 'ordering', filterValue: this.dateSortAscend ? 'created_at' : '-created_at' })
      this.$store.commit('incrementFilterCount');
    },
    // removeFilter(filterName) {
    //   this.$store.commit('removeFilter', { filterName: filterName })
    // },
    removeFilter(filter, type, index) {
      this.tags.splice(index, 1)
      const filtered = this.$store.getters.getFilters[type].filter((obj) => obj.value !== filter)
      this.$store.commit('addFilter', { filterName: type, filterValue: filtered })
      this.$store.commit('incrementFilterCount');

    },
  },
  watch: {
    filterCount: async function () {
      // await this.mapFiltersToTags()
      const response = await this.$store.dispatch(this.lessonType, { page: 1, filters: this.$store.getters.getFilters })
      this.lessons = response.results;
      this.lessonsNo = response.count;
      this.$store.state.lessons.lesson_length = this.lessonsNo;
    }
  },
  async created() {
    this.$store.commit('clearFilters')
    if (this.language) {
      this.$store.commit('addFilter', { filterName: 'languageFilter', filterValue: [{ id: this.language[1], value: this.language[0] }] })
    }
    let response = []
    if (!this.propsLessons) response = await this.$store.dispatch(this.lessonType, { page: 1 })
    this.lessons = this.propsLessons ? this.propsLessons : response.results
    this.lessonsNo = response.count
    this.$store.state.lessons.lesson_length = this.lessonsNo;
    // await this.mapFiltersToTags()
  }
}

</script>

<style scoped lang="scss">

.lessons-container {
  display: flex;
  flex-direction: column;
  // height: 100vh;
  overflow-y: scroll;
  padding: 0 20px;
  margin-top: 20px;
  margin-bottom: 20px;

  @media (min-width: 992px) {
    padding: 0 40px;
    margin-top: 40px;
  }

  @media (min-width: 1800px) {
    margin-top: 60px;
  }

  .lessons-title-bar {
    border-bottom: 1px solid black;
    position: relative;

    @media (min-width: 992px) {
      flex-direction: row;
      justify-content: space-between;
    }

    h3 {
      font-size: 20px;
      margin: 0;
      color: #252525;
      font-family: 'Inter', sans-serif;
      font-weight: 300;
      margin-bottom: 1rem;

      @media (min-width: 768px) {
        font-size: 30px;
      }
    }

    .mobile-filters-btn {
      background-color: #aefcd8;
      text-transform: uppercase;
      font-family: "Inter", sans-serif;
      border-radius: 15px;
      padding: 4px 10px;
      font-size: 14px;
      font-weight: 600;
      border: 2px solid black;
      position: absolute;
      right: 0;
      top: 0;

      @media (min-width: 992px) {
        display: none;
      }
    }
  }

  .lessons-list {
    border-bottom: 1px solid black;
    padding: 0.5rem 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    // width: 100%;

    img {
      width: 40px;
    }

    .lesson-text-container {
      color: #252525;
      margin: 1rem 0;

      .lessons-date {
        font-family: "IBM Plex Mono";
        font-size: 14px;
        font-style: italic;
        line-height: 18px;
        margin: 0 0 0.25rem;
      }

      .lessons-title {
        color: #252525;
        font-family: 'Inter', sans-serif;
        font-size: 18px;
        font-weight: 700;
        text-decoration: none;
        @media (min-width: 992px) {
          font-size: 18px;
        }
      }
      .lessons-title:hover {
        text-decoration: underline;
      }

      .lesson-topic {
        display: inline-block;
        font-family: 'Inter', sans-serif;
        font-size: 11px;
        padding: 5px 10px;
        background-color: #c1ead7;
        margin-right: 10px;
        margin-top: 5px;
      }
    }
  }
  .notFound {
    display: flex;
    flex-direction: column;
    img {
      margin-top: 50px;
      width: 80px;
      margin-left: auto;
      margin-right: auto;
    }

    span {
      color: #252525;
      font-family: 'Inter', sans-serif;
      font-size: 20px;
      font-weight: 400;
      font-style: normal;
      letter-spacing: normal;
      line-height: 30px;
      text-align: center;
    }
  }
}

.share-bar {
  position: relative;
  width: 100%;
  overflow: hidden;
  display: flex;
  flex-direction: row;
  padding: 20px;
  // background-image: linear-gradient(-62deg, #f2f6fa 0%, #dbe7f1 100%);
  background-image: linear-gradient(-62deg, #cee7fd 0%, #f7fafd 100%);
  z-index: 2;

  .share-bar-split {
    width: 100%;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-content: center;
    &.hidden {
      display: none !important;
    }
  }

  h1 {
    margin-top: 0;
    // width: 100%;
  }

  input {
    margin-left: 20px;
  }
}

.parent-container {
  display: flex;
  width: 100%;
  margin: 0 auto;
  flex-direction: column;
  justify-content: center;
  align-items: initial;
  overflow-x: auto;
}

.tags {
  list-style: none;
  padding: 0;
  margin-bottom: 10px;
}

.tag {
  display: inline-block;
  padding-left: 10px;
  padding-right: 10px;
  border-radius: 14px;
  border: 2px solid black;
  margin-right: 10px;

  img {
    height: 1em; 
    vertical-align: middle;
    margin-bottom: 2px;
  }
  img:hover {
    cursor: pointer;
  }
}

.tag-text {
  color: #000000;
  font-family: 'Fredoka One', cursive;
  font-size: 14px;
  letter-spacing: normal;
  line-height: 18px;
  text-align: center;
}

</style>
