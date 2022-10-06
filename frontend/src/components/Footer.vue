<template>
  <footer>
    <div class="links">
      <div class="left-side">
        <a href="/about">{{ $t("footer.about") }}</a>
        <a href="/howto">{{ $t("footer.howto") }}</a>
      </div>
      <div class="right-side">
        <div class="locale">
          <label for="locale-select">{{ $t("filters.language") }}</label>
          <select v-model="$i18n.locale" id="locale-select">
            <option
              v-for="locale in $i18n.availableLocales"
              :key="`locale-${locale}`"
              :value="locale"
            >
              {{ locale }}
            </option>
          </select>
        </div>
      </div>
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
          ><img
            src="../assets/logos/polskadebatuje.png"
            alt="Polska debatuje logo"
        /></a>
        <a href="https://idebate.net/" target="_blank"
          ><img
            src="../assets/logos/IDEA_logo.png"
            alt="IDEA logo"
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

  .divider {
    border-bottom: 2px solid #000;
  }

  .links,
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

  .links {
    padding-block: 10px;

    .left-side {
      align-items: center;
      gap: 100px;
      padding-block: 15px;
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

    .right-side {
      align-items: center;

      .locale {
        label {
          font-family: "Inter", sans-serif;
          font-size: 16px;
          font-weight: 600;
          font-style: normal;
          color: #252525;
          margin-right: 10px;
        }

        select {
          width: 70px;
          height: 35px;
          padding: 5px;
          border-color: #252525;
          border-width: 1px;
          font-family: inherit;
          font-size: 16px;
        }
      }
    }
  }
}
</style>
