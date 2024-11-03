# Vite Press

## Github

- [Github](https://github.com/LearnCodingEasy/Script_Youtube)

* Git Clone Project 📦

```cmd
git clone https://github.com/LearnCodingEasy/script_youtube.git
```

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

## Vuepress

```cmd
npm init vuepress script_youtube_vuepress
```

```cmd
cd script_youtube_vuepress
```

```cmd
npm install -D sass-embedded
```

Run Vuepress

```cmd
npm run docs:dev
```

Open Docs File 📁 > Create File 📁

```
index.md
```

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

## LICENSE

Create File 📝 [ LICENSE ]

```text
LICENSE
```

```text
MIT License
Copyright (c) 2024 Hossam Rashad
```

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

## Django

Create Virtual Environment

```cmd
python -m venv script_youtube_virtual_environment
```

- Activate Virtual Environment

```cmd
script_youtube_virtual_environment\Scripts\activate
```

- Install Django

```cmd
pip install django
```

- 5 Install Django Libraries
  [
  1 - djangorestframework |
  2 - djangorestframework-simplejwt |
  3 - django-cors-headers |
  4 - pillow
  ]

```cmd
pip install djangorestframework djangorestframework-simplejwt django-cors-headers pillow
```

### Create Django Project

```cmd
django-admin startproject script_youtube_django
```

### Create Django App Account

```cmd
cd script_youtube_django
```

```cmd
python manage.py startapp account
```

### Settings 📝

Setup Django File 📝 Settings

```python
# Page [script_youtube/script_youtube_django/script_youtube_django/settings.py]

from datetime import timedelta
ALLOWED_HOSTS = []
WEBSITE_URL = "http://127.0.0.1:8000"
AUTH_USER_MODEL = "account.User"
SIMPLE_JWT = {
  "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
  "REFRESH_TOKEN_LIFETIME": timedelta(days=180),
  "ROTATE_REFRESH_TOKENS": False,
}

REST_FRAMEWORK = {
  "DEFAULT_AUTHENTICATION_CLASSES": (
      "rest_framework_simplejwt.authentication.JWTAuthentication",
  ),
  "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

CORS_ALLOWED_ORIGINS = [
  "http://localhost:5173",
  "http://localhost:5174",
]

CSRF_TRUSTED_ORIGINS = [
  "http://localhost:5173",
  "http://localhost:5174",
]

INSTALLED_APPS = [
    # ...
    # Apps
    "account",
    # Libraries
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
]

MIDDLEWARE = [
    # ...
    "corsheaders.middleware.CorsMiddleware",
    # ...
]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
```

### Models 📝

- Setup Django App 📦 Account
- Edite Page 📝 [ models.py ] Inside App Account

```python
# Page [ script_youtube/script_youtube_django/account/models.py ]

import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone

class CustomUserManager(UserManager):
    def _create_user(self, name, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(name, email, password, **extra_fields)

    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(name, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=255, blank=True, null=True, default="")
    surname = models.CharField(max_length=255, blank=True, default="")
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
    cover = models.ImageField(upload_to="covers", blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []
```

### Admin 📝

Edite Page 📝 [ admin.py ] Inside App Account

```python
from django.contrib import admin
from .models import User
admin.site.register(User)
```

### Serializers 📝

Create Page 📝 [ serializers.py ] Inside App Account

```text
serializers.py
```

```python
# Page [ script_youtube/script_youtube_django/account/serializers.py ]
from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = (
      "id",
      "name",
      "surname",
      "email",
      "date_of_birth",
      "gender",
    )
```

### Forms 📝

Create Page 📝[ forms.py ] Inside App Account

```text
forms.py
```

```python
# Page [ script_youtube/script_youtube_django/account/forms.py ]

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "name",
            "surname",
            "email",
            "date_of_birth",
            "gender",
            "password1",
            "password2",
        )
```

### Api 📝

Create Page 📝 [ api.py ] Inside App Account

```text
api.py
```

```python
# Page [ script_youtube/script_youtube_django/account/api.py ]

from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from .forms import SignupForm
from .models import User
from .serializers import UserSerializer

@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def signup(request):

  data = request.data
  message = "success"

  form = SignupForm(
    {
      "name": data.get("name"),
      "surname": data.get("surname"),
      "email": data.get("email"),
      "date_of_birth": data.get("date_of_birth"),
      "gender": data.get("gender"),
      "password1": data.get("password1"),
      "password2": data.get("password2"),
    }
  )

  if form.is_valid():
    user = form.save()
    user.is_active = True
    user.save()

    return JsonResponse({"message": message, "email_sent": True}, safe=False)
  else:
    message = form.errors.as_json()

  print(message)

  return JsonResponse({"message": message}, safe=False)


@api_view(["GET"])
def me(request):
  return JsonResponse(
    {
      "id": request.user.id,
      "name": request.user.name,
      "surname": request.user.surname,
      "email": request.user.email,
      "date_of_birth": request.user.date_of_birth,
      "gender": request.user.gender,
    }
  )
```

### Urls 📝

Create Page 📝[ urls.py ] Inside App Account

```text
urls.py
```

```python
# Page [ script_youtube/script_youtube_django/account/urls.py ]
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path("me/", api.me, name="me"),
    path("signup/", api.signup, name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
```

- Setup Page 📝 [ urls.py ] Inside script_youtube_django

```python
# Page [ script_youtube/script_youtube_django/script_youtube_django/urls.py ]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("api/", include("account.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Superuser 👉️

Create Superuser

```cmd
python manage.py createsuperuser
```

### Makemigrations 🛠️

🛠️ Modifications To Models File

```cmd
python manage.py makemigrations
```

### Makemigrations 🛠️

🛠️ Migrate To The Database

```cmd
python manage.py migrate
```

### Run Server 🚀

🚀 Try The Project On Your Device

```cmd
python manage.py runserver
```

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

## Vue

### Create Vue Project

```cmd
npm create vue@latest
```

- 11 Choose Vite [ Project name & Select a framework ]

```cmd
√ Project name: ... script_youtube_vue
√ Add TypeScript? ... [No] / Yes
√ Add JSX Support? ... [No] / Yes
√ Add Vue Router for Single Page Application development? ... No / [Yes]
√ Add Pinia for state management? ... No / [Yes]
√ Add Vitest for Unit Testing? ... [No] / Yes
√ Add an End-to-End Testing Solution? » [No]
√ Add ESLint for code quality? ... No / [Yes]
√ Add Prettier for code formatting? ... No / [Yes]
√ Add Vue DevTools 7 extension for debugging? (experimental) ... [No] / Yes

Scaffolding project in E:\Projects\script_youtube\script_youtube_vue...

Done. Now run:
  cd script_youtube_vue
  npm install
  npm run format
  npm run build
  npm run dev
```

### Install Vue Libraries

[
1 - Tailwind |
2 - PrimeVue |
3 - scss |
4 - Axios |
5 - Font Awesome |
6 - Pwa |
7 - Prism |
8 - |
9 - |
]

```cmd
npm install -D tailwindcss postcss autoprefixer
```

```cmd
npx tailwindcss init -p
```

```cmd
npm install primevue primeicons
```

```cmd
npm install @primevue/themes
```

```cmd
npm install quill
```

```cmd
npm install -D sass@latest
```

```cmd
npm install axios
```

```cmd
npm i --save @fortawesome/fontawesome-svg-core @fortawesome/vue-fontawesome@latest @fortawesome/vue-fontawesome@prerelease @fortawesome/free-solid-svg-icons @fortawesome/free-brands-svg-icons @fortawesome/free-regular-svg-icons
```

```cmd
npm install -D vite-plugin-pwa
```

```cmd
npm i swiper
```

```cmd
npm i prismjs vue-prism-component
```

### Sutap Vue Libraries

#### Tailwind

Configure Tailwind

- File 📝 [ tailwind.config.js ]

```js
// Page [ script_youtube/script_youtube_vue/tailwind.config.js ]
content: [
"./index.html",
"./src/**/*.{vue,js,ts,jsx,tsx}",
],
```

- style.css

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

#### Import Font Awesome

```js
// Page [ script_youtube/script_youtube_vue/src/main.js ]
// Font Awesome
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { fab } from "@fortawesome/free-brands-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";
// Add Free Icons Styles To SVG Core
library.add(fas, far, fab);

// eslint-disable-next-line vue/multi-word-component-names
app.component("fa", FontAwesomeIcon);
```

#### Setup Pwa

- Edit Page 📝 [ vite.config.js ]

```js
// Page [ script_youtube/script_youtube_vue/vite.config.js ]

import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// For Pwa
// https://vite-pwa-org.netlify.app/guide/
import { VitePWA } from "vite-plugin-pwa";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    // For Pwa
    VitePWA({
      registerType: "autoUpdate",
      workbox: {
        globPatterns: ["**/*.{js,css,html,ico,png,svg}"],
        clientsClaim: true,
        skipWaiting: true,
        cleanupOutdatedCaches: false,
        offlineGoogleAnalytics: true,
        sourcemap: true,
        runtimeCaching: [
          {
            urlPattern: ({ request }) =>
              request.destination === "document" ||
              request.destination === "script" ||
              request.destination === "style" ||
              request.destination === "image" ||
              request.destination === "font",
            handler: "StaleWhileRevalidate",
            options: {
              cacheName: "assets-cache",
              expiration: {
                maxEntries: 100,
                maxAgeSeconds: 60 * 60 * 24 * 30
              }
            }
          }
        ]
      },
      devOptions: {
        enabled: true
      },
      injectRegister: "auto",
      includeAssets: ["**/*"],
      manifest: {
        name: "Script Youtube",
        short_name: "Script Youtube",
        description: "My Awesome App Script Youtube",
        theme_color: "#ffffff",
        icons: [
          {
            src: "./images/icons/script_youtube_icon_72x72.png",
            type: "image/png",
            sizes: "72x72",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/script_youtube_icon_96x96.png",
            type: "image/png",
            sizes: "96x96",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/script_youtube_icon_128x128.png",
            type: "image/png",
            sizes: "128x128",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/script_youtube_icon_144x144.png",
            type: "image/png",
            sizes: "144x144",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/script_youtube_icon_152x152.png",
            type: "image/png",
            sizes: "152x152",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/script_youtube_icon_192x192.png",
            type: "image/png",
            sizes: "192x192",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/script_youtube_icon_384x384.png",
            type: "image/png",
            sizes: "384x384",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/script_youtube_icon_512x512.png",
            type: "image/png",
            sizes: "512x512",
            purpose: "any maskable"
          }
        ],
        screenshots: [
          {
            src: "./images/screenshots/screenshots.png",
            sizes: "640x480",
            type: "image/png",
            form_factor: "wide"
            // "form_factor": "narrow"
          }
        ]
      }
    })
  ],

  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url))
    }
  }
});
```

- Add Image Inside Public

```
├── public/
│   ├── images/
│   |   ├── icons/
│   │   |   ├── 🖼️ facebook_icon_72x72.png
│   │   |   ├── 🖼️ facebook_icon_96x96.png
│   │   |   ├── 🖼️ facebook_icon_128x128.png
│   │   |   ├── 🖼️ facebook_icon_144x144.png
│   │   |   ├── 🖼️ facebook_icon_152x152.png
│   │   |   ├── 🖼️ facebook_icon_192x192.png
│   │   |   ├── 🖼️ facebook_icon_384x384.png
│   │   |   ├── 🖼️ facebook_icon_512x512.png
│   |   ├── screenshots/
│   │   |   ├── 🖼️ screenshots.png
```

- Setup Axios

```js
// Axios  استيراد
import axios from "axios";
axios.defaults.baseURL = "http://127.0.0.1:8000";

