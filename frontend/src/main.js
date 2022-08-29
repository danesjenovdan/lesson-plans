import { createApp } from 'vue'
import { createWebHistory , createRouter } from "vue-router";
import Toast, { TYPE } from "vue-toastification";
import "vue-toastification/dist/index.css";
import Home from './views/Home.vue'
import LessonView from './views/LessonView.vue'
import AboutView from './views/AboutView.vue'
import HowToView from './views/HowToView.vue'
import store from './store/store'
import App from './App.vue'
import IconComponent from './components/IconComponent.vue'

import { createI18n } from 'vue-i18n'

import en from './locales/en.json'

const i18n = createI18n({
  locale: 'en',
  messages: {
    en,
  }
})

const options = {
  toastDefaults: {
      // ToastOptions object for each type of toast
      [TYPE.ERROR]: {
          timeout: 10000,
          closeButton: false,
      },
      [TYPE.SUCCESS]: {
          icon:  IconComponent,
          closeButtonClassName: "toast-button-class",
          toastClassName: "toast-custom-background",
          bodyClassName: ["toast-black-font-stlye"]
      }
  }
};


const routes = [
    {
      path: '/',
      name: 'Home',
      component: Home,
      props: true
    },
    {
      path: '/lesson/:id',
      name: 'LessonView',
      component: LessonView,
      props: true
    },
    {
      path: '/about',
      name: 'AboutView',
      component: AboutView,
      props: true
    },
    {
      path: '/howto',
      name: 'HowToView',
      component: HowToView,
      props: true
    },
  ];

const router = createRouter({
  history: createWebHistory(),
  routes,
})

createApp(App).use(i18n).use(store).use(router).use(Toast, options).mount('#app')
