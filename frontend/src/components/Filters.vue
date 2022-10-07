<template>
  <div>
    <div class="header">
      <img src="../assets/lesson-plans.svg" alt="Logo" />
      <h3>{{ $t('pageTitle') }}</h3>
    </div>
    <!-- <div class="clear-all-btn-wrapper">
      <div class="clear-all-btn" @click="resetFilters">Clear all</div>
    </div>-->
    <div class="filters-container">
      <!-- LANGUAGE -->
      <div
        class="filter-box bottom-popup"
        :class="{ 'filters-selected': chosenLanguageFilters.length }"
        v-outside="hideSelected"
      >
        <div class="content" @click="toggleSelected">
          <img src="../assets/language.svg" />
          <span
            v-if="chosenLanguageFilters.length > 0"
          >{{ chosenFiltersText(chosenLanguageFilters) }}</span>
        </div>
        <div
          class="content-no-filters"
          @click="toggleSelected"
          v-if="chosenLanguageFilters.length === 0"
        >
          <img src="../assets/language.svg" />
          <span data-type="languageFilter">{{ $t('filters.language') }}</span>
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
                >{{ $t(`filterOptions.${language}`) }}</label>
              </div>
            </div>
          </div>
          <div class="popup-apply" :onclick="toggleFilters" data-type="languageFilter">
            <span>Apply</span>
          </div>
          <div class="popup-arrow"></div>
        </div>
      </div>

      <!-- AGE AND DIFFICULTY -->
      <div
        class="filter-box bottom-popup"
        :class="{ 'filters-selected': chosenAgeAndDifficultyFilters.length }"
        v-outside="hideSelected"
      >
        <div class="content" @click="toggleSelected">
          <img src="../assets/difficulty.svg" />
          <span
            v-if="chosenAgeAndDifficultyFilters.length > 0"
          >{{ chosenFiltersText(chosenAgeAndDifficultyFilters) }}</span>
        </div>
        <div
          class="content-no-filters"
          @click="toggleSelected"
          v-if="chosenAgeAndDifficultyFilters.length === 0"
        >
          <img src="../assets/difficulty.svg" />
          <span data-type="ageAndDifficultyFilter">{{ $t('filters.ageAndDifficulty') }}</span>
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
                >{{ $t(`filterOptions.${ageAndDifficulty}`) }}</label>
              </div>
            </div>
          </div>
          <div class="popup-apply" :onclick="toggleFilters" data-type="ageAndDifficultyFilter">
            <span>Apply</span>
          </div>
          <div class="popup-arrow"></div>
        </div>
      </div>

      <!-- TOPIC -->
      <div
        class="filter-box bottom-popup"
        :class="{ 'filters-selected': chosenTopicFilters.length }"
        v-outside="hideSelected"
      >
        <div class="content" @click="toggleSelected">
          <img src="../assets/topic.svg" />
          <span v-if="chosenTopicFilters.length > 0">{{ chosenFiltersText(chosenTopicFilters) }}</span>
        </div>
        <div
          class="content-no-filters"
          @click="toggleSelected"
          v-if="chosenTopicFilters.length === 0"
        >
          <img src="../assets/topic.svg" />
          <span data-type="topicFilter">{{ $t('filters.topic') }}</span>
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
                <label class="popup-text" :for="'topic-' + topic">{{ $t(`filterOptions.${topic}`) }}</label>
              </div>
            </div>
          </div>
          <div class="popup-apply" :onclick="toggleFilters" data-type="topicFilter">
            <span>Apply</span>
          </div>
          <div class="popup-arrow"></div>
        </div>
      </div>

      <!-- ACTIVITY TYPE -->
      <div
        class="filter-box top-popup"
        :class="{ 'filters-selected': chosenActivityTypeFilters.length }"
        v-outside="hideSelected"
      >
        <div class="content" @click="toggleSelected">
          <img src="../assets/activity_type.svg" />
          <span
            v-if="chosenActivityTypeFilters.length > 0"
          >{{ chosenFiltersText(chosenActivityTypeFilters) }}</span>
        </div>
        <div
          class="content-no-filters"
          @click="toggleSelected"
          v-if="chosenActivityTypeFilters.length === 0"
        >
          <img src="../assets/activity_type.svg" />
          <span data-type="activityTypeFilter">{{ $t('filters.activityType') }}</span>
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
                >{{ $t(`filterOptions.${activityType}`) }}</label>
              </div>
            </div>
          </div>
          <div class="popup-apply" :onclick="toggleFilters" data-type="activityTypeFilter">
            <span>Apply</span>
          </div>
          <div class="popup-arrow"></div>
        </div>
      </div>

      <!-- DURATION -->
      <div
        class="filter-box top-popup"
        :class="{ 'filters-selected': chosenDurationFilters.length }"
        v-outside="hideSelected"
      >
        <div class="content" @click="toggleSelected">
          <img src="../assets/duration.svg" />
          <span
            v-if="chosenDurationFilters.length > 0"
          >{{ chosenFiltersText(chosenDurationFilters) }}</span>
        </div>
        <div
          class="content-no-filters"
          @click="toggleSelected"
          v-if="chosenDurationFilters.length === 0"
        >
          <img src="../assets/duration.svg" />
          <span data-type="durationFilter">{{ $t('filters.duration') }}</span>
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
                >{{ $t(`filterOptions.${duration}`) }}</label>
              </div>
            </div>
          </div>
          <div class="popup-apply" :onclick="toggleFilters" data-type="durationFilter">
            <span>Apply</span>
          </div>
          <div class="popup-arrow"></div>
        </div>
      </div>

      <!-- MATERIAL TYPE -->
      <div
        class="filter-box top-popup"
        :class="{ 'filters-selected': chosenMaterialTypeFilters }"
        v-outside="hideSelected"
      >
        <div class="content" @click="toggleSelected">
          <img src="../assets/type.svg" />
          <span
            v-if="chosenMaterialTypeFilters.length > 0"
          >{{ chosenFiltersText(chosenMaterialTypeFilters) }}</span>
        </div>
        <div
          class="content-no-filters"
          @click="toggleSelected"
          v-if="chosenMaterialTypeFilters.length === 0"
        >
          <img src="../assets/type.svg" />
          <span data-type="materialTypeFilter">{{ $t('filters.materialType') }}</span>
        </div>
        <div class="popup-container" id="materialTypeFilter" @click.stop>
          <div class="popup-box">
            <div class="checkmark-container">
              <div v-for="materialType in materialTypeArray" :key="materialType">
                <input
                  :id="'materialType-' + materialType"
                  :value="{ id: materialType, value: materialType }"
                  type="checkbox"
                  v-model="materialTypeFilter"
                />
                <label
                  class="popup-text"
                  :for="'materialType-' + materialType"
                >{{ $t(`filterOptions.${materialType}`) }}</label>
              </div>
            </div>
          </div>
          <div class="popup-apply" :onclick="toggleFilters" data-type="materialTypeFilter">
            <span>Apply</span>
          </div>
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
      return this.$store.getters.getFilters.materialTypeFilter || [];
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
      e.target.parentElement.classList.toggle('selected');
    },
    hideSelected(e) {
      if (!e.target.classList.contains('popup-container')) {
        Array.from(document.querySelectorAll('.selected')).forEach((el) => el.classList.remove('selected'));
      }
      if (e.target.parentElement.classList.contains('filter-box')) {
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
      const filter = event.target.parentElement.getAttribute('data-type');
      const popup = document.getElementById(filter);
      this.$store.commit('removeFilter', { filterName: filter })
      this.$store.commit('addFilter', { filterName: filter, filterValue: this[filter] });
      this.$store.commit('incrementFilterCount');
      popup.parentElement.classList.toggle('selected');
    },
    chosenFiltersText(array) {
      if (array.length === 1) {
        return this.$t(`filterOptions.${array[0].value}`);
      } else {
        return this.$t(`filterOptions.${array[0].value}`) + ` + ${array.length - 1}`;
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
  },
  mounted() {
    // if there are topic filter values when it redirects from lesson view to lesson list
    this.topicFilter = this.chosenTopicFilters.map(f => { 
      return {id: f.id, value: f.value} 
    });
  }
}
</script>

<style scoped lang="scss">
.header {
  display: flex;
  justify-content: center;
  margin: 30px 0;

  img {
    width: 60px;
  }

  h3 {
    margin-left: 20px;
    margin-top: 7px;
    margin-bottom: 0;
    font-size: 32px;
    line-height: 36px;
    letter-spacing: 4px;
    font-family: "Fredoka One", cursive;
    color: #000000;
  }

  @media (min-width: 1200px) {
    h3 {
      font-size: 48px;
      line-height: 50px;
      letter-spacing: 6px;
    }

    img {
      width: 74px;
    }
  }

  @media (min-width: 1400px) {
    margin: 60px 0;
  }

  @media (min-width: 1800px) {
    margin: 100px 0;
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
  margin: 15px auto 20px;
  display: grid;
  position: relative;
  grid-template-columns: repeat(2, minmax(0, 1fr));

  @media (min-width: 768px) {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }

  @media (min-width: 1400px) {
    margin-bottom: 80px;
  }

  @media (min-width: 1600px) {
    width: 90%;
  }

  .filter-box {
    height: 120px;
    width: 120px;
    margin: 20px;
    position: relative;

    @media (min-width: 576px) {
      height: 140px;
      width: 140px;
    }

    @media (min-width: 1400px) {
      height: 160px;
      width: 160px;
    }

    @media (min-width: 1600px) {
      height: 200px;
      width: 200px;
    }

    @media (min-width: 1800px) {
      height: 220px;
      width: 220px;
    }

    &.selected {
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

    .content,
    .content-no-filters {
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      // pointer-events: none;

      background-color: #aefcd8;
      cursor: pointer;
      border: 2px solid #000000;

      @media (min-width: 576px) {
        position: absolute;
      }

      img {
        width: 50px;
        pointer-events: none;

        @media (min-width: 1800px) {
          width: 80px;
        }
      }

      span {
        color: #252525;
        font-family: "Inter", sans-serif;
        font-size: 14px;
        line-height: 20px;
        text-align: center;
        padding: 10px;
        pointer-events: none;
        margin-top: 10px;
        pointer-events: none;

        @media (min-width: 576px) {
          font-size: 18px;
          line-height: 21px;
        }

        @media (min-width: 1800px) {
          font-size: 21px;
          line-height: 26px;
        }
      }
    }

    .content-no-filters {
      position: absolute;
      right: 10px;
      bottom: 10px;
      background-color: #ffffff;
      z-index: 1;
    }

    .popup-container {
      opacity: 0;
      z-index: -1;
      transition: opacity 0.2s, z-index 0.1s 0.2s;
      background-color: white;
      color: black;
      border: 2px solid black;
      position: absolute;
      box-shadow: 0 0 27px 3px rgba(0, 0, 0, 0.5);
      cursor: default;

      &#materialTypeFilter {
        min-width: 300px;
      }

      .popup-box {
        padding: 20px;
        padding-bottom: 5px;
        max-height: 300px;
        overflow-y: auto;

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
          font-family: "Inter", sans-serif;
          font-style: normal;
          padding-left: 28px;
        }
      }

      .popup-apply {
        padding: 15px 20px;
        text-align: right;
        border-top: 1px solid black;
        cursor: pointer;

        span {
          background-color: #aefcd8;
          text-transform: uppercase;
          font-family: "Inter", sans-serif;
          border-radius: 15px;
          padding: 2px 8px;
          font-size: 16px;
          font-weight: 500;
          border: 1px solid black;
        }
      }
      .popup-arrow {
        content: "";
        width: 20px;
        height: 20px;
        background: #fff;
        position: absolute;
        z-index: 1;
        border-left: 2px solid black;
        border-bottom: 2px solid black;
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
          top: calc(100% + 3px);
          transform: none;
        }
      }

      .popup-arrow {
        transform: rotate(135deg);
        top: -12px;
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
        bottom: -12px;
        transform: rotate(-45deg);
        display: none;
        @media (min-width: 576px) {
          display: block;
        }
      }
    }
  }
}

.apply-button {
  display: flex;
  justify-content: center;

  .btn {
    background-color: #aefcd8;
    text-transform: uppercase;
    font-family: "Inter", sans-serif;
    border-radius: 15px;
    padding: 4px 10px;
    font-size: 14px;
    font-weight: 600;
    border: 2px solid black;
    color: black;
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
