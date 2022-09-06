<template>
  <PageContainer>
    <ArticleContainer>
      <template #title>{{ $t("howTo.title") }}</template>
      <template #default>
        <div class="md-content" v-html="$t('howTo.md-content')"></div>
      </template>
    </ArticleContainer>
  </PageContainer>
</template>

<script>
import PageContainer from "../components/PageContainer.vue";
import ArticleContainer from "../components/ArticleContainer.vue";
import messages from "../locales/how-to.yaml";

export default {
  components: {
    PageContainer,
    ArticleContainer,
  },
  i18n: {
    messages,
  },
};
</script>
