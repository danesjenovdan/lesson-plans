<template>
  <ArticleContainer>
    <template #title>
      {{ lesson.title }}
    </template>
    <template #subtitle>
      <ul class="tags">
        <li class="tag" v-for="topic in lesson.topic" :key="topic">
          <span class="tag-text">{{ topic }}</span>
        </li>
      </ul>
    </template>
    <template #default>
      {{ lesson.description }}
    </template>
    <template #sidebar>
      <div class="sidebar-content">
        <button class="download" @click="modalVisible = true">
          Download lesson
          <img src="../assets/download.svg" />
        </button>
        <div class="infos">
          <div class="info">
            <span class="meta">Material type</span>
            <span class="value">{{ lesson.material_type?.join(", ") }}</span>
          </div>
          <div class="info">
            <span class="meta">Language</span>
            <span class="value">{{ lesson.language?.join(", ") }}</span>
          </div>
          <div class="info">
            <span class="meta">Topic</span>
            <span class="value">{{ lesson.topic?.join(", ") }}</span>
          </div>
          <div class="info">
            <span class="meta">Age and difficulty</span>
            <span class="value">{{
              lesson.age_and_difficulty?.join(", ")
            }}</span>
          </div>
          <div class="info">
            <span class="meta">Duration</span>
            <span class="value">{{ lesson.duration?.join(", ") }}</span>
          </div>
          <div class="info">
            <span class="meta">Activity type</span>
            <span class="value">{{ lesson.activity_type?.join(", ") }}</span>
          </div>
          <div class="info similar-lessons">
            <span class="meta">Similar lessons</span>
            <div class="values">
              <div
                v-for="similarLesson in lesson.similar_lessons"
                :key="similarLesson"
                class="value"
              >
                <a :href="`/lesson/${similarLesson.id}`">
                  {{ similarLesson.title }}
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </template>
  </ArticleContainer>
  <DownloadModal
    v-if="modalVisible"
    @success="modalVisible = false"
    :lesson="lesson"
  />
</template>

<script>
import ArticleContainer from "../components/ArticleContainer.vue";
import DownloadModal from "./DownloadModal.vue";

export default {
  components: {
    ArticleContainer,
    DownloadModal,
  },
  props: ["id", "lesson"],
  data() {
    return {
      modalVisible: false,
    };
  },
};
</script>

<style scoped lang="scss">
.tags {
  list-style: none;
  margin: 10px 0 0 0;
  padding: 0;

  .tag {
    display: inline-block;
    background-color: #c1ead7;
    padding: 6px 14px;

    & + .tag {
      margin-left: 14px;
    }

    .tag-text {
      color: #252525;
      font-family: "Inter", sans-serif;
      font-size: 18px;
    }
  }
}

.sidebar-content {
  .download {
    position: relative;
    display: flex;
    align-items: center;
    gap: 23px;
    padding: 16px 34px;
    background: #fff;
    border: 2px solid #000;
    font-family: "Inter", sans-serif;
    font-size: 18px;
    font-weight: 600;
    color: #252525;
    cursor: pointer;
    transform-style: preserve-3d;

    &::before {
      content: "";
      display: block;
      position: absolute;
      inset: 0;
      border: 2px solid #000;
      background-color: #aefcd8;
      transform: translate(9px, 9px) translateZ(-1px);
    }

    img {
      width: 20px;
      height: 25px;
    }
  }

  .infos {
    margin-top: 45px;

    .info {
      border: 1px solid #000;
      padding: 18px;
      width: fit-content;

      & + .info {
        margin-top: -1px;
      }

      .meta {
        color: #252525;
        font-family: "Inter", sans-serif;
        font-size: 14px;
        font-style: italic;
        margin-right: 18px;
      }

      .value {
        color: #252525;
        font-family: "Inter", sans-serif;
        font-size: 18px;
        font-weight: 600;
      }

      &.similar-lessons {
        width: auto;
        display: flex;

        .meta {
          width: min-content;
        }

        .values {
          .value {
            & + .value {
              margin-top: 14px;
            }

            a {
              &,
              &:visited {
                display: inline;
                font-size: 16px;
                text-decoration: none;
                color: #252525;
                border-bottom: 1px solid #000;
              }

              &::before {
                content: "";
                display: inline-block;
                background-image: url("../assets/open-new-page.svg");
                background-repeat: no-repeat;
                width: 14px;
                height: 14px;
                margin-right: 5px;
              }
            }
          }
        }
      }
    }
  }
}
</style>
