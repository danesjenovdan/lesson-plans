<template>
  <div class="page-container">
    <div class="container-child">
      <div class="wrapper">
        <router-link to="/" class="back-link">{{ $t('lesson.back') }}</router-link>
        <slot />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.page-container {
  display: flex;
  height: 100%;

  .container-child {
    flex: 1;
    padding-inline: 60px;
    background-color: #f1f2f2;

    @media (max-width: 991.98px) {
      padding-inline: 20px;
    }

    .wrapper {
      max-width: 1370px;
      margin-inline: auto;
      margin-top: 50px;

      @media (max-width: 991.98px) {
        margin-top: 20px;
      }

      .back-link {
        font-family: "Inter", sans-serif;
        font-size: 14px;
        text-decoration: none;
        color: #252525;

        &:before {
          content: "";
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
}
</style>
