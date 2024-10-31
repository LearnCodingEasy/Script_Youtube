// Page [ script_youtube/script_youtube_vue/src/main.js ]

import './assets/main.css'
// My Style
import './assets/Scss/Style.scss'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'


// Import Font Awesome

// Font Awesome
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { fab } from "@fortawesome/free-brands-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";
// Add Free Icons Styles To SVG Core
library.add(fas, far, fab);

// Axios  استيراد
import axios from "axios"
axios.defaults.baseURL = "http://127.0.0.1:8000"

// Page [ facebook/facebook_vue/src/main.js ]
// Prime Vue 
import PrimeVue from "primevue/config";
// Popup
import ConfirmationService from 'primevue/confirmationservice'
import DialogService from 'primevue/dialogservice'
// Button
import Button from 'primevue/button';
// Form
import Fluid from 'primevue/fluid';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import Password from 'primevue/password';
import FloatLabel from 'primevue/floatlabel';
import Checkbox from 'primevue/checkbox';
import DatePicker from 'primevue/datepicker';
import InputGroup from 'primevue/inputgroup';
import InputGroupAddon from 'primevue/inputgroupaddon';
// File Upload
import FileUpload from 'primevue/fileupload';
// Menu
import Menubar from 'primevue/menubar';
import TieredMenu from 'primevue/tieredmenu';
// Image
import Image from 'primevue/image';
import Avatar from 'primevue/avatar';
import AvatarGroup from 'primevue/avatargroup';
// Popup
import Popover from 'primevue/popover';
import Dialog from 'primevue/dialog';
import Drawer  from 'primevue/drawer';
// panel
import Fieldset from 'primevue/fieldset';
import Stepper from 'primevue/stepper';
import StepList from 'primevue/steplist';
import StepPanels from 'primevue/steppanels';
import StepItem from 'primevue/stepitem';
import Step from 'primevue/step';
import StepPanel from 'primevue/steppanel';

// Card
import Card from 'primevue/card';
// Theme
import Noir from './presets/Noir.js';
import ThemeSwitcher from './components/Theme/ThemeSwitcher.vue';
// Toast
import Toast from 'primevue/toast';
import ToastService from 'primevue/toastservice';
// Message
import Message from 'primevue/message';
// PrimeIcons أيقونات 
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
// Quill محرر النصوص الغنية المستندة إلى 
import Editor from 'primevue/editor';
// 


import 'primeicons/primeicons.css'
import 'tailwindcss/tailwind.css'


// Prismjs For Type Code Like Vscode
import "prismjs";
import "prismjs/components/prism-pug";
import "prismjs/components/prism-scss";
import "prismjs/components/prism-git";
import "prismjs/components/prism-python";
// This Is The Theme
// import "prismjs/themes/prism-coy.css";
// import "prismjs/themes/prism-dark.css";
// import "prismjs/themes/prism-okaidia.css";
// import "prismjs/themes/prism-solarizedlight.css";
// import "prismjs/themes/prism-twilight.css";
// import "prismjs/themes/prism.css";
import "prismjs/themes/prism-tomorrow.css";

const app = createApp(App)


// eslint-disable-next-line vue/multi-word-component-names
app.component("fa", FontAwesomeIcon)


app.use(createPinia())
app.use(router, axios)


// Prime Vue 
app.use(PrimeVue, {
  theme: {
      preset: Noir,
      options: {
          prefix: 'p',
          darkModeSelector: '.p-dark',
          cssLayer: false,
      }
  }
});
app.use(ConfirmationService);
app.use(DialogService);
// Prime Theme Switcher
app.component('ThemeSwitcher', ThemeSwitcher);
// Prime Button
app.component('prime_button', Button);
// Prime Form
app.component('prime_fluid', Fluid);
app.component('prime_input_text', InputText);
app.component('prime_textarea', Textarea);
app.component('prime_input_password', Password);
app.component('prime_float_label', FloatLabel);
app.component('prime_check_box', Checkbox);
app.component('prime_date_picker', DatePicker);
app.component('prime_input_group', InputGroup);
app.component('prime_input_group_addon', InputGroupAddon);
app.component('prime_file_upload', FileUpload);
// Prime Menu
app.component('prime_menubar', Menubar);
app.component('prime_tiered_menu', TieredMenu);
app.component('prime_image', Image);
app.component('prime_avatar', Avatar);
app.component('prime_avatar_group', AvatarGroup);
app.component('prime_card', Card);
// Popup 
app.component('prime_popover', Popover);
app.component('prime_dialog', Dialog);
app.component('prime_drawer', Drawer);
// panel
app.component('prime_fieldset', Fieldset);
app.component('prime_stepper', Stepper);
app.component('prime_steplist', StepList);
app.component('prime_steppanels', StepPanels);
app.component('prime_stepitem', StepItem);
app.component('prime_step', Step);
app.component('prime_steppanel', StepPanel);



// Toast
// app.use(Toast);
app.component('prime_toast', Toast);
app.use(ToastService);
// 
app.component('prime_icon_field', IconField);
app.component('prime_input_icon', InputIcon);
// Message
// app.use(Message);
app.component('prime_message', Message);
// Editor
app.component('prime_editor', Editor);


app.mount('#app')


