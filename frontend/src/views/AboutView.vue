<template>
  <PageContainer>
    <ArticleContainer>
      <template #title>About</template>
      <template #default>
        <p>Resourcebase was created as an online educational resource through the project Innovate debate, run by a consortium of 6 organizations and funded under the Erasmus + funding scheme.</p>
        <p>During three years of development, all the materials presented in this tool were created and reviewed by educators and students they worked with. The site is designed to grow and develop with new materials as organizations that made the initial consortium grow and develop their partnership and as other youth debate organizations join our effort to expand access to debate.</p>
        <p>Project "Innovate debate: Applied curriculum for debate-based youth work" is funded under the Erasmus+ program of the Europan Union. The project code is 2019-2-HR01-KA205-061076.</p>
        <p>It is a joint endeavor of Croatia debate society, International debate education association, Za in Proti, Slovak debate association, Polish debate foundation, and the Institute for Social Sciences at the University of Zagreb.</p>
        <p>The European Commission's support for the production of this publication does not constitute an endorsement of the contents, which reflect the views only of the authors, and the Commission cannot be held responsible for any use which may be made of the information contained therein.</p>
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
