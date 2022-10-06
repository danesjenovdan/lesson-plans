<template>
  <div class="split-container">
    <div class="container-child" :class="{ opened: filtersOpened }">
      <div class="wrapper">
        <filters @toggle-filters="toggleFilters" />
      </div>
    </div>
    <div class="container-child">
      <lesson-list
        type="getLessons"
        :language="language"
        :headers="true"
        :hideAll="true"
        :title="$t('listTitle')"
        :filterByTopic="filterByTopic"
        @toggle-filters="toggleFilters"
      />
    </div>
  </div>
</template>

<script>
import Lesson from "../components/Lesson.vue";
import Filters from "../components/Filters.vue";
import LessonList from "../components/LessonList.vue";

export default {
  props: ["language", "filterByTopic"],
  components: {
    Lesson,
    Filters,
    LessonList,
  },
  data() {
    return {
      filtersOpened: false,
    };
  },
  methods: {
    toggleFilters() {
      this.filtersOpened = !this.filtersOpened;
    },
    resetFilters() {
      this.$store.commit("clearFilters");
      this.$store.commit("resetFilterCount");
    },
  },
};
</script>

<style scoped lang="scss">
.split-container {
  height: 100%;
  display: flex;
  flex-wrap: wrap;

  @media (min-width: 992px) {
    flex-wrap: nowrap;
  }

  .container-child {
    flex: 1 0 100%;

    @media (min-width: 992px) {
      flex: 1 0 50%;
    }

    &:first-child {
      position: absolute;
      opacity: 0;
      z-index: -1;
      background-color: #f1f2f2;
      height: 100%;

      &.opened {
        opacity: 1;
        z-index: 1;
        width: 100%;
        // height: 100vh;

        @media (min-width: 992px) {
          // height: 100%;
        }
      }

      @media (min-width: 992px) {
        position: static;
        opacity: 1;
        z-index: 1;
        // height: 100%;
      }
    }

    .wrapper {
      padding: 0 20px;
      display: flex;
      max-height: 100%;
      justify-content: start;
      flex-direction: column;
    }
  }
}
</style>
