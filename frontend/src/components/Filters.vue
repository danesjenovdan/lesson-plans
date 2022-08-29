<template>
  <div>
    <div class="search">
      <h3>Search for lessons</h3>
    </div>
    <div class="clear-all-btn-wrapper">
      <div class="clear-all-btn" @click="resetFilters">Clear all</div>
    </div>
    <div class="filters-container">
      <div
        class="filter-box bottom-popup"
        :class="{ 'filters-selected': chosenLanguageFilters.length }"
        @click="toggleSelected"
        v-outside="hideSelected"
      >
        <div class="content">
          <img src="../assets/topic.svg" />
          <span v-if="chosenLanguageFilters.length === 0" data-type="languageFilter">
            <i>{{ $t('filters.language') }}</i>
          </span>
          <span
            v-if="chosenLanguageFilters.length > 0"
          >{{ chosenFiltersText(chosenLanguageFilters) }}</span>
        </div>
        <div class="popup-container" id="languageFilter" @click.stop>
          <div class="popup-box">
            <div class="checkmark-container">
              <div v-for="language in languageArray" :key="language">
                <input
                  :id="'language-' + language"
                  type="checkbox"
                  :value="{ id: language, value: language }"
                  v-model="languageFilter"
                />
                <label
                  class="popup-text"
                  :for="'language-' + language"
                >{{ $t(`filterOptions.language.${language}`) }}</label>
              </div>
            </div>
          </div>
          <div class="popup-apply" :onclick="toggleFilters" data-type="languageFilter">Apply</div>
          <div class="popup-arrow"></div>
        </div>
      </div>
      <div
        class="filter-box bottom-popup"
        :class="{ 'filters-selected': chosenAgeAndDifficultyFilters.length }"
        @click="toggleSelected"
        v-outside="hideSelected"
      >
        <div class="content">
          <img src="../assets/ageAndDifficulty.svg" />
          <span
            v-if="chosenAgeAndDifficultyFilters.length === 0"
            data-type="ageAndDifficultyFilter"
          >
            <i>{{ $t('filters.ageAndDifficulty') }}</i>
          </span>
          <span
            v-if="chosenAgeAndDifficultyFilters.length > 0"
          >{{ chosenFiltersText(chosenAgeAndDifficultyFilters) }}</span>
        </div>
        <div class="popup-container" id="ageAndDifficultyFilter" @click.stop>
          <div class="popup-box">
            <div class="checkmark-container">
              <div v-for="ageAndDifficulty in ageAndDifficultiesArray" :key="ageAndDifficulty">
                <input
                  :id="'ageAndDifficulty-' + ageAndDifficulty"
                  :value="{ id: ageAndDifficulty, value: ageAndDifficulty }"
                  type="checkbox"
                  v-model="ageAndDifficultyFilter"
                />
                <label
                  class="popup-text"
                  :for="'ageAndDifficulty-' + ageAndDifficulty"
                >{{ $t(`filterOptions.ageAndDifficulty.${ageAndDifficulty}`) }}</label>
              </div>
            </div>
          </div>
          <div class="popup-apply" :onclick="toggleFilters" data-type="ageAndDifficultyFilter">Apply</div>
          <div class="popup-arrow"></div>
        </div>
      </div>
      <div
        class="filter-box bottom-popup"
        :class="{ 'filters-selected': chosenTopicFilters.length }"
        @click="toggleSelected"
        v-outside="hideSelected"
      >
        <div class="content">
          <img src="../assets/topic.svg" />
          <span v-if="chosenTopicFilters.length === 0" data-type="topicFilter">
            <i>{{ $t('filters.topic') }}</i>
          </span>
          <span v-if="chosenTopicFilters.length > 0">{{ chosenFiltersText(chosenTopicFilters) }}</span>
        </div>
        <div class="popup-container" id="topicFilter" @click.stop>
          <div class="popup-box">
            <div class="checkmark-container">
              <div v-for="topic in topicArray" :key="topic">
                <input
                  :id="'topic-' + topic"
                  :value="{ id: topic, value: topic }"
                  type="checkbox"
                  v-model="topicFilter"
                />
                <label
                  class="popup-text"
                  :for="'topic-' + topic"
                >{{ $t(`filterOptions.topic.${topic}`) }}</label>
              </div>
            </div>
          </div>
          <div class="popup-apply" :onclick="toggleFilters" data-type="topicFilter">Apply</div>
          <div class="popup-arrow"></div>
        </div>
      </div>
      <div
        class="filter-box bottom-popup"
        :class="{ 'filters-selected': chosenActivityTypeFilters.length }"
        @click="toggleSelected"
        v-outside="hideSelected"
      >
        <div class="content">
          <img src="../assets/activityType.svg" />
          <span
            v-if="chosenActivityTypeFilters.length === 0"
            data-activity-type="activityTypeFilter"
          >
            <i>{{ $t('filters.activityType') }}</i>
          </span>
          <span
            v-if="chosenActivityTypeFilters.length > 0"
          >{{ chosenFiltersText(chosenActivityTypeFilters) }}</span>
        </div>
        <div class="popup-container" id="activityTypeFilter" @click.stop>
          <div class="popup-box">
            <div class="checkmark-container">
              <div v-for="activityType in activityTypeArray" :key="activityType">
                <input
                  :id="'activityType-' + activityType"
                  :value="{ id: activityType, value: activityType }"
                  type="checkbox"
                  v-model="activityTypeFilter"
                />
                <label
                  class="popup-text"
                  :for="'activityType-' + activityType"
                >{{ $t(`filterOptions.activityType.${activityType}`) }}</label>
              </div>
            </div>
          </div>
          <div class="popup-apply" :onclick="toggleFilters" data-type="activityTypeFilter">Apply</div>
          <div class="popup-arrow"></div>
        </div>
      </div>
      <div
        class="filter-box top-popup"
        :class="{ 'filters-selected': chosenDurationFilters.length }"
        @click="toggleSelected"
        v-outside="hideSelected"
      >
        <div class="content">
          <img src="../assets/duration.svg" />
          <span v-if="chosenDurationFilters.length === 0" data-type="durationFilter">
            <i>{{ $t('filters.duration') }}</i>
          </span>
          <span
            v-if="chosenDurationFilters.length > 0"
          >{{ chosenFiltersText(chosenDurationFilters) }}</span>
        </div>
        <div class="popup-container" id="durationFilter" @click.stop>
          <div class="popup-box">
            <div class="checkmark-container">
              <div v-for="duration in durationArray" :key="duration">
                <input
                  :id="'duration-' + duration"
                  :value="{ id: duration, value: duration }"
                  type="checkbox"
                  v-model="durationFilter"
                />
                <label
                  class="popup-text"
                  :for="'duration-' + duration"
                >{{ $t(`filterOptions.duration.${duration}`) }}</label>
              </div>
            </div>
          </div>
          <div class="popup-apply" :onclick="toggleFilters" data-type="durationFilter">Apply</div>
          <div class="popup-arrow"></div>
        </div>
      </div>
      <div
        class="filter-box top-popup"
        :class="{ 'filters-selected': chosenMaterialTypeFilters }"
        @click="toggleSelected"
        v-outside="hideSelected"
      >
        <div class="content">
          <img src="../assets/keyword.svg" />
          <span data-type="materialTypeFilter">
            <i>{{ $t('filters.materialType') }}</i>
          </span>
        </div>
        <div class="popup-container" id="materialTypePrepFilter" @click.stop>
          <div class="popup-box">
            <div class="checkmark-container">
              <div v-for="materialType in materialTypeArray" :key="materialType">
                <input
                  :id="'materialType-' + materialType"
                  :value="{ id: materialType, value: materialType }"
                  type="checkbox"
                  v-model="durationFilter"
                />
                <label
                  class="popup-text"
                  :for="'materialType-' + materialType"
                >{{ $t(`filterOptions.materialType.${materialType}`) }}</label>
              </div>
            </div>
          </div>
          <div class="popup-apply" :onclick="toggleFilters" data-type="durationFilter">Apply</div>
          <div class="popup-arrow"></div>
        </div>
      </div>
    </div>
    <div class="apply-button">
      <button class="btn" @click="closeFilters">Apply</button>
    </div>
  </div>
