import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import svgLoader from "vite-svg-loader";
import vueI18n from "@intlify/vite-plugin-vue-i18n";
import { fileURLToPath } from "url";
import { resolve, dirname } from "node:path";
import yaml from "@rollup/plugin-yaml";
import { Remarkable } from "remarkable";

const md = new Remarkable();

const processLocaleMarkdown = (messages) => {
  Object.keys(messages).forEach((key) => {
    if (typeof messages[key] === "object" && messages[key]) {
      processLocaleMarkdown(messages[key]);
    } else if (key.startsWith("md-")) {
      messages[key] = md.render(messages[key]);
    }
  });
  return messages;
};

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    yaml({
      transform(data) {
        return processLocaleMarkdown(data ?? {});
      },
    }),
    vue(),
    svgLoader({
      defaultImport: "url",
    }),
    vueI18n({
      // if you want to use Vue I18n Legacy API, you need to set `compositionOnly: false`
      compositionOnly: false,
      // you need to set i18n resource including paths !
      include: resolve(
        dirname(fileURLToPath(import.meta.url)),
        "./src/locales/**/.js"
      ),
    }),
  ],
});
