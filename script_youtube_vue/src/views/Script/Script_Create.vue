<template>
  <div class="Component-Name mt-8">
    <div class="container mx-auto">
      <div class="wrapper_form_create_script px-5">
        <form class="form_login" v-on:submit.prevent="submitAddScriptForm">
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-7">
            <!-- 1️⃣ title -->
            <div class="title border p-5 rounded shadow-lg">
              <h2 dir="auto" class="mb-5 text-2xl">موضوع الفيديو [ العنوان ]</h2>
              <div class="card">
                <prime_editor v-model="title" editorStyle="height: 50px" />
              </div>
            </div>
            <!-- 2️⃣ list of sources urls -->
            <div class="list_of_sources">
              <h2 dir="auto">قائمة المصادار</h2>
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
                <prime_editor v-model="item.description" editorStyle="height: 100px" />
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
            <!-- 4️⃣ list of examples -->
            <div class="list_of_sources shadow-lg py-7 px-3">
              <h2 dir="auto">قائمة الامثلة</h2>
              <div v-for="(item, index) in list_of_examples" :key="index" class="mb-5">
                <prime_input_text
                  type="text"
                  v-model="item.title"
                  placeholder="Examples Title"
                  class="mb-5"
                >
                </prime_input_text>
                <prime_input_text
                  type="text"
                  v-model="item.page"
                  placeholder="Examples Page Name"
                  class="mb-5"
                >
                </prime_input_text>
                <prime_input_text
                  type="text"
                  v-model="item.lang"
                  placeholder="Examples  Language"
                  class="mb-5"
                >
                </prime_input_text>
                <prime_editor v-model="item.code" editorStyle="height: 100px" />
                <prime_button
                  @click="removeOneOfListOfExamples(index)"
                  severity="danger"
                  icon="pi pi-trash"
                  iconPos="right"
                  class="mx-3"
                >
                </prime_button>
                <prime_button
                  @click="addOneOfListOfExamples"
                  severity="success"
                  icon="pi pi-folder-plus"
                  iconPos="right"
                ></prime_button>
              </div>
            </div>
            <!-- 5️⃣ list of Paragraphs -->
            <div class="list_of_sources shadow-lg py-7 px-3">
              <h2 dir="auto">قائمة الفقرات</h2>
              <div v-for="(item, index) in list_of_paragraphs" :key="index" class="mb-5">
                <prime_input_text
                  type="text"
                  v-model="item.text"
                  placeholder="Font Name"
                  class="mb-5"
                >
                </prime_input_text>
                <prime_editor v-model="item.description" editorStyle="height: 100px" />
                <prime_button
                  @click="removeOneOfListOfParagraphs(index)"
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
            <!-- 6️⃣ list of fonts urls -->
            <div class="list_of_sources shadow-lg py-7 px-3">
              <h2 dir="auto">قائمة الخط</h2>
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
            <!-- Send -->
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
      list_of_shots: [{ text: '', description: '' }],
      list_of_examples: [{ title: '', page: '', lang: '', code: '' }],
      list_of_paragraphs: [{ text: '', description: '', start: '', end: '' }],
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
      // 2️⃣ list of Shots
      const validShots = this.list_of_shots.filter((item) => item.text !== '')
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
      // 3️⃣ list of examples
      const validExamples = this.list_of_shots.filter((item) => item.text !== '')
      if (validExamples.length > 0) {
        // console.log('validFontsUrls: ', validFontsUrls)
        formData.append('list_of_examples', JSON.stringify(validExamples))
      } else {
        this.errors.push('Type at least one valid Examples Title')
        this.$toast.add({
          severity: 'error',
          summary: 'List Examples',
          detail: 'At least one valid Script List Examples is required',
          life: 3000
        })
      }
      // 4️⃣ list of paragraphs
      const validParagraphs = this.list_of_paragraphs.filter((item) => item.text !== '')
      if (validParagraphs.length > 0) {
        // console.log('validFontsUrls: ', validFontsUrls)
        formData.append('list_of_paragraphs', JSON.stringify(validParagraphs))
      } else {
        this.errors.push('Type at least one valid Paragraphs')
        this.$toast.add({
          severity: 'error',
          summary: 'List Paragraphs',
          detail: 'At least one valid Script List Paragraphs is required',
          life: 3000
        })
      }
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
            this.scripts.unshift(response.data), (this.title = '')
            this.list_of_sources_urls = ['']
            this.list_of_shots = [{ text: '', description: '' }]
            this.list_of_examples = [{ title: '', page: '', lang: '', code: '' }]
            this.list_of_paragraphs = [{ text: '', description: '', start: '', end: '' }]
            this.list_of_fonts_urls = [{ name: '', url: '' }]
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
    addOneOfListOfShots() {
      this.list_of_shots.push({ text: '', description: '' })
    },
    removeOneOfListOfShots(index) {
      this.list_of_shots.splice(index, 1)
    },
    addOneOfListOfExamples() {
      this.list_of_examples.push({ title: '', page: '', lang: '', code: '' })
    },
    removeOneOfListOfExamples(index) {
      this.list_of_shots.splice(index, 1)
    },
    addOneOfListOfParagraphs() {
      this.list_of_paragraphs.push({ text: '', description: '', start: '', end: '' })
    },
    removeOneOfListOfParagraphs(index) {
      this.list_of_shots.splice(index, 1)
    },
    addOneOfListOfFontsUrls() {
      this.list_of_fonts_urls.push({ name: '', url: '' })
    },
    removeOneOfListOfFontsUrls(index) {
      this.list_of_fonts_urls.splice(index, 1)
    }
  }
}
</script>
