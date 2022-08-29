<template>
  <div class="split-container">
    <div class="container-child">
      <div class="wrapper">
        <div class="debate-logo"></div>
        <router-link to="/">Back to the list</router-link>
        <lesson class="lesson" :lesson="lesson" :id="id" />
      </div>
    </div>
  </div>
</template>

<script>
import Lesson from '../components/Lesson.vue'

export default {
  data() {
    return {
      lesson: {},
      }
    },
  components: {
    Lesson,
    },
  props: ['id'],
  async created() {
    this.lesson = await this.$store.dispatch('getLesson', {id: this.id})
    this.$store.state.lessons.lesson = this.lesson
    const choice = this.votes.find(vote => vote.lesson === this.lesson.id)
    if (choice) this.lesson.choice = choice.choices;
  }
}

</script>

<style scoped lang="scss">
</style>