app.use(router, axios);
```

- Setup PrimeVue

* Create Page 📝 [ primeTheme.js ] Inside stores

```js
// Page [ script_youtube/script_youtube_vue/src/stores/primeTheme.js ]

import { reactive } from "vue";
export default {
  install: (app) => {
    const _appState = reactive({ theme: "Aura", darkTheme: false });
    app.config.globalProperties.$appState = _appState;
  }
};
```

- Create Page [ Theme/ThemeSwitcher.vue ] Inside components

```html
<template>
  <span class="">
    <ul class="flex list-none m-0 p-0 gap-2 items-center">
      <li>
        <button
          type="button"
          class="inline-flex w-8 h-8 p-0 items-center justify-center surface-0 dark:surface-800 border border-surface-200 dark:border-surface-600 rounded-full"
          @click="onThemeToggler"
        >
          <i :class="`dark:text-white pi ${iconClass}`" />
        </button>
      </li>
    </ul>
  </span>
</template>
```

```js
<script>
  import { updatePreset, updateSurfacePalette } from '@primevue/themes'

  export default {
    data() {
      return {
        iconClass: 'pi-moon',
        selectedPrimaryColor: 'noir',
        selectedSurfaceColor: null
      }
    },
    methods: {
      onThemeToggler() {
        const root = document.getElementsByTagName('html')[0]
        root.classList.toggle('p-dark')
        this.iconClass = this.iconClass === 'pi-moon' ? 'pi-sun' : 'pi-moon'
      },

      updateColors(type, color) {
        if (type === 'primary') this.selectedPrimaryColor = color.name
        else if (type === 'surface') this.selectedSurfaceColor = color.name

        this.applyTheme(type, color)
      },
      applyTheme(type, color) {
        if (type === 'primary') {
          updatePreset(this.getPresetExt())
        } else if (type === 'surface') {
          updateSurfacePalette(color.palette)
        }
      },
      onRippleChange(value) {
        this.$primevue.config.ripple = value
      }
    },
    computed: {
      rippleActive() {
        return this.$primevue.config.ripple
      }
    }
  }
