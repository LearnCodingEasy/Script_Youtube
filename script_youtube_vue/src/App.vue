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
  // توجيه المستخدم إلى صفحة تسجيل الدخول
  setTimeout(() => {
    router.push('/login').then(() => {})
  }, 10)
}
</script>

<template>
  <div class="">
    <!-- Header -->
    <div class="wrapper_header">
      <prime_card
        class="header_wrapper"
        v-if="userStore.user.isAuthenticated"
        style="box-shadow: none !important; height: 60px"
      >
        <template #content>
          <header class="card shadow-md fixed top-0 left-0 right-0 h-16 px-2">
            <div class="container mx-auto flex justify-between items-center h-full">
              <!-- Left Section (Logo and Search Bar) -->
              <div class="header_left_section flex items-center space-x-1 basis-1/4">
                <!-- Logo -->
                <RouterLink to="/" class="logo flex">
                  <fa :icon="['fab', 'youtube']" class="text-5xl text-red-600" />
                </RouterLink>
                <!-- Search Bar -->
                <div class="search_bar w-full flex">
                  <prime_icon_field>
                    <prime_input_icon class="pi pi-search" />
                    <prime_input_text v-model="value1" placeholder="Search Script Youtube" />
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
                <RouterLinka to="/" class="text-xl grow header_center_section_link_friends">
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
                <!-- Add -->
                <RouterLink
                  to="/ScriptCreate"
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
                <!-- Add -->
                <RouterLink to="/ScriptList" class="text-xl grow header_center_section_link_videos">
                  <span class="header_center_section_link_videos_span">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 640 512"
                      width="24"
                      height="24"
                      fill="currentColor"
                      class="header_center_section_link_videos_svg"
                    >
                      <path
                        d="M48 0C21.5 0 0 21.5 0 48v64c0 8.8 7.2 16 16 16h80V48C96 21.5 74.5 0 48 0zm208 412.6V352h288V96c0-52.9-43.1-96-96-96H111.6C121.7 13.4 128 29.9 128 48v368c0 38.9 34.7 69.7 74.8 63.1C234.2 474 256 444.5 256 412.6zM288 384v32c0 52.9-43.1 96-96 96h336c61.9 0 112-50.1 112-112 0-8.8-7.2-16-16-16H288z"
                      />
                    </svg>
                  </span>
                </RouterLink>
                <RouterLink to="/" class="text-xl grow header_center_section_link_marketplace">
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
                <RouterLink to="/" class="text-xl grow header_center_section_link_groups">
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
              <div class="header_right_section flex items-center justify-end space-x-1 basis-1/4">
                <RouterLinka to="/" class="header_right_section_link bg-gray-300 p-3 rounded-full">
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
                <RouterLinka to="/" class="header_right_section_link bg-gray-300 p-3 rounded-full">
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
                <RouterLink to="/" class="header_right_section_link bg-gray-300 p-3 rounded-full">
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
                        <i class="pi pi-sign-out" style="font-size: 1rem" shape="circle"></i>
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
    </div>

    <prime_toast />

    <RouterView />
  </div>
</template>

<style lang="scss">
body {
  min-height: 10000px;
}
.header_right_section {
  a,
  routerlinka {
    margin: 0 0.5rem;
  }
}
</style>
