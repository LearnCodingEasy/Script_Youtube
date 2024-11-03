<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-left col-span-1">
      <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
        <img :src="user.get_avatar" class="mb-6 rounded-full" />

        <p>
          <strong>{{ user.name }}</strong>
        </p>

        <div class="mt-6 flex space-x-8 justify-around" v-if="user.id">
          <!-- <RouterLink
            :to="{ name: 'friends', params: { id: user.id } }"
            class="text-xs text-gray-500"
            >{{ user.friends_count }} friends</RouterLink
          > -->
          <p class="text-xs text-gray-500">{{ user.script_count }} scripts</p>
        </div>

        <div class="mt-6">
          <button
            class="inline-block py-4 px-3 bg-purple-600 text-xs text-white rounded-lg"
            @click="sendFriendshipRequest"
            v-if="userStore.user.id !== user.id && can_send_friendship_request"
          >
            Send friendship request
          </button>

          <button
            class="inline-block mt-4 py-4 px-3 bg-purple-600 text-xs text-white rounded-lg"
            @click="sendDirectMessage"
            v-if="userStore.user.id !== user.id"
          >
            Send direct message
          </button>

          <button
            class="inline-block py-4 px-3 bg-red-600 text-xs text-white rounded-lg"
            @click="logout"
            v-if="userStore.user.id === user.id"
          >
            Log out
          </button>
        </div>
      </div>
    </div>

    <div class="main-center col-span-2 space-y-4">
      <div
        class="bg-white border border-gray-200 rounded-lg"
        v-if="userStore.user.id === user.id"
      ></div>
    </div>

    <div class="main-right col-span-1 space-y-4">
      <Trends />
    </div>
  </div>
</template>

<style>
input[type='file'] {
  display: none;
}

.custom-file-upload {
  border: 1px solid #ccc;
  display: inline-block;
  padding: 6px 12px;
  cursor: pointer;
}
</style>

<script>
import axios from 'axios'

import { useUserStore } from '@/stores/user'

export default {
  name: 'FeedView',

  setup() {
    const userStore = useUserStore()

    return {
      userStore
    }
  },

  components: {},

  data() {
    return {
      scripts: [],
      user: {
        id: ''
      },
      can_send_friendship_request: null
    }
  },

  mounted() {
    this.getScript()
  },

  watch: {
    '$route.params.id': {
      handler: function () {
        this.getScript()
      },
      deep: true,
      immediate: true
    }
  },

  methods: {
    // deletePost(id) {
    //   this.scripts = this.scripts.filter((post) => post.id !== id)
    // },

    sendDirectMessage() {
      console.log('sendDirectMessage')

      axios
        .get(`/api/chat/${this.$route.params.id}/get-or-create/`)
        .then((response) => {
          console.log(response.data)

          this.$router.push('/chat')
        })
        .catch((error) => {
          console.log('error', error)
        })
    },

    sendFriendshipRequest() {
      axios
        .post(`/api/friends/${this.$route.params.id}/request/`)
        .then((response) => {
          console.log('data', response.data)

          this.can_send_friendship_request = false

          if (response.data.message == 'request already sent') {
            this.toastStore.showToast(5000, 'The request has already been sent!', 'bg-red-300')
          } else {
            this.toastStore.showToast(5000, 'The request was sent!', 'bg-emerald-300')
          }
        })
        .catch((error) => {
          console.log('error', error)
        })
    },

    getScript() {
      axios
        .get(`/api/scripts/script_list/${this.$route.params.id}/`)
        .then((response) => {
          console.log('data script', response.data)

          this.script = response.data.script
          this.user = response.data.user
          this.can_send_friendship_request = response.data.can_send_friendship_request
        })
        .catch((error) => {
          console.log('error', error)
        })
    },

    logout() {
      console.log('Log out')

      this.userStore.removeToken()

      this.$router.push('/login')
    }
  }
}
</script>