</template>

<script>
import { MATERIAL_TYPE_CHOICES, AGE_CHOICES, LANGUAGE_CHOICES, TOPIC_CHOICES, DIFFICULTY_CHOICES, DURATION_CHOICES, ACTIVITY_TYPE_CHOICES } from './filters';

export default {
  data() {
    return {
      languageArray: [],
      ageAndDifficultiesArray: [],
      ageArray: [],
      topicArray: [],
      activityTypeArray: [],
      durationArray: [],
      languageFilter: [],
      topicFilter: [],
      durationFilter: [],
      ageAndDifficultyFilter: [],
      activityTypeFilter: [],
      materialTypeFilter: []
    }
  },
  computed: {
    chosenLanguageFilters() {
      return this.$store.getters.getFilters.languageFilter || [];
    },
    chosenAgeAndDifficultyFilters() {
      return this.$store.getters.getFilters.ageAndDifficultyFilter || [];
    },
    chosenTopicFilters() {
      return this.$store.getters.getFilters.topicFilter || [];
    },
    chosenActivityTypeFilters() {
      return this.$store.getters.getFilters.activityTypeFilter || [];
    },
    chosenDurationFilters() {
      return this.$store.getters.getFilters.durationFilter || [];
    },
    chosenMaterialTypeFilters() {
      return this.$store.getters.getFilters.materialTypeFilter;
    },
    isDisabled() {
      return this.$store.getters.lesson_length > 0
    }
  },
  directives: {
    outside: {
      beforeMount(el, binding, vnode) {
        el.clickOutsideEvent = function (event) {
          if (!(el === event.target || el.contains(event.target))) {
            binding.value(event, el);
          }
        };
        document.body.addEventListener('click', el.clickOutsideEvent);
      },
      unmounted(el) {
        document.body.removeEventListener('click', el.clickOutsideEvent);
      }
    }
  },
  methods: {
    toggleSelected(e) {
      e.target.classList.toggle('selected');
    },
    hideSelected(e) {
      if (!e.target.classList.contains('popup-container')) {
        Array.from(document.querySelectorAll('.selected')).forEach((el) => el.classList.remove('selected'));
      }
      if (e.target.classList.contains('filter-box')) {
        this.toggleSelected(e);
      }
    },
    closeFilters() {
      const filterArrays = [
        { filters: this.languageFilter, type: 'languageFilter' },
        { filters: this.ageAndDifficultyFilter, type: 'ageAndDifficultyFilter' },
        { filters: this.topicFilter, type: 'topicFilter' },
        { filters: this.activityTypeFilter, type: 'activityTypeFilter' },
        { filters: this.durationFilter, type: 'durationFilter' },
        { filters: this.materialTypeFilter, type: 'materialTypeFilter' }
      ]
      filterArrays.forEach((arr) => {
        this.$store.commit('removeFilter', { filterName: arr.type })
        this.$store.commit('addFilter', { filterName: arr.type, filterValue: arr.filters })
      })
      this.$store.commit('incrementFilterCount');
      this.$emit('toggle-filters');
    },
    toggleFilters(event) {
      const popup = document.getElementById(event.target.getAttribute('data-type'));
      this.$store.commit('removeFilter', { filterName: event.target.getAttribute('data-type') })
      this.$store.commit('addFilter', { filterName: event.target.getAttribute('data-type'), filterValue: this[event.target.getAttribute('data-type')] });
      this.$store.commit('incrementFilterCount');
      popup.parentElement.classList.toggle('selected');
    },
    chosenFiltersText(array) {
      if (array.length === 1) {
        return array[0].value;
      } else {
        return `${array[0].value} + ${array.length - 1} more`;
      }
    },
    resetFilters() {
      this.$store.commit('clearFilters');
      this.$store.commit('resetFilterCount');
    }
  },
  async created() {
    this.languageArray = LANGUAGE_CHOICES
    this.materialTypeArray = MATERIAL_TYPE_CHOICES
    this.ageAndDifficultiesArray = AGE_CHOICES.concat(DIFFICULTY_CHOICES)
    this.topicArray = TOPIC_CHOICES
    this.durationArray = DURATION_CHOICES
    this.activityTypeArray = ACTIVITY_TYPE_CHOICES
  }
}
</script>

