<template>
  <div class="parentContainer">
    <h1>{{ lesson.title }}</h1>
    <ul class="tags">
      <li class="tag" v-for="topic in lesson.topic" :key="topic">
        <span class="tag-text">{{ topic }}</span>
      </li>
    </ul>
    <span class="lesson-text">{{ lesson.description }}</span>
    <div class="line"></div>
    <button class="download">DOWNLOAD</button>
    <div class="info">
      <span class="meta">Material type</span>
      <span
        class="value"
        v-for="materialType in lesson.material_type"
        :key="materialType"
      >{{ materialType }}</span>
    </div>
    <div class="info">
      <span class="meta">Language</span>
      <span class="value" v-for="language in lesson.language" :key="language">{{ language }}</span>
    </div>
    <div class="info">
      <span class="meta">Topic</span>
      <span class="value" v-for="topic in lesson.topic" :key="topic">{{ topic }}</span>
    </div>
    <div class="info">
      <span class="meta">Age and difficulty</span>
      <span
        class="value"
        v-for="ageAndDifficulty in lesson.age_and_difficulty"
        :key="ageAndDifficulty"
      >{{ ageAndDifficulty }}</span>
    </div>
    <div class="info">
      <span class="meta">Duration</span>
      <span class="value" v-for="duration in lesson.duration" :key="duration">{{ duration }}</span>
    </div>
    <div class="info">
      <span class="meta">Activity type</span>
      <span
        class="value"
        v-for="activityType in lesson.activity_type"
        :key="activityType"
      >{{ activityType }}</span>
    </div>
    <div class="info">
      <span class="meta">Similar lessons</span>
      <a
        class="value"
        v-for="similarLesson in lesson.similar_lessons"
        :key="similarLesson"
        :href="`/lesson/{{ lesson.id }}`"
      >{{ lesson.title }}</a>
    </div>
  </div>
</template>

<script>
import LessonList from './LessonList.vue'

export default {
  data() {
    return {
      isAuth: false,
      languagesDictionary: {},
      tags: null,
      lessons: []
    }
  },
  components: {
    LessonList
  },
  props: ['id', 'lesson'],
  methods: {
    async getFilteredLessons(language) {
      this.$router.push({ name: 'Home', params: { language: [this.languagesDictionary[language], language] } })
    }
  },
  removeFilter() {
    this.tags = null;
  },
  async created() {
    const languageArray = ['SL', 'EN']
    languageArray.forEach(language => {
      this.languagesDictionary[language.id] = language.value
    });
  }
}

</script>

<style scoped lang="scss">
.parentContainer {
  display: flex;
  flex-direction: column;
  background-color: #ffffff;
  padding: 20px;
  margin-top: 100px;
  margin-bottom: 40px;

  @media (min-width: 992px) {
    padding: 40px;
  }

  p {
    font-family: "IBM Plex Mono";
    font-size: 14px;
    margin-bottom: 10px;
    margin-top: 40px;

    @media (min-width: 992px) {
      font-size: 18px;
    }
  }
}
.lessonButtons {
  display: flex;
  justify-content: space-between;
}
.line {
  margin-top: 26px;
  border-top: 1px solid;
}
.tags {
  list-style: none;
  margin-top: 20px;
  overflow: hidden;
  padding: 0;
  cursor: pointer;
}
.tag {
  display: inline-block;
  padding-left: 10px;
  padding-right: 10px;
  margin: 10px;
  border-radius: 14px;
  border: 2px solid #3098f3;
  &.selected {
    background-color: #3098f3;
  }
}
.tag-text {
  color: #000000;
  font-family: "IBM Plex Mono";
  font-size: 14px;
  font-weight: 400;
  font-style: italic;
  letter-spacing: normal;
  line-height: 18px;
  text-align: center;
}

.lesson-text {
  /* Style for "EU member" */
  color: #252525;
  font-family: Poppins;
  font-size: 32px;
  line-height: 48px;

  @media (min-width: 992px) {
    font-size: 48px;
    line-height: 60px;
  }
}
</style>
