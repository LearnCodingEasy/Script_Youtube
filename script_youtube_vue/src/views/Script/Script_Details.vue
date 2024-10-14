<template>
  <div class="">
    <div class="container mx-auto">
      <div class="wrapper_script_details mt-10">
        <div class="inner_script_details">
          <div class="script_image" v-if="script.attachments">
            <img :src="script.attachments[0].get_image" />
          </div>
          <div class="script_title">
            <h2 v-html="script.title"></h2>
          </div>
          <div class="script_title"></div>
          <div class="script_title"></div>
          <div class="script_title"></div>
          <div class="script_title"></div>
          <div class="script_title"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Script_Details',

  data() {
    return {
      script: {
        id: null
      }
    }
  },

  mounted() {
    this.getScript()
  },

  methods: {
    getScript() {
      axios
        .get(`/api/scripts/script_list/script_detail/${this.$route.params.id}/`)
        .then((response) => {
          console.log('data', response.data)

          this.script = response.data.script
        })
        .catch((error) => {
          console.log('error', error)
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
</script>
