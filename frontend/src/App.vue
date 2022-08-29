<template>
  <div class="content-wrapper">
    <div class="content">
      <router-view />
    </div>
    <Footer />
  </div>
</template>

<script>
import Footer from "./components/Footer.vue";

export default {
  components: {
    Footer,
  },
};
</script>

<style lang="scss">
@import "src/index.scss";

a:link {
  color: #252525;
}

h1 {
  color: #252525;
  font-family: "Poppins";
  font-size: 24px;
  font-weight: 900;
  line-height: 48px;
  position: relative;
  display: inline-block;
  &::before {
    content: "";
    display: block;
    position: absolute;
    bottom: 15px;
    z-index: -1;
    width: 100%;
    height: 16px;
    background-color: #ffcc00;
  }
}

@media (max-width: 1119px) {
  h1 {
    font-size: 22px;
  }
}
.modal {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: rgba(48, 152, 243, 0.8);
  z-index: 10;
}
.modal-inner {
  max-width: 500px;
  margin: auto;
  margin-top: 100px;
  background-color: #ffffff;
  padding: 100px;
}
@media (max-width: 767px) {
  .team-heading {
    width: calc(100% - 24px) !important;
  }
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) {
  .visible-xs {
    display: none !important;
  }
}
</style>
