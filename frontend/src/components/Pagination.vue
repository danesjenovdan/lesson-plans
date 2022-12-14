<template>
    <div v-if="pagesNo > 1" class="pagination">
      <div>
        <!-- <button @click="goToPage(1)">
          <svg
            class="rotate-arrow"
            height="15"
            width="15"
            fill="#000000"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            viewBox="0 0 24 24"
            version="1.1"
            x="0px"
            y="0px"
          >
            <title>icon/double-chevron-right-solid</title>
            <desc>Created with Sketch Beta.</desc>
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <path
                d="M11.8789,2.6816 L13.2929,1.2676 L23.9999,11.9746 L13.2929,22.6816 L11.8789,21.2676 L21.1719,11.9746 L11.8789,2.6816 Z M5.293,22.6816 L3.879,21.2676 L13.172,11.9746 L3.879,2.6816 L5.293,1.2676 L16,11.9746 L5.293,22.6816 Z"
                fill="#000000"
              />
            </g>
          </svg>
        </button> -->
        <button @click="goToPage(active - 1)">
          <svg
            height="15"
            width="15"
            fill="#000000"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            viewBox="0 0 24 24"
            version="1.1"
            x="0px"
            y="0px"
          >
            <title>icon/chevron-left-solid</title>
            <desc>Created with Sketch Beta.</desc>
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <polygon
                fill="#000000"
                points="16.1211 21.2676 6.8281 11.9746 16.1211 2.6816 14.7071 1.2676 4.0001 11.9746 14.7071 22.6816"
              />
            </g>
          </svg>
        </button>
        <ul>
            <li v-if="active > 2" class="page" @click="goToPage(1)">1</li>
            <li v-if="active > 3" class="dots">...</li>
            <li v-if="active - 1 > 0" @click="goToPage(active - 1)">{{ active - 1 }}</li>
            <li class="active-page">{{ active }}</li>
            <li v-if="active + 1 < pagesNo" @click="goToPage(active + 1)">{{ active + 1 }}</li>
            <li v-if="pagesNo - active > 2" class="dots">...</li>
            <li v-if="active < pagesNo" @click="goToPage(pagesNo)">{{ pagesNo }}</li>
        </ul>
        <button @click="goToPage(active + 1)">
          <svg
            class="rotate-arrow"
            height="15"
            width="15"
            fill="#000000"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            viewBox="0 0 24 24"
            version="1.1"
            x="0px"
            y="0px"
          >
            <title>icon/chevron-left-solid</title>
            <desc>Created with Sketch Beta.</desc>
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <polygon
                fill="#000000"
                points="16.1211 21.2676 6.8281 11.9746 16.1211 2.6816 14.7071 1.2676 4.0001 11.9746 14.7071 22.6816"
              />
            </g>
          </svg>
        </button>
        <!-- <button @click="goToPage(pagesNo)">
          <svg
            height="15"
            width="15"
            fill="#ffffff"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            viewBox="0 0 24 24"
            version="1.1"
            x="0px"
            y="0px"
          >
            <title>icon/double-chevron-right-solid</title>
            <desc>Created with Sketch Beta.</desc>
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <path
                d="M11.8789,2.6816 L13.2929,1.2676 L23.9999,11.9746 L13.2929,22.6816 L11.8789,21.2676 L21.1719,11.9746 L11.8789,2.6816 Z M5.293,22.6816 L3.879,21.2676 L13.172,11.9746 L3.879,2.6816 L5.293,1.2676 L16,11.9746 L5.293,22.6816 Z"
                fill="#000000"
              />
            </g>
          </svg>
        </button> -->
      </div>
    </div>
</template>

<script>
export default {
  props: {
    active: {
      type: Number,
      default: 1
    },
    pagesNo: {
      type: Number,
      default: 1
    }
  },
  data () {
    return {
    }
  },
  methods: {
    goToPage (p) {
      this.$emit('go-to-page', p)
    }
  }
}
</script>

<style scoped lang="scss">
.pagination {
  width: 100%;
  margin-bottom: 20px;

  .rotate-arrow {
    transform: rotate(180deg);
  }

  & > div {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  ul {
    display: inline-flex;
    padding: 0 0.5rem;
    margin: 0;

    li {
      list-style: none;
      margin: 0 0.1rem;
    }
  }

  button, li {
    width: 2rem;
    height: 2rem;
    border-radius: 50%;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    font-size: 18px;
    font-weight: 500;
    font-style: italic;
    color: #252525;
    cursor: pointer;
    border: 1px solid transparent;

    &.active-page {
        background-color: #aefcd8;
    }

    &:hover, &.active-page:hover {
        background-color: #c1ead7;
    }

    &.dots {
      background-color: transparent;
      cursor: default;
      color: #252525;
    }
  }

  button {
    margin: 0 0.25rem;
    background-color: #c1ead7;
    border: 1px solid #c1ead7;
  }
}
</style>
  