<script setup>
import { RouterLink } from 'vue-router'

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
</script>

<template>
  <div class="Component-Name mt-12">
    <div class="container mx-auto">
      <div class="wrapper_scripts_list px-5">
        <div class="grid grid-cols-3 md:grid-cols-3 lg:grid-cols-4 gap-7">
          <div
            class="basis-1/4 md:basis-full sm:basis-11/12 shadow-sm hover:shadow-lg"
            v-for="script in scripts"
            v-bind:key="script.id"
          >
            <prime_card>
              <template #title>
                <div class="image rounded-lg overflow-hidden">
                  <prime_image
                    :src="script.attachments[0].get_image"
                    alt="Image"
                    width="100%"
                    preview
                    class="rounded-lg"
                    style="height: 299px; max-height: 300px !important; width: 100%"
                    v-if="script.attachments.length > 0"
                  />
                </div>
              </template>
              <template #content>
                <h2 class="text-3xl mb-4 mt-2" dir="auto" v-html="script.title"></h2>
                <!-- <div class="hidden hover:block"> -->
                <div class="" v-if="userStore.user.id == script.created_by.id">
                  <prime_button
                    @click="deleteScript(script.id)"
                    severity="danger"
                    icon="pi pi-trash"
                    iconPos="right"
                  ></prime_button>
                </div>
              </template>
              <template #footer>
                <div class="flex justify-between items-center">
                  <RouterLink :to="{ name: 'ScriptDetails', params: { id: script.id } }">
                    <prime_button
                      class="text-lg py-1 px-5 capitalize"
                      icon="pi pi-eye"
                      aria-label="go"
                      iconPos="right"
                    >
                    </prime_button>
                  </RouterLink>

                  <prime_button
                    class="text-lg py-1 px-5 capitalize block"
                    icon="pi pi-pencil"
                    aria-label="Edit"
                    iconPos="right"
                    @click="$router.push({ name: 'ScriptEdit', params: { id: script.id } })"
                    v-if="userStore.user.id == script.created_by.id"
                  >
                  </prime_button>
                </div>
              </template>
            </prime_card>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ScriptList',
  setup() {
    return {}
  },
  data() {
    return {
      scripts: [],
      // ضع معرف الـ Script المراد حذفه
      scriptId: 'your-script-uuid-here',
      errors: []
    }
  },
  async mounted() {
    await this.gatAllScripts()
  },
  methods: {
    gatAllScripts() {
      axios
        .get('/api/scripts/script_list')
        .then((response) => {
          this.scripts = response.data
          console.log('response.data: ', response.data)
          console.log('this.scripts: ', this.scripts)
        })
        .catch((error) => {
          console.log('error', error)
          this.$toast.add({
            severity: 'error',
            summary: 'Script List Error',
            detail: `Your Error Message Is${error.message}`,
            life: 10000
          })
        })
    },
    deleteScript(scriptId) {
      // تأكيد عملية الحذف من المستخدم
      if (confirm('Are you sure you want to delete this script?')) {
        axios
          .delete(`/api/scripts/script_list/script_delete/${scriptId}/`)
          .then((response) => {
            if (response.data.message == `script deleted`) {
              console.log(response.data)
              console.log('scriptId: ', scriptId)
              this.$toast.add({
                severity: 'error',
                summary: 'Script Deleted',
                detail: 'Script Youtube Deleted.',
                life: 3000
              })
              this.scripts = this.scripts.filter((script) => script.id !== scriptId)
            }
          })
          .catch((error) => {
            console.error('Error deleting script:', error)

            this.$toast.add({
              severity: 'error',
              summary: 'Script List Error',
              detail: `Your Error ${error}`,
              life: 3000
            })
          })
      }
    }
  }
}
</script>

<style lang="scss" scoped></style>