<style scoped lang="scss">
.search {
  font-size: 20px;
  margin: 0;
  color: #252525;
  font-family: "Poppins";
  width: 90%;
  h3 {
    margin-bottom: 20px;
  }
  @media (min-width: 768px) {
    font-size: 30px;
  }

  @media (min-width: 1400px) {
    width: 90%;
    margin: 0 auto;
  }

  @media (min-width: 1600px) {
    width: 80%;
  }
}

.clear-all-btn-wrapper {
  text-align: end;

  @media (min-width: 1400px) {
    margin-right: 5%;
  }

  @media (min-width: 1600px) {
    margin-right: 10%;
  }

  .clear-all-btn {
    text-transform: uppercase;
    font-style: italic;
    color: black;
    border-radius: 20px;
    background-color: rgb(214, 234, 253);
    padding: 5px 10px;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    cursor: pointer;
    font-family: "IBM Plex Mono";
    font-size: 14px;
    line-height: 18px;

    &:hover {
      background-color: #ffcc00;
    }
  }
}

.filters-container {
  margin: 15px auto 40px;
  width: 100%;
  display: grid;
  position: relative;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  column-gap: 3%;
  row-gap: 3%;

  @media (min-width: 1400px) {
    width: 90%;
    column-gap: 5%;
    row-gap: 5%;
    margin: 15px auto 80px;
  }

  @media (min-width: 1600px) {
    width: 80%;
  }

  .filter-box {
    background-color: white;
    cursor: pointer;
    border: 4px solid white;
    height: 120px;

    @media (min-width: 576px) {
      position: relative;
      height: initial;
    }

    &:after {
      content: "";
      display: block;
      padding-bottom: 25%;

      @media (min-width: 576px) {
        padding-bottom: 90%;
        position: relative;
      }
    }

    &.selected {
      border: 4px solid #3098f3;

      /* Toggle this class when clicking on the popup container (hide and show the popup) */
      .popup-container {
        opacity: 1;
        z-index: 2;
        transition: z-index 0s;

        .popup-box label.popup-text {
          cursor: pointer;
        }
      }
    }

    .content {
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      pointer-events: none;

      @media (min-width: 576px) {
        position: absolute;
      }

      img {
        width: 50%;
        pointer-events: none;

        @media (min-width: 1400px) {
          width: 40%;
        }
      }

      span {
        color: #252525;
        font-family: "IBM Plex Mono";
        font-size: 14px;
        line-height: 20px;
        text-align: center;
        padding: 10px;
        pointer-events: none;

        @media (min-width: 576px) {
          font-size: 18px;
        }
      }
    }

    &.filters-selected {
      background-color: #d6eafd;
      border-color: #d6eafd;

      &.selected {
        border-color: #3098f3;
      }

      img {
        width: 25%;
      }
    }

    .popup-container {
      opacity: 0;
      z-index: -1;
      transition: opacity 0.2s, z-index 0.1s 0.2s;
      background-color: white;
      color: black;
      border: 4px solid #3098f3;
      position: absolute;
      box-shadow: 0 0 27px 3px rgba(48, 152, 243, 0.5);
      cursor: default;

      &#materialTypeFilter {
        min-width: 300px;
      }

      .popup-box {
        padding: 20px;
        max-height: 300px;
        overflow-y: auto;

        .keyword-container {
          input {
            height: auto !important;
            border: 1px solid black;
            margin: 10px 0;
            width: 100%;

            @media (min-width: 576px) {
              width: 100%;
            }
          }
        }

        .keyword-apply {
          display: flex;
          justify-content: space-between;
          align-items: center;
          span {
            text-decoration: underline;
          }
          .popup-apply {
            margin-right: 0;
            padding-bottom: 0;
            border-top: 0;
          }
        }

        .keyword-text {
          font-family: "IBM Plex Mono";
          font-size: 14px;
        }

        .checkmark-container {
          display: grid;
          grid-template-columns: 100%;
          column-gap: 20px;
          row-gap: 10px;
          width: 100%;
          align-items: start;
          padding-bottom: 15px;

          @media (min-width: 992px) {
            grid-template-columns: 45% 45%;
          }
        }

        label.popup-text {
          cursor: default;
        }
      }

      .popup-apply {
        color: #3098f3 !important;
        margin-right: 20px;
        padding-bottom: 20px;
        font-family: Poppins;
        font-size: 18px;
        font-weight: 700;
        text-align: right;
        text-decoration: underline;
        border-top: 1px solid black;
        cursor: pointer;
      }
      .popup-arrow {
        content: "";
        width: 20px;
        height: 20px;
        background: #fff;
        position: absolute;
        z-index: 1;
        border-left: 4px solid #3098f3;
        border-bottom: 4px solid #3098f3;
        left: 20px;
      }
    }

    &.bottom-popup {
      .popup-container {
        left: 0;
        right: 0;
        top: 50%;
        transform: translateY(-50%);
        @media (min-width: 576px) {
          left: -4px;
          right: initial;
          top: calc(100% + 28px);
          transform: none;
        }
      }

      .popup-arrow {
        transform: rotate(135deg);
        top: -14px;
        display: none;
        @media (min-width: 576px) {
          display: block;
        }
      }
    }

    &.top-popup {
      .popup-container {
        left: 0;
        right: 0;
        top: 50%;
        transform: translateY(-50%);
        @media (min-width: 576px) {
          left: -4px;
          right: initial;
          top: initial;
          bottom: calc(100% + 28px);
          transform: none;
        }
      }

      .popup-arrow {
        bottom: -14px;
        transform: rotate(-45deg);
        display: none;
        @media (min-width: 576px) {
          display: block;
        }
      }
    }
  }
  .filter-box:hover {
    background-color: #d6eafd;
    border: #3098f3;
  }
}

