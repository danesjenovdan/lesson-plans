<template>
  <footer>
    <div class="links">
      <a href="/about">{{ $t("footer.about") }}</a>
      <a href="/howto">{{ $t("footer.howto") }}</a>
    </div>
    <div class="divider"></div>
    <div class="logos">
      <div class="left-side">
        <a href="https://zainproti.si/" target="_blank"
          ><img src="../assets/ZiP_logo.png" alt="ZiP logo"
        /></a>
        <a href="http://hdd.hr/" target="_blank"
          ><img src="../assets/HDD_logo.png" alt="HDD logo"
        /></a>
        <a href="https://idebate.org/" target="_blank"
          ><img src="../assets/IDEA_logo.png" alt="IDEA logo"
        /></a>
      </div>
      <div class="right-side">
        <img src="../assets/EU_logo.png" alt="EU logo" />
      </div>
    </div>
  </footer>
</template>

<style lang="scss" scoped>
footer {
  padding-inline: 60px;

  @media (max-width: 991.98px) {
    padding-inline: 20px;
  }

  .links {
    display: flex;
    gap: 100px;
    padding: 20px;
    font-family: "Inter", sans-serif;
    font-size: 16px;
    font-weight: 600;
    color: #252525;

    @media (max-width: 575.98px) {
      justify-content: space-evenly;
    }

    a,
    a:visited {
      color: inherit;
      text-decoration: none;
      border-bottom: 1px solid #000;
    }
  }

  .divider {
    border-bottom: 2px solid #000;
  }

  .logos {
    display: flex;
    justify-content: space-between;
    padding: 16px 20px;

    @media (max-width: 575.98px) {
      justify-content: center;
      flex-wrap: wrap;
      gap: 20px;
    }

    .left-side,
    .right-side {
      display: flex;
      flex-wrap: wrap;
      gap: 40px;

      @media (max-width: 575.98px) {
        gap: 20px;
      }
    }

    img {
      height: 45px;
    }
  }
}
</style>