</script>
```

- Create Page 📝 [ presets/Noir.js ] Inside src

```js
import { definePreset } from "@primevue/themes";
import Aura from "@primevue/themes/aura";

const Noir = definePreset(Aura, {
  semantic: {
    primary: {
      50: "{surface.50}",
      100: "{surface.100}",
      200: "{surface.200}",
      300: "{surface.300}",
      400: "{surface.400}",
      500: "{surface.500}",
      600: "{surface.600}",
      700: "{surface.700}",
      800: "{surface.800}",
      900: "{surface.900}",
      950: "{surface.950}"
    },
    colorScheme: {
      light: {
        primary: {
          color: "{primary.950}",
          contrastColor: "#ffffff",
          hoverColor: "{primary.900}",
          activeColor: "{primary.800}"
        },
        highlight: {
          background: "{primary.950}",
          focusBackground: "{primary.700}",
          color: "#ffffff",
          focusColor: "#ffffff"
        }
      },
      dark: {
        primary: {
          color: "{primary.50}",
          contrastColor: "{primary.950}",
          hoverColor: "{primary.100}",
          activeColor: "{primary.200}"
        },
        highlight: {
          background: "{primary.50}",
          focusBackground: "{primary.300}",
          color: "{primary.950}",
          focusColor: "{primary.950}"
        }
      }
    }
  }
});

