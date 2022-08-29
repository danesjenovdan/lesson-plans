<template>
  <div class="split-container">
    <div class="container-child">
      <div class="wrapper">
        <div class="debate-logo"></div>
        <router-link to="/" class="back-link">Back to the list</router-link>
        <lesson class="lesson" :lesson="lesson" :id="id" />
      </div>
    </div>
  </div>
</template>

<script>
import Lesson from "../components/Lesson.vue";

export default {
  data() {
    return {
      lesson: {},
    };
  },
  components: {
    Lesson,
  },
  props: ["id"],
  async created() {
    this.lesson = await this.$store.dispatch("getLesson", { id: this.id });
    this.$store.state.lessons.lesson = this.lesson;
    const choice = this.votes.find((vote) => vote.lesson === this.lesson.id);
    if (choice) this.lesson.choice = choice.choices;
  },
};
</script>

<style scoped lang="scss">
.container-child {
  background-color: #f1f2f2;

  .wrapper {
    max-width: 1300px;
    margin-inline: auto;

    .back-link {
      font-family: "Inter", sans-serif;
      font-size: 14px;
      text-decoration: none;
      color: #252525;

      &:before {
        content: '';
        display: inline-block;
        width: 18px;
        height: 10px;
        background-image: url("../assets/back-arrow.svg");
        background-repeat: no-repeat;
        background-position: center center;
        background-size: 31px;
        transform: rotate(180deg);
        margin-right: 10px;
      }
    }
  }
}
</style>
