<template>
  <div v-if="lessons.length > 0 || hideAll" class="parent-container">
    <div v-if="headers" class="header">
      <div class="logo">
        <img src="../assets/lesson-generator-logo.svg" alt="lesson generator logo" />
      </div>
    </div>
    <div v-if="headers" class="line" />
    <div class="lessons-container">
      <div class="lessons-title-bar">
        <div>
          <h3>{{ title }}</h3>
          <button v-if="headers" class="btn" @click="toggleFilters">Filters</button>
          <ul class="tags">
            <li class="tag" v-for="tag in tags" :key="tag">
              <span class="tag-text">{{ tag }}</span>
            </li>
          </ul>
        </div>
      </div>
      <div class="lessons-list" v-for="lesson in lessons" :key="lesson.id">
        <div class="lesson-text-container">
          <router-link :to="'/lesson/' + lesson.id" class="lessons-title">{{ lesson.title }}</router-link>
          <span v-for="topic in lesson.topic" :key="topic" class="lesson-topic">{{ topic }}</span>
        </div>
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
      Object.keys(this.$store.getters.getFilters).forEach(filter => {
        console.log(filter);
        this.$store.getters.getFilters[filter].forEach((filterValue) => {
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
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;

  @media (min-width: 992px) {
    justify-content: flex-end;
  }

  @media (min-width: 1200px) {
  }

  .logo {
    img {
      margin-left: 20px;
      height: 30px;

      @media (min-width: 576px) {
        height: 40px;
      }

      @media (min-width: 992px) {
        display: none;
      }
    }
  }

  .btn {
    @media (max-width: 575px) {
      padding: 5px 5px;
      font-size: 10px;
    }
  }
  .button {
    margin-left: 10px;
    @media (max-width: 575px) {
      padding: 5px 5px;
      font-size: 10px;
    }
  }
}

.lessons-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  overflow-y: scroll;
  padding: 0 20px;
  margin-bottom: 20px;

  @media (min-width: 992px) {
    padding: 0 40px;
  }

  .lessons-title-bar {
    display: flex;
    flex-direction: column;
    border-bottom: 1px solid black;

    @media (min-width: 992px) {
      flex-direction: row;
      justify-content: space-between;
    }

    div:nth-child(1) {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 0;

      @media (min-width: 992px) {
        padding: 20px 0;
      }
    }

    h3 {
      font-size: 20px;
      margin: 0;
      color: #252525;
      font-family: "Poppins";

      @media (min-width: 768px) {
        font-size: 30px;
        line-height: 60px;
      }
    }

    button {
      font-size: 14px;
      letter-spacing: 1px;
      padding: 5px 12px;

      @media (min-width: 992px) {
        display: none;
      }
    }

    .lessons-sort {
      display: flex;
      flex-direction: row;
      align-items: center;
      margin-bottom: 10px;

      @media (min-width: 992px) {
        margin-bottom: 0;
      }

      .sort-button,
      p {
        font-family: "IBM Plex Mono";
        font-size: 12px;
        line-height: 14px;

        @media (min-width: 992px) {
          font-size: 14px;
          line-height: 18px;
        }
      }

      .sort-button {
        border-radius: 20px;
        background-color: rgb(48, 152, 243, 0.2);
        padding: 5px 10px;
        margin-left: 10px;
        cursor: pointer;
        color: #000000;
        font-weight: 700;
        text-transform: uppercase;
        display: flex;
        align-items: center;

        svg {
          margin-left: 0.5rem;
          transition: transform 0.5s;
          height: 14px;
          &.toggled {
            transform: rotate(-180deg);
          }
        }
      }
      .sort-button:hover {
        background-color: #ffcc00;
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

    .lesson-text-container {
      display: flex;
      flex-direction: column;
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
        font-family: Poppins;
        font-size: 20px;
        text-decoration: none;
        @media (min-width: 992px) {
          font-size: 24px;
        }
      }
      .lessons-title:hover {
        color: #3098f3;
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
      font-family: Poppins;
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

.lessonButtons {
  display: flex;
  justify-content: space-between;
}

.line {
  margin: 0;
  border-top: 1px solid #3098f3;
}
</style>
