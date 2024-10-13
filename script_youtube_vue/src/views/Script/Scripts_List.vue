<template>
  <div class="Component-Name mt-12">
    <div class="container mx-auto">
      <div class="wrapper_scripts_list px-5">
        <div class="grid grid-cols-3 md:grid-cols-3 lg:grid-cols-4 gap-7">
          <div
            class="basis-1/4 md:basis-full sm:basis-11/12"
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
                  />
                </div>
              </template>
              <template #content>
                <h2 class="text-3xl mb-4 mt-2" dir="auto" v-html="script.title"></h2>
                <!-- <div class="hidden hover:block"> -->
                <div class="">
                  <prime_button
                    @click="deleteScript(script.id)"
                    severity="danger"
                    icon="pi pi-trash"
                    iconPos="right"
                  ></prime_button>
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
        })
    },
    deleteScript(scriptId) {
      // تأكيد عملية الحذف من المستخدم
      if (confirm('Are you sure you want to delete this script?')) {
        axios
          .delete(`/api/scripts/${scriptId}/script_delete/`)
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
          })
      }
    }
  }
}
</script>

<style lang="scss" scoped></style>
