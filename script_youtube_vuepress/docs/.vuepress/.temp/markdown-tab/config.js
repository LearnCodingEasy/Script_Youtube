import { CodeTabs } from "F:/Script_Youtube/script_youtube_vuepress/node_modules/@vuepress/plugin-markdown-tab/lib/client/components/CodeTabs.js";
import { Tabs } from "F:/Script_Youtube/script_youtube_vuepress/node_modules/@vuepress/plugin-markdown-tab/lib/client/components/Tabs.js";
import "F:/Script_Youtube/script_youtube_vuepress/node_modules/@vuepress/plugin-markdown-tab/lib/client/styles/vars.css";

export default {
  enhance: ({ app }) => {
    app.component("CodeTabs", CodeTabs);
    app.component("Tabs", Tabs);
  },
};
