<template>
  <PageContainer>
    <ArticleContainer>
      <template #title>About title</template>
      <template #default>
        <div>ABOUT TEXT</div>
      </template>
    </ArticleContainer>
  </PageContainer>
</template>

<script>
import PageContainer from "../components/PageContainer.vue";
import ArticleContainer from "../components/ArticleContainer.vue";

export default {
  components: {
    PageContainer,
    ArticleContainer,
  },
};
</script>
