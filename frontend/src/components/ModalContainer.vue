<template>
  <div class="modal-bg">
    <div class="modal">
      <div class="container">
        <h4 v-if="!!$slots.title"><slot name="title" /></h4>
        <slot />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.modal-bg {
  position: fixed;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999999999;
  background: rgba(0, 0, 0, 0.5);

  .modal {
    position: relative;
    display: flex;
    max-width: 600px;
    max-height: 100%;
    background: #f1f2f2;
    border: 2px solid #000;

    @media (min-width: 992px) {
      margin: 0 auto;
      max-height: 90vh;
    }

    .container {
      padding: 20px 30px;
      overflow-y: auto;

      h4 {
        margin: 0;
        color: #252525;
        font-family: "Fredoka", sans-serif;
        font-weight: 600;
        font-size: 32px;
      }
    }
  }
}
</style>
