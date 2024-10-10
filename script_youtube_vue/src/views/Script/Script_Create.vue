<template>
  <div class="Component-Name mt-8">
    <div class="container mx-auto">
      <div class="wrapper_form_create_script px-5">
        <form class="form_login" v-on:submit.prevent="submitAddScriptForm">
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-7">
            <!-- 1️⃣ title -->
            <div class="title">
              <div class="card">
                <prime_editor v-model="title" editorStyle="height: 50px" />
              </div>
            </div>
            <!-- 2️⃣ list of sources urls -->
            <div class="list_of_sources">
              <div v-for="(url, index) in list_of_sources_urls" :key="index">
                <prime_input_text
                  type="url"
                  v-model="list_of_sources_urls[index]"
                  placeholder="Enter URL"
                />
                <prime_button
                  @click="removeOneOfListOfSourcesUrls(index)"
                  severity="danger"
                  icon="pi pi-trash"
                  iconPos="right"
                  class="mx-3"
                ></prime_button>
                <prime_button
                  @click="addOneOfListOfSourcesUrls"
                  severity="success"
                  icon="pi pi-folder-plus"
                  iconPos="right"
                ></prime_button>
              </div>
            </div>
            <!-- 3️⃣ list of shots -->
            <div class="list_of_sources shadow-lg py-7 px-3">
              <h2 dir="auto">قائمة التصوير</h2>
              <div v-for="(item, index) in list_of_shots" :key="index" class="mb-5">
                <prime_input_text
                  type="text"
                  v-model="item.text"
                  placeholder="Font Name"
                  class="mb-5"
                >
                </prime_input_text>
                <prime_editor v-model="item.discription" editorStyle="height: 100px" />
                <!-- <prime_input_text
                  type="url"
                  v-model="item.discription"
                  placeholder="Shot Discription"
                /> -->
                <prime_button
                  @click="removeOneOfListOfShots(index)"
                  severity="danger"
                  icon="pi pi-trash"
                  iconPos="right"
                  class="mx-3"
                ></prime_button>
                <prime_button
                  @click="addOneOfListOfShots"
                  severity="success"
                  icon="pi pi-folder-plus"
                  iconPos="right"
                ></prime_button>
              </div>
            </div>
            <!-- 4️⃣ -->
            <!-- 6️⃣ list of fonts urls -->
            <div class="list_of_sources shadow-lg py-7 px-3">
              <h2 dir="auto">قائمةالخط</h2>
              <div v-for="(item, index) in list_of_fonts_urls" :key="index">
                <prime_input_text type="text" v-model="item.name" placeholder="Font Name">
                </prime_input_text>
                <prime_input_text type="url" v-model="item.url" placeholder="URL Fonts" />
                <prime_button
                  @click="removeOneOfListOfFontsUrls(index)"
                  severity="danger"
                  icon="pi pi-trash"
                  iconPos="right"
                  class="mx-3"
                ></prime_button>
                <prime_button
                  @click="addOneOfListOfFontsUrls"
                  severity="success"
                  icon="pi pi-folder-plus"
                  iconPos="right"
                ></prime_button>
              </div>
            </div>

            <div class="send">
              <prime_button
                @click="submitAddScriptForm"
                label="Submit"
                severity="success"
                icon="pi pi-send"
                iconPos="right"
              ></prime_button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
//

export default {
  name: 'Script_Create',
  // props: {
  //   user: Object,
  //   posts: Array
  // },
  setup() {
    return {}
  },
  data() {
    return {
      title: '',
      list_of_sources_urls: [''],
      list_of_shots: [{ text: '', discription: '' }],
      list_of_paragraphs: [{ text: '', discription: '', start: '', end: '' }],
      list_of_fonts_urls: [{ name: '', url: '' }],
      errors: []
    }
  },

  methods: {
    // Script
    submitAddScriptForm() {
      this.errors = []

      let formData = new FormData()
      // Title
      if (this.title == '') {
        this.$toast.add({
          severity: 'error',
          summary: 'Type Script Title',
          detail: 'Your Script Title is missing',
          life: 3000
        })
        this.errors.push('Type Script Title')
      } else if (this.title !== '') {
        formData.append('title', this.title)
      }
      // list of sources urls
      const validSourcesUrls = this.list_of_sources_urls.filter((url) => url !== '')
      if (validSourcesUrls.length > 0) {
        formData.append('list_of_sources_urls', JSON.stringify(validSourcesUrls))
      } else {
        this.errors.push('Type at least one valid Script URL')
        this.$toast.add({
          severity: 'error',
          summary: 'Type Script Url',
          detail: 'At least one valid Script URL is required',
          life: 3000
        })
      }
      // 2️⃣
      // 3️⃣
      // list of fonts urls
      const validFontsUrls = this.list_of_fonts_urls.filter((item) => item.url !== '')
      if (validFontsUrls.length > 0) {
        console.log('validFontsUrls: ', validFontsUrls)
        formData.append('list_of_fonts_urls', JSON.stringify(validFontsUrls))
      } else {
        this.errors.push('Type at least one valid Script URL')
        this.$toast.add({
          severity: 'error',
          summary: 'Font Url',
          detail: 'At least one valid Script Font URL is required',
          life: 3000
        })
      }
      // list of fonts urls
      const validShots = this.list_of_fonts_urls.filter((item) => item.text !== '')
      if (validShots.length > 0) {
        // console.log('validFontsUrls: ', validFontsUrls)
        formData.append('list_of_shots', JSON.stringify(validShots))
      } else {
        this.errors.push('Type at least one valid Script URL')
        this.$toast.add({
          severity: 'error',
          summary: 'List Shots',
          detail: 'At least one valid Script List Shots is required',
          life: 3000
        })
      }

      if (this.errors.length === 0) {
        axios
          .post('/api/scripts/script_create/', formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          })
          .then((response) => {
            console.log('Data Is Send To Django: ', response.data)
            this.$toast.add({
              severity: 'success',
              summary: 'Script Done',
              detail: 'Good Script Youtube Adding.',
              life: 3000
            })
            this.scripts.unshift(response.data)
            this.title = ''
            this.list_of_sources_urls = ['']
            this.list_of_fonts_urls = [{ name: '', url: '' }]

            if (this.user) {
              console.log('this.user: ', this.user)
              // this.user.posts_count += 1
            }
          })
          .catch((error) => {
            console.log('error', error)
          })
      }
    },
    addOneOfListOfSourcesUrls() {
      this.list_of_sources_urls.push('')
    },
    removeOneOfListOfSourcesUrls(index) {
      this.list_of_sources_urls.splice(index, 1)
    },
    addOneOfListOfFontsUrls() {
      this.list_of_fonts_urls.push({ name: '', url: '' })
    },
    removeOneOfListOfFontsUrls(index) {
      this.list_of_fonts_urls.splice(index, 1)
    },
    addOneOfListOfShots() {
      this.list_of_shots.push({ text: '', discription: '' })
    },
    removeOneOfListOfShots(index) {
      this.list_of_shots.splice(index, 1)
    }
  }
}
</script>