.apply-button {
  display: flex;
  justify-content: center;

  .btn {
    margin-top: 20px;
    font-size: 14px;
    letter-spacing: 1px;
    padding: 5px 12px;
  }

  @media (min-width: 992px) {
    display: none;
  }
}

/* the actual input checkbox */
[type="checkbox"]:not(:checked),
[type="checkbox"]:checked {
  position: absolute;
  opacity: 0;
}

/* checkbox style for filters */
[type="checkbox"]:not(:checked) + label,
[type="checkbox"]:checked + label {
  position: relative;
  padding-left: 2.3em;
  font-size: 14px;
  line-height: 1.7;
  cursor: pointer;
  color: #000000;
  font-family: "IBM Plex Mono";
  font-style: italic;
  display: flex;
}

/* checkbox aspect */
[type="checkbox"]:not(:checked) + label:before,
[type="checkbox"]:checked + label:before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  width: 1.4em;
  height: 1.4em;
  border: 1px solid rgb(0, 0, 0);
  background: #fff;
}

[type="checkbox"]:checked + label:before {
  background-image: url("../assets/checkbox.png");
  background-size: contain;
}

/* Accessibility */
// [type="checkbox"]:checked:activityType + label:before,
// [type="checkbox"]:not(:checked):activityType + label:before {
// }
</style>
