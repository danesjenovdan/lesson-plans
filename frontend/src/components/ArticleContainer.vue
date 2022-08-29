<template>
  <div class="article-container">
    <div class="main-content">
      <h1><slot name="title" /></h1>
      <slot name="subtitle" />
      <div class="main-text"><slot /></div>
    </div>
    <div v-if="!!$slots.sidebar" class="sidebar">
      <slot name="sidebar" />
    </div>
  </div>
</template>

<style scoped lang="scss">
.article-container {
  display: flex;
  gap: 50px;
  margin-top: 50px;
  margin-bottom: 40px;

  @media (max-width: 991.98px) {
    flex-direction: column;
    gap: 20px;
  }

  .main-content {
    flex: 2;

    h1 {
      margin: 0;
      color: #252525;
      font-family: "Fredoka", sans-serif;
      font-weight: 600;
      font-size: 46px;

      @media (max-width: 575.98px) {
        font-size: 32px;
      }
    }

    .main-text {
      margin-top: 48px;
      color: #252525;
      font-family: "Inter", sans-serif;
      font-size: 21px;
      line-height: 31px;

      @media (max-width: 575.98px) {
        margin-top: 28px;
        font-size: 16px;
         line-height: 24px;
      }
    }
  }

  .sidebar {
    flex: 1;
  }
}
</style>
