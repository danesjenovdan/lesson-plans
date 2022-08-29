<template>
  <PageContainer>
    <Lesson class="lesson" :lesson="lesson" :id="id" />
  </PageContainer>
</template>

<script>
import PageContainer from "../components/PageContainer.vue";
import Lesson from "../components/Lesson.vue";

export default {
  data() {
    return {
      lesson: {},
    };
  },
  components: {
    PageContainer,
    Lesson,
  },
  props: ["id"],
  async created() {
    this.lesson = await this.$store.dispatch("getLesson", { id: this.id });
    this.$store.state.lessons.lesson = this.lesson;
  },
};
</script>
