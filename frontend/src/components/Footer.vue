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
          ><img src="../assets/logos/ZIP-logo-2-1.png" alt="ZiP logo"
        /></a>
        <a href="http://hdd.hr/" target="_blank"
          ><img src="../assets/logos/cds.png" alt="HDD logo"
        /></a>
        <a href="https://www.idi.hr/" target="_blank"
          ><img src="../assets/logos/idiz-logo-full.svg" alt="IDIZ logo"
        /></a>
        <a href="https://www.sda.sk/" target="_blank"
          ><img src="../assets/logos/SDA_logo.png" alt="SDA logo"
        /></a>
        <a href="http://www.polskadebatuje.org/" target="_blank"
          ><img src="../assets/logos/polskadebatuje.png" alt="Polska debatuje logo"
        /></a>
      </div>
      <div class="right-side">
        <img src="../assets/logos/cofoundederasmus.png" alt="EU logo" />
      </div>
    </div>
  </footer>
</template>

<style lang="scss" scoped>
footer {
  padding-inline: 60px;
  border-top: 2px solid black;

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