export default Noir;
```

- Setup User Store

* Create Page 📝 [ user.js ] Inside Stores

```js
// Page [ script_youtube/script_youtube_vue/src/stores/user.js ]
import { defineStore } from "pinia";
import axios from "axios";
export const useUserStore = defineStore({
  id: "user",
  state: () => ({
    user: {
      isAuthenticated: false,
      id: null,
      name: null,
      surname: null,
      email: null,
      date_of_birth: null,
      access: null,
      refresh: null
    }
  }),
  actions: {
    initStore() {
      if (localStorage.getItem("user.access")) {
        console.log("User has access!");
        this.user.isAuthenticated = true;
        this.user.id = localStorage.getItem("user.id");
        this.user.name = localStorage.getItem("user.name");
        this.user.surname = localStorage.getItem("user.surname");
        this.user.email = localStorage.getItem("user.email");
        this.user.date_of_birth = localStorage.getItem("user.date_of_birth");
        this.user.access = localStorage.getItem("user.access");
        this.user.refresh = localStorage.getItem("user.refresh");
        this.refreshToken();
      }
    },
    setToken(data) {
      console.log("setToken", data);
      this.user.access = data.access;
      this.user.refresh = data.refresh;
      this.user.isAuthenticated = true;
      localStorage.setItem("user.access", data.access);
      localStorage.setItem("user.refresh", data.refresh);

      console.log("user.access: ", localStorage.getItem("user.access"));
    },
    removeToken() {
      console.log("removeToken");
      this.user.refresh = null;
      this.user.access = null;
      this.user.isAuthenticated = false;
      this.user.id = null;
      this.user.name = null;
      this.user.surname = null;
      this.user.email = null;
      this.user.date_of_birth = null;
      localStorage.setItem("user.access", "");
      localStorage.setItem("user.refresh", "");
      localStorage.setItem("user.id", "");
      localStorage.setItem("user.name", "");
      localStorage.setItem("user.surname", "");
      localStorage.setItem("user.email", "");
      localStorage.setItem("user.date_of_birth", "");
    },
    setUserInfo(user) {
      console.log("setUserInfo", user);
      this.user.id = user.id;
      this.user.name = user.name;
      this.user.surname = user.surname;
      this.user.email = user.email;
      this.user.date_of_birth = user.date_of_birth;
      localStorage.setItem("user.id", this.user.id);
      localStorage.setItem("user.name", this.user.name);
      localStorage.setItem("user.surname", this.user.surname);
      localStorage.setItem("user.email", this.user.email);
      localStorage.setItem("user.date_of_birth", this.user.date_of_birth);
    },
    refreshToken() {
      axios
        .post("/api/refresh/", {
          refresh: this.user.refresh
        })
        .then((response) => {
          this.user.access = response.data.access;
          localStorage.setItem("user.access", response.data.access);
          axios.defaults.headers.common["Authorization"] =
            "Bearer " + response.data.access;
        })
        .catch((error) => {
          console.log(error);
          this.removeToken();
        });
    }
  }
});
```

- Create Page 📝 [ Authentication/Login.vue ] Inside views

```text
Authentication/Login.vue
```

```html

```

```js

```

- Create Page 📝 [ Account/Profile.vue ] Inside views

```text
Account/Profile.vue
```

```html

```

```js

```

- Edite Page 📝 [ App.vue ]

```js
<script setup>
import { RouterLink, RouterView } from 'vue-router'
import axios from 'axios'

