<template>
  <div class="split-container">
    <div class="container-child" :class="{ 'opened': filtersOpened }">
      <div class="wrapper">
        <div class="debate-logo">
          <router-link to="/" @click="resetFilters">
            <img src="../assets/lesson-generator-logo.svg" alt="lesson generator logo" />
          </router-link>
          <span>{{ $t('pageTitle') }}</span>
        </div>
        <filters @toggle-filters="toggleFilters" />
      </div>
    </div>
    <div class="container-child">
      <lesson-list
        type="getLessons"
        :language="language"
        :headers="true"
        :hideAll="true"
        title="Lessons"
        @toggle-filters="toggleFilters"
      />
    </div>
  </div>
</template>

<script>
import Lesson from '../components/Lesson.vue'
import Filters from '../components/Filters.vue'
import LessonList from '../components/LessonList.vue'

export default {
  props: ['language'],
  components: {
    Lesson,
    Filters,
    LessonList,
  },
  data() {
    return {
      filtersOpened: false
    }
  },
  methods: {
    toggleFilters() {
      this.filtersOpened = !this.filtersOpened
    },
    resetFilters() {
      this.$store.commit('clearFilters');
      this.$store.commit('resetFilterCount');
    }
  }
}

</script>

<style scoped lang="scss">
.container-child:first-child {
  position: absolute;
  opacity: 0;
  z-index: -1;
  height: 100%;

  &.opened {
    opacity: 1;
    z-index: 1;
    width: 100%;
    height: 100vh;

    @media (min-width: 992px) {
      height: 100%;
    }
  }

  @media (min-width: 992px) {
    position: static;
    opacity: 1;
    z-index: 1;
    height: 100%;
  }
}
</style>