import { ref } from 'vue'
//
import { onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'

const userStore = useUserStore()
userStore.initStore()
const router = useRouter()

onMounted(() => {
  // Perform any necessary operations on component mount
  if (!userStore.user.access) {
    console.log('User Data: ', userStore.user.access)
    // Replace '/login' with your actual login route
    router.push('/login')
  } else {
    // Set default Authorization header for axios
    axios.defaults.headers.common['Authorization'] = `Bearer ${userStore.user.access}`
    // console.log('User Data: ', userStore.user)
  }
})

// For Toggle Theme
const op = ref(null)
const toggle = (event) => {
  op.value.toggle(event)
}
// Log Out
let logout = () => {
  console.log('User Log out')
  userStore.removeToken()
  setTimeout(() => {
    router.push('/login').then(() => {})
  }, 10)
}
</script>
```

```html
<template>
  <!-- Header -->
  <!-- v-if="userStore.user.isAuthenticated" -->
  <prime_card class="header_wrapper">
    <template #content>
      <header class="card shadow-md fixed top-0 left-0 right-0 h-16 px-2">
        <div class="container mx-auto flex justify-between items-center h-full">
          <!-- Left Section (Logo and Search Bar) -->
          <div
            class="header_left_section flex items-center space-x-1 basis-1/4"
          >
            <!-- Logo -->
            <RouterLink to="/" class="logo flex">
              <fa
                :icon="['fab', 'facebook']"
                class="text-5xl text-indigo-700"
              />
            </RouterLink>
            <!-- Search Bar -->
            <div class="search_bar w-full flex">
              <prime_icon_field>
                <prime_input_icon class="pi pi-search" />
                <prime_input_text
                  v-model="value1"
                  placeholder="Search Script Youtube"
                />
              </prime_icon_field>

              <!--               
              <span class="icon">
                <fa :icon="['fas', 'search']" />
              </span>
              <input
                type="text"
                class="w-full p-2 rounded-full focus:outline-none"
                placeholder="Search Facebook"
              /> -->
            </div>
          </div>
          <!-- Center Section (Navigation Icons) -->
          <div
            class="header_center_section flex items-center justify-center space-x-1 basis-1/2"
          >
            <RouterLink to="/" class="header_center_section_link_home grow">
              <span class="header_center_section_link_home_span">
                <svg
                  viewBox="0 0 24 24"
                  width="24"
                  height="24"
                  fill="currentColor"
                  class="header_center_section_link_home_svg"
                >
                  <path
                    d="M9.464 1.286C10.294.803 11.092.5 12 .5c.908 0 1.707.303 2.537.786.795.462 1.7 1.142 2.815 1.977l2.232 1.675c1.391 1.042 2.359 1.766 2.888 2.826.53 1.059.53 2.268.528 4.006v4.3c0 1.355 0 2.471-.119 3.355-.124.928-.396 1.747-1.052 2.403-.657.657-1.476.928-2.404 1.053-.884.119-2 .119-3.354.119H7.93c-1.354 0-2.471 0-3.355-.119-.928-.125-1.747-.396-2.403-1.053-.656-.656-.928-1.475-1.053-2.403C1 18.541 1 17.425 1 16.07v-4.3c0-1.738-.002-2.947.528-4.006.53-1.06 1.497-1.784 2.888-2.826L6.65 3.263c1.114-.835 2.02-1.515 2.815-1.977zM10.5 13A1.5 1.5 0 0 0 9 14.5V21h6v-6.5a1.5 1.5 0 0 0-1.5-1.5h-3z"
                  ></path>
                </svg>
              </span>
            </RouterLink>
            <RouterLinka
              to="/"
              class="text-xl grow header_center_section_link_friends"
            >
              <span class="header_center_section_link_friends_span">
                <svg
                  viewBox="0 0 24 24"
                  width="24"
                  height="24"
                  fill="currentColor"
                  class="header_center_section_link_friends_svg"
                >
                  <path
                    d="M12.496 5a4 4 0 1 1 8 0 4 4 0 0 1-8 0zm4-2a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm-9 2.5a4 4 0 1 0 0 8 4 4 0 0 0 0-8zm-2 4a2 2 0 1 1 4 0 2 2 0 0 1-4 0zM5.5 15a5 5 0 0 0-5 5 3 3 0 0 0 3 3h8.006a3 3 0 0 0 3-3 5 5 0 0 0-5-5H5.5zm-3 5a3 3 0 0 1 3-3h4.006a3 3 0 0 1 3 3 1 1 0 0 1-1 1H3.5a1 1 0 0 1-1-1zm12-9.5a5.04 5.04 0 0 0-.37.014 1 1 0 0 0 .146 1.994c.074-.005.149-.008.224-.008h4.006a3 3 0 0 1 3 3 1 1 0 0 1-1 1h-3.398a1 1 0 1 0 0 2h3.398a3 3 0 0 0 3-3 5 5 0 0 0-5-5H14.5z"
                  ></path>
                </svg>
              </span>
            </RouterLinka>
            <RouterLink
              to="/"
              class="text-xl grow header_center_section_link_videos"
            >
              <span class="header_center_section_link_videos_span">
                <svg
                  viewBox="0 0 24 24"
                  width="24"
                  height="24"
                  fill="currentColor"
                  class="header_center_section_link_videos_svg"
                >
                  <path
                    d="M10.996 8.132A1 1 0 0 0 9.5 9v4a1 1 0 0 0 1.496.868l3.5-2a1 1 0 0 0 0-1.736l-3.5-2z"
                  ></path>
                  <path
                    d="M14.573 2H9.427c-1.824 0-3.293 0-4.45.155-1.2.162-2.21.507-3.013 1.31C1.162 4.266.817 5.277.655 6.477.5 7.634.5 9.103.5 10.927v.146c0 1.824 0 3.293.155 4.45.162 1.2.507 2.21 1.31 3.012.802.803 1.813 1.148 3.013 1.31C6.134 20 7.603 20 9.427 20h5.146c1.824 0 3.293 0 4.45-.155 1.2-.162 2.21-.507 3.012-1.31.803-.802 1.148-1.813 1.31-3.013.155-1.156.155-2.625.155-4.449v-.146c0-1.824 0-3.293-.155-4.45-.162-1.2-.507-2.21-1.31-3.013-.802-.802-1.813-1.147-3.013-1.309C17.866 2 16.397 2 14.573 2zM3.38 4.879c.369-.37.887-.61 1.865-.741C6.251 4.002 7.586 4 9.5 4h5c1.914 0 3.249.002 4.256.138.978.131 1.496.372 1.865.74.37.37.61.888.742 1.866.135 1.007.137 2.342.137 4.256 0 1.914-.002 3.249-.137 4.256-.132.978-.373 1.496-.742 1.865-.369.37-.887.61-1.865.742-1.007.135-2.342.137-4.256.137h-5c-1.914 0-3.249-.002-4.256-.137-.978-.132-1.496-.373-1.865-.742-.37-.369-.61-.887-.741-1.865C2.502 14.249 2.5 12.914 2.5 11c0-1.914.002-3.249.138-4.256.131-.978.372-1.496.74-1.865zM8 21.5a1 1 0 1 0 0 2h8a1 1 0 1 0 0-2H8z"
                  ></path>
                </svg>
              </span>
            </RouterLink>
            <RouterLink
              to="/"
              class="text-xl grow header_center_section_link_marketplace"
            >
              <span class="header_center_section_link_marketplace_span">
                <svg
                  viewBox="0 0 24 24"
                  width="24"
                  height="24"
                  fill="currentColor"
                  class="header_center_section_link_marketplace_svg"
                >
                  <path
                    d="M1.588 3.227A3.125 3.125 0 0 1 4.58 1h14.84c1.38 0 2.597.905 2.993 2.227l.816 2.719a6.47 6.47 0 0 1 .272 1.854A5.183 5.183 0 0 1 22 11.455v4.615c0 1.355 0 2.471-.119 3.355-.125.928-.396 1.747-1.053 2.403-.656.657-1.475.928-2.403 1.053-.884.12-2 .119-3.354.119H8.929c-1.354 0-2.47 0-3.354-.119-.928-.125-1.747-.396-2.403-1.053-.657-.656-.929-1.475-1.053-2.403-.12-.884-.119-2-.119-3.354V11.5l.001-.045A5.184 5.184 0 0 1 .5 7.8c0-.628.092-1.252.272-1.854l.816-2.719zM10 21h4v-3.5a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5V21zm6-.002c.918-.005 1.608-.025 2.159-.099.706-.095 1.033-.262 1.255-.485.223-.222.39-.55.485-1.255.099-.735.101-1.716.101-3.159v-3.284a5.195 5.195 0 0 1-1.7.284 5.18 5.18 0 0 1-3.15-1.062A5.18 5.18 0 0 1 12 13a5.18 5.18 0 0 1-3.15-1.062A5.18 5.18 0 0 1 5.7 13a5.2 5.2 0 0 1-1.7-.284V16c0 1.442.002 2.424.1 3.159.096.706.263 1.033.486 1.255.222.223.55.39 1.255.485.551.074 1.24.094 2.159.1V17.5a2.5 2.5 0 0 1 2.5-2.5h3a2.5 2.5 0 0 1 2.5 2.5v3.498zM4.581 3c-.497 0-.935.326-1.078.802l-.815 2.72A4.45 4.45 0 0 0 2.5 7.8a3.2 3.2 0 0 0 5.6 2.117 1 1 0 0 1 1.5 0A3.19 3.19 0 0 0 12 11a3.19 3.19 0 0 0 2.4-1.083 1 1 0 0 1 1.5 0A3.2 3.2 0 0 0 21.5 7.8c0-.434-.063-.865-.188-1.28l-.816-2.72A1.125 1.125 0 0 0 19.42 3H4.58z"
                  ></path>
                </svg>
              </span>
            </RouterLink>
            <RouterLink
              to="/"
              class="text-xl grow header_center_section_link_groups"
            >
              <span class="header_center_section_link_groups_span">
                <svg
                  viewBox="0 0 24 24"
                  width="24"
                  height="24"
                  fill="currentColor"
                  class="header_center_section_link_groups_svg"
                >
                  <path
                    d="M12 5a4 4 0 1 0 0 8 4 4 0 0 0 0-8zm-2 4a2 2 0 1 1 4 0 2 2 0 0 1-4 0z"
                  ></path>
                  <path
                    d="M12 .5C5.649.5.5 5.649.5 12S5.649 23.5 12 23.5 23.5 18.351 23.5 12 18.351.5 12 .5zM2.5 12c0-.682.072-1.348.209-1.99a2 2 0 0 1 0 3.98A9.539 9.539 0 0 1 2.5 12zm4 0a4.001 4.001 0 0 0-3.16-3.912A9.502 9.502 0 0 1 12 2.5a9.502 9.502 0 0 1 8.66 5.588 4.001 4.001 0 0 0 0 7.824 9.514 9.514 0 0 1-1.755 2.613A5.002 5.002 0 0 0 14 14.5h-4a5.002 5.002 0 0 0-4.905 4.025 9.515 9.515 0 0 1-1.755-2.613A4.001 4.001 0 0 0 6.5 12zm13 0a2 2 0 0 1 1.791-1.99 9.538 9.538 0 0 1 0 3.98A2 2 0 0 1 19.5 12zm-2.51 8.086A9.455 9.455 0 0 1 12 21.5c-1.83 0-3.54-.517-4.99-1.414a1.004 1.004 0 0 1-.01-.148V19.5a3 3 0 0 1 3-3h4a3 3 0 0 1 3 3v.438a1 1 0 0 1-.01.148z"
                  ></path>
                </svg>
              </span>
            </RouterLink>
          </div>
          <!--  -->
          <div class="toggle_header_left_section">
            <span class="icon"> <i class="fas fa-bars"></i> </span>
          </div>
          <!-- Right Section (Profile and Notifications) -->
          <div
            class="header_right_section flex items-center justify-end space-x-1 basis-1/4"
          >
            <RouterLinka
              to="/"
              class="header_right_section_link bg-gray-300 p-3 rounded-full"
            >
              <span class="header_right_section_link_span">
                <svg
                  viewBox="0 0 24 24"
                  width="20"
                  height="20"
                  fill="currentColor"
                  class="header_right_section_link_svg"
                >
                  <path
                    d="M18.5 1A1.5 1.5 0 0 0 17 2.5v3A1.5 1.5 0 0 0 18.5 7h3A1.5 1.5 0 0 0 23 5.5v-3A1.5 1.5 0 0 0 21.5 1h-3zm0 8a1.5 1.5 0 0 0-1.5 1.5v3a1.5 1.5 0 0 0 1.5 1.5h3a1.5 1.5 0 0 0 1.5-1.5v-3A1.5 1.5 0 0 0 21.5 9h-3zm-16 8A1.5 1.5 0 0 0 1 18.5v3A1.5 1.5 0 0 0 2.5 23h3A1.5 1.5 0 0 0 7 21.5v-3A1.5 1.5 0 0 0 5.5 17h-3zm8 0A1.5 1.5 0 0 0 9 18.5v3a1.5 1.5 0 0 0 1.5 1.5h3a1.5 1.5 0 0 0 1.5-1.5v-3a1.5 1.5 0 0 0-1.5-1.5h-3zm8 0a1.5 1.5 0 0 0-1.5 1.5v3a1.5 1.5 0 0 0 1.5 1.5h3a1.5 1.5 0 0 0 1.5-1.5v-3a1.5 1.5 0 0 0-1.5-1.5h-3zm-16-8A1.5 1.5 0 0 0 1 10.5v3A1.5 1.5 0 0 0 2.5 15h3A1.5 1.5 0 0 0 7 13.5v-3A1.5 1.5 0 0 0 5.5 9h-3zm0-8A1.5 1.5 0 0 0 1 2.5v3A1.5 1.5 0 0 0 2.5 7h3A1.5 1.5 0 0 0 7 5.5v-3A1.5 1.5 0 0 0 5.5 1h-3zm8 0A1.5 1.5 0 0 0 9 2.5v3A1.5 1.5 0 0 0 10.5 7h3A1.5 1.5 0 0 0 15 5.5v-3A1.5 1.5 0 0 0 13.5 1h-3zm0 8A1.5 1.5 0 0 0 9 10.5v3a1.5 1.5 0 0 0 1.5 1.5h3a1.5 1.5 0 0 0 1.5-1.5v-3A1.5 1.5 0 0 0 13.5 9h-3z"
                  ></path>
                </svg>
              </span>
            </RouterLinka>
            <RouterLinka
              to="/"
              class="header_right_section_link bg-gray-300 p-3 rounded-full"
            >
              <span class="header_right_section_link_span">
                <svg
                  viewBox="0 0 12 13"
                  width="20"
                  height="20"
                  fill="currentColor"
                  class="header_right_section_link_svg"
                >
                  <g fill-rule="evenodd" transform="translate(-450 -1073)">
                    <path
                      d="m459.603 1077.948-1.762 2.851a.89.89 0 0 1-1.302.245l-1.402-1.072a.354.354 0 0 0-.433.001l-1.893 1.465c-.253.196-.583-.112-.414-.386l1.763-2.851a.89.89 0 0 1 1.301-.245l1.402 1.072a.354.354 0 0 0 .434-.001l1.893-1.465c.253-.196.582.112.413.386M456 1073.5c-3.38 0-6 2.476-6 5.82 0 1.75.717 3.26 1.884 4.305.099.087.158.21.162.342l.032 1.067a.48.48 0 0 0 .674.425l1.191-.526a.473.473 0 0 1 .32-.024c.548.151 1.13.231 1.737.231 3.38 0 6-2.476 6-5.82 0-3.344-2.62-5.82-6-5.82"
                    ></path>
                  </g>
                </svg>
              </span>
            </RouterLinka>
            <RouterLink
              to="/"
              class="header_right_section_link bg-gray-300 p-3 rounded-full"
            >
              <span class="header_right_section_link_span">
                <svg
                  viewBox="0 0 24 24"
                  width="20"
                  height="20"
                  fill="currentColor"
                  class="header_right_section_link_svg"
                >
                  <path
                    d="M3 9.5a9 9 0 1 1 18 0v2.927c0 1.69.475 3.345 1.37 4.778a1.5 1.5 0 0 1-1.272 2.295h-4.625a4.5 4.5 0 0 1-8.946 0H2.902a1.5 1.5 0 0 1-1.272-2.295A9.01 9.01 0 0 0 3 12.43V9.5zm6.55 10a2.5 2.5 0 0 0 4.9 0h-4.9z"
                  ></path>
                </svg>
              </span>
            </RouterLink>
            <!-- Avatar -->
            <prime_avatar
              image="https://learncodingeasy.github.io/Images/images/user/user.png"
              size="large"
              shape="circle"
              alt="Profile Picture"
              class="w-10 h-10 rounded-full"
              @click="toggle"
              type="button"
              aria-haspopup="true"
              aria-controls="overlay_tmenu"
            />
            <!-- Popup User Option -->
            <prime_popover ref="op">
              <div class="w-[25rem]">
                <!-- User Profile -->
                <div class="div_wrapper_profile">
                  <RouterLink
                    class="flex align-middle"
                    v-if="userStore.user.id"
                    :to="{ name: 'profile', params: { id: userStore.user.id } }"
                  >
                    <span class="user_img">
                      <!-- v-if="userStore.user.avatar" -->
                      <img
                        v-if="userStore.user.avatar"
                        :src="userStore.user.avatar"
                        class="rounded-full"
                        alt=""
                      />
                      <!-- v-else  -->
                      <img
                        v-else
                        src="https://learncodingeasy.github.io/Images/images/user/user.png"
                        class="rounded-full"
                        alt=""
                      />
                    </span>
                    <span class="user_name">{{ userStore.user.name }}</span>
                  </RouterLink>
                </div>
                <!-- Log Out -->
                <div
                  class="div_wrapper_logout flex items-start py-3 align-middle cursor-pointer"
                  @click="logout"
                >
                  <div class="icon_logout flex justify-center items-start">
                    <i
                      class="pi pi-sign-out"
                      style="font-size: 1rem"
                      shape="circle"
                    ></i>
                  </div>
                  <button class="font-bold py-3">Log out</button>
                </div>
                <!-- Toggle Theme -->
                <div class="flex div_wrapper_toggle_theme cursor-pointer">
                  <ThemeSwitcher />
                  <span class="font-medium mb-2">Toggle theme</span>
                </div>
              </div>
            </prime_popover>
          </div>
        </div>
      </header>
    </template>
  </prime_card>

  <prime_toast />

  <RouterView />
</template>
```

---

---

---

---

---

---

---

---

---

---

---

---

## Django

### Start Create App Script

```cmd
python manage.py startapp script
```

Add To Apps Inside [ settings.py ]

```python
INSTALLED_APPS = [
    # Apps
    "script",
    # Libraries
]
```

Edite Page 📝 [ models.py ] Inside App Script

```python
# Page [ script_youtube/script_youtube_django/script/models.py ]

import uuid
from django.utils.timesince import timesince
from django.conf import settings
from django.db import models
from account.models import User


class ScriptAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="script_attachments")
    created_by = models.ForeignKey(
        User, related_name="script_attachments", on_delete=models.CASCADE
    )

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return ""


class ScriptVideo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video = models.FileField(upload_to="Script_videos")
    created_by = models.ForeignKey(
        User, related_name="script_videos", on_delete=models.CASCADE
    )

    def get_video(self):
        if self.video:
            return settings.WEBSITE_URL + self.video.url
        else:
            return ""


class Script(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TASKS = "Tasks"
    DONE = "Done"
    IN_MAKING = "In Making"
    scriptStatusList = [
        ("TASKS", "Tasks"),
        ("DONE", "Done"),
        ("IN_MAKING", "In Making"),
    ]
    #
    script_status = models.CharField(
        max_length=50, choices=scriptStatusList, default=TASKS, blank=True
    )
    # Boolean
    is_private = models.BooleanField(default=False)
    title = models.TextField(blank=True, null=True)
    list_of_sources_urls = models.JSONField(default=list, blank=True, null=True)
    list_of_shots = models.JSONField(default=list, blank=True, null=True)
    list_of_examples = models.JSONField(default=list, blank=True, null=True)
    list_of_paragraphs = models.JSONField(default=list, blank=True, null=True)
    list_of_fonts_urls = models.JSONField(default=list, blank=True, null=True)
    list_of_colors = models.JSONField(default=list, blank=True, null=True)
    list_of_musics = models.JSONField(default=list, blank=True, null=True)
    list_of_videos_background = models.JSONField(default=list, blank=True, null=True)
    list_of_images = models.JSONField(default=list, blank=True, null=True)
    list_of_icons = models.JSONField(default=list, blank=True, null=True)
    list_of_visual_effects = models.JSONField(default=list, blank=True, null=True)
    list_of_transitions = models.JSONField(default=list, blank=True, null=True)
    list_of_sound_effects = models.JSONField(default=list, blank=True, null=True)
    script = models.TextField(blank=True, null=True)
    # 🖼️ Image
    attachments = models.ManyToManyField(ScriptAttachment, blank=True)
    # 🎥 Video
    videos = models.ManyToManyField(ScriptVideo, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="scripts", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("-created_at",)

    def created_at_formatted(self):
        return timesince(self.created_at)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return

```

Edite Page 📝 [ admin.py ] Inside App Script

```python

```

Edite Page 📝 [ serializers.py ] Inside App Script

```python

```

Create Page 📝 [ forms.py ] Inside App Script

```python

```

Create Page 📝 [ api.py ] Inside App Script

```python

```

Create Page 📝 [ urls.py ] Inside App Script

```python

```

---

---

---

---

---

---

---

## Django

### Start Create App Task

```cmd
python manage.py startapp task
```

Add To Apps Inside [ settings.py ]

```python
INSTALLED_APPS = [
    # Apps
    "task",
    # Libraries
]
```

Edite Page 📝 [ models.py ] Inside App Script

```python

```

Edite Page 📝 [ admin.py ] Inside App Script

```python

```

Edite Page 📝 [ serializers.py ] Inside App Script

```python

```

Create Page 📝 [ forms.py ] Inside App Script

```python

```

Create Page 📝 [ api.py ] Inside App Script

```python

```

Create Page 📝 [ urls.py ] Inside App Script

```python

```
