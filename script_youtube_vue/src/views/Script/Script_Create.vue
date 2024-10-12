<template>
  <div class="Component-Name mt-8">
    <div class="container mx-auto">
      <div class="wrapper_form_create_script px-5">
        <form class="form_login" v-on:submit.prevent="submitAddScriptForm">
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-7">
            <!-- 1️⃣ title -->
            <div class="title border p-5 rounded shadow-lg">
              <h2 dir="auto" class="mb-5 text-1xl font-bold">موضوع الفيديو [ العنوان ]</h2>
              <div class="card">
                <prime_editor v-model="title" editorStyle="height: 50px" />
              </div>
            </div>
            <!-- 2️⃣ list of sources urls -->
            <div class="list_of_sources">
              <h2 dir="auto">قائمة المصادار</h2>
              <div v-for="(item, index) in list_of_sources_urls" :key="index">
                <prime_input_text type="text" v-model="item.name" placeholder="Enter URL" />
                <prime_input_text type="url" v-model="item.url" placeholder="Enter URL" />

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
              <h2 dir="auto" class="mb-5 text-1xl font-bold">قائمة الفقرات</h2>
              <div v-for="(item, index) in list_of_paragraphs" :key="index" class="mb-5">
                <prime_input_text
                  type="text"
                  v-model="item.text"
                  placeholder="Font Name"
                  class="mb-5"
                >
                </prime_input_text>
                <prime_editor
                  v-model="item.description"
                  editorStyle="height: 100px"
                  style="margin-bottom: 1rem"
                />
                <prime_input_text
                  type="number"
                  v-model="item.text"
                  placeholder="00.00"
                  class="mb-5"
                >
                </prime_input_text>
                <prime_input_text
                  type="number"
                  v-model="item.text"
                  placeholder="00.01"
                  class="mb-5"
                >
                </prime_input_text>
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
            <!-- 7️⃣ list of Colors -->
            <div class="list_of_sources shadow-lg py-7 px-3">
              <h2 dir="auto" class="mb-5 text-1xl font-bold">قائمة الالوان</h2>
              <div v-for="(item, index) in list_of_colors" :key="index">
                <prime_input_text type="text" v-model="item.name" placeholder="Font Name">
                </prime_input_text>
                <prime_button
                  @click="removeOneOfListOfColors(index)"
                  severity="danger"
                  icon="pi pi-trash"
                  iconPos="right"
                  class="mx-3"
                ></prime_button>
                <prime_button
                  @click="addOneOfListOfColors"
                  severity="success"
                  icon="pi pi-folder-plus"
                  iconPos="right"
                ></prime_button>
              </div>
            </div>
            <!-- 8️⃣ list of Musics -->
            <div class="list_of_sources shadow-lg py-7 px-3">
              <h2 dir="auto" class="mb-5 text-1xl font-bold">قائمة الموسيقى</h2>
              <div v-for="(item, index) in list_of_musics" :key="index">
                <prime_input_text type="text" v-model="item.name" placeholder="Musics Name">
                </prime_input_text>
                <prime_input_text type="url" v-model="item.url" placeholder="Musics Url">
                </prime_input_text>
                <prime_button
                  @click="removeOneOfListOfColors(index)"
                  severity="danger"
                  icon="pi pi-trash"
                  iconPos="right"
                  class="mx-3"
                ></prime_button>
                <prime_button
                  @click="addOneOfListOfColors"
                  severity="success"
                  icon="pi pi-folder-plus"
                  iconPos="right"
                ></prime_button>
              </div>
            </div>
            <!-- 9️⃣ list of Musics -->
            <div class="list_of_sources shadow-lg py-7 px-3">
              <h2 dir="auto" class="mb-5 text-1xl font-bold">قائمة فيديوهات الخلفية</h2>
              <div v-for="(item, index) in list_of_videos_background" :key="index">
                <prime_input_text type="text" v-model="item.name" placeholder="Musics Name">
                </prime_input_text>
                <prime_input_text type="url" v-model="item.url" placeholder="Musics Url">
                </prime_input_text>
                <prime_button
                  @click="removeOneOfListOfColors(index)"
                  severity="danger"
                  icon="pi pi-trash"
                  iconPos="right"
                  class="mx-3"
                ></prime_button>
                <prime_button
                  @click="addOneOfListOfColors"
                  severity="success"
                  icon="pi pi-folder-plus"
                  iconPos="right"
                ></prime_button>
              </div>
            </div>
            <!-- 🔟 list of Images -->
            <div class="list_of_sources shadow-lg py-7 px-3">
              <h2 dir="auto" class="mb-5 text-1xl font-bold">قائمة الصور</h2>
              <div v-for="(item, index) in list_of_images" :key="index">
                <prime_input_text type="text" v-model="item.name" placeholder="Images Name">
                </prime_input_text>
                <prime_input_text type="url" v-model="item.url" placeholder="Images Url">
                </prime_input_text>
                <prime_button
                  @click="removeOneOfListOfImages(index)"
                  severity="danger"
                  icon="pi pi-trash"
                  iconPos="right"
                  class="mx-3"
                ></prime_button>
                <prime_button
                  @click="addOneOfListOfImages"
                  severity="success"
                  icon="pi pi-folder-plus"
                  iconPos="right"
                ></prime_button>
              </div>
            </div>
            <!-- 1️⃣1️⃣ list of Icons -->
            <div class="list_of_sources shadow-lg py-7 px-3">
              <h2 dir="auto" class="mb-5 text-1xl font-bold">قائمة الأيقونات</h2>
              <div v-for="(item, index) in list_of_icons" :key="index">
                <prime_input_text type="text" v-model="item.name" placeholder="Icons Name">
                </prime_input_text>
                <prime_input_text type="url" v-model="item.url" placeholder="Icons Url">
                </prime_input_text>
                <prime_button
                  @click="removeOneOfListOfIcons(index)"
                  severity="danger"
                  icon="pi pi-trash"
                  iconPos="right"
                  class="mx-3"
                ></prime_button>
                <prime_button
                  @click="addOneOfListOfIcons"
                  severity="success"
                  icon="pi pi-folder-plus"
                  iconPos="right"
                ></prime_button>
              </div>
            </div>
            <!-- 1️⃣2️⃣ list of Visual Effects -->
            <div class="list_of_sources shadow-lg py-7 px-3">
              <h2 dir="auto" class="mb-5 text-1xl font-bold">قائمة التأثيرات البصرية</h2>
              <div v-for="(item, index) in list_of_visual_effects" :key="index">
                <prime_input_text type="text" v-model="item.name" placeholder="Visual Effects Name">
                </prime_input_text>
                <prime_input_text type="url" v-model="item.url" placeholder="Visual Effects Url">
                </prime_input_text>
                <prime_button
                  @click="removeOneOfListOfVisualEffects(index)"
                  severity="danger"
                  icon="pi pi-trash"
                  iconPos="right"
                  class="mx-3"
                ></prime_button>
                <prime_button
                  @click="addOneOfListOfVisualEffects"
                  severity="success"
                  icon="pi pi-folder-plus"
                  iconPos="right"
                ></prime_button>
              </div>
            </div>
            <!-- 1️⃣3️⃣ list of Sound Effects -->
            <div class="list_of_sources shadow-lg py-7 px-3">
              <h2 dir="auto" class="mb-5 text-1xl font-bold">قائمة المؤثرات الصوتية</h2>
              <div v-for="(item, index) in list_of_sound_effects" :key="index">
                <prime_input_text type="text" v-model="item.name" placeholder="Sound Effects Name">
                </prime_input_text>
                <prime_input_text type="url" v-model="item.url" placeholder="Sound Effects Url">
                </prime_input_text>
                <prime_button
                  @click="removeOneOfListOfSoundEffects(index)"
                  severity="danger"
                  icon="pi pi-trash"
                  iconPos="right"
                  class="mx-3"
                ></prime_button>
                <prime_button
                  @click="addOneOfListOfSoundEffects"
                  severity="success"
                  icon="pi pi-folder-plus"
                  iconPos="right"
                ></prime_button>
              </div>
            </div>
            <!-- Script -->
            <div class="script border p-5 rounded shadow-lg">
              <h2 dir="auto" class="mb-5 text-1xl font-bold">السيناريو</h2>
              <div class="card">
                <prime_editor v-model="script" editorStyle="height: 350px" />
              </div>
            </div>
            <!-- Script -->
            <div class="script border p-5 rounded shadow-lg">
              <h2 dir="auto" class="mb-5 text-1xl font-bold">صورة الغلاف</h2>
              <div class="card">
                <input
                  type="file"
                  ref="file"
                  @change="handleImageFileUpload"
                  class="form-control"
                  placeholder="image"
                  id="image"
                />
                <div class="show_image_script">
                  <div id="preview" v-if="imageFileUrl">
                    <img :src="imageFileUrl" class="img-thumbnail" />
                  </div>
                </div>
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
      list_of_sources_urls: [{ name: '', url: '' }],
      list_of_shots: [{ text: '', description: '' }],
      list_of_examples: [{ title: '', page: '', lang: '', code: '' }],
      list_of_paragraphs: [{ text: '', description: '', start: '', end: '' }],
      list_of_fonts_urls: [{ name: '', url: '' }],
      list_of_colors: [{ name: '' }],
      list_of_musics: [{ name: '', url: '' }],
      list_of_videos_background: [{ name: '', url: '' }],
      list_of_images: [{ name: '', url: '' }],
      list_of_icons: [{ name: '', url: '' }],
      list_of_visual_effects: [{ name: '', url: '' }],
      list_of_sound_effects: [{ name: '', url: '' }],
      script: '',
      selectedImageFile: null,
      imageFileUrl: null,
      errors: []
    }
  },

  methods: {
    // For Upload Image to Post Store and for Post
    handleImageFileUpload(event) {
      let file = event.target.files[0]
      if (file) {
        console.log('event.target.files[0]: ', event.target.files[0])
        console.log('file: ', file)
        this.selectedImageFile = file

        this.imageFileUrl = URL.createObjectURL(file)
        // توليد URL للصورة للعرض
      } else {
        // في حالة عدم اختيار ملف، تفريغ الصورة
        this.imageFileUrl = null
      }
      // this.imageFileUrl = URL.createObjectURL(file)
      // this.selectedImageFile = event.target.files[0]
    },
    // Add Script
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
      // 2️ list of Colors
      const validColors = this.list_of_colors.filter((item) => item.text !== '')
      if (validColors.length > 0) {
        formData.append('list_of_colors', JSON.stringify(validColors))
      } else {
        this.errors.push('Type at least one valid colors')
        this.$toast.add({
          severity: 'error',
          summary: 'List Colors',
          detail: 'At least one valid Script List Colors is required',
          life: 3000
        })
      }
      // 2️ list of Musics
      const validMusics = this.list_of_musics.filter((item) => item.text !== '')
      if (validMusics.length > 0) {
        formData.append('list_of_musics', JSON.stringify(validMusics))
      } else {
        this.errors.push('Type at least one valid musics')
        this.$toast.add({
          severity: 'error',
          summary: 'List m',
          detail: 'At least one valid Script List Colors is required',
          life: 3000
        })
      }
      // 2️ list of Videos Background
      const validVideosBackground = this.list_of_videos_background.filter(
        (item) => item.text !== ''
      )
      if (validVideosBackground.length > 0) {
        formData.append('list_of_videos_background', JSON.stringify(validVideosBackground))
      } else {
        this.errors.push('Type at least one valid Videos Background')
        this.$toast.add({
          severity: 'error',
          summary: 'List Videos Background',
          detail: 'At least one valid Script List Videos Background is required',
          life: 3000
        })
      }
      // 2️ list of Images
      const validImages = this.list_of_images.filter((item) => item.name !== '')
      if (validImages.length > 0) {
        formData.append('list_of_images', JSON.stringify(validImages))
      } else {
        this.errors.push('Type at least one valid Images')
        this.$toast.add({
          severity: 'error',
          summary: 'List Images',
          detail: 'At least one valid Script List Images is required',
          life: 3000
        })
      }
      // 2️ list of Icons
      const validIcons = this.list_of_icons.filter((item) => item.name !== '')
      if (validIcons.length > 0) {
        formData.append('list_of_icons', JSON.stringify(validIcons))
      } else {
        this.errors.push('Type at least one valid Icons')
        this.$toast.add({
          severity: 'error',
          summary: 'List Icons',
          detail: 'At least one valid Script List Icons is required',
          life: 3000
        })
      }
      // 2️ list of Visual Effects
      const validVisualEffects = this.list_of_visual_effects.filter((item) => item.name !== '')
      if (validVisualEffects.length > 0) {
        formData.append('list_of_visual_effects', JSON.stringify(validVisualEffects))
      } else {
        this.errors.push('Type at least one valid Visual Effects')
        this.$toast.add({
          severity: 'error',
          summary: 'List Visual Effects',
          detail: 'At least one valid Script List Visual Effects is required',
          life: 3000
        })
      }
      // 2️ list of Sound Effects
      const validSoundEffects = this.list_of_sound_effects.filter((item) => item.name !== '')
      if (validSoundEffects.length > 0) {
        formData.append('list_of_sound_effects', JSON.stringify(validSoundEffects))
      } else {
        this.errors.push('Type at least one valid Sound Effects')
        this.$toast.add({
          severity: 'error',
          summary: 'List Sound Effects',
          detail: 'At least one valid Script List Sound Effects is required',
          life: 3000
        })
      }
      // Script
      if (this.script == '') {
        this.$toast.add({
          severity: 'error',
          summary: 'Type Script ',
          detail: 'Your Script is missing',
          life: 3000
        })
        this.errors.push('Type Script')
      } else if (this.script !== '') {
        formData.append('script', this.script)
      }
      // Add Image [  ] إضافة الصور إذا تم تحديدها
      if (this.selectedImageFile) {
        formData.append('attachments', this.selectedImageFile)
        // formData.append('image', this.selectedImageFile)
      } else if (this.selectedImageFile !== '') {
        this.$toast.add({
          severity: 'error',
          summary: 'Upload Script Image',
          detail: 'Your Script Image is missing',
          life: 3000
        })
        this.errors.push('Upload Script Image')
      }
      // All Is Good
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
            this.list_of_sources_urls = [{ name: '', url: '' }]
            this.list_of_shots = [{ text: '', description: '' }]
            this.list_of_examples = [{ title: '', page: '', lang: '', code: '' }]
            this.list_of_paragraphs = [{ text: '', description: '', start: '', end: '' }]
            this.list_of_fonts_urls = [{ name: '', url: '' }]
            this.list_of_colors = [{ name: '' }]
            this.list_of_musics = [{ name: '', url: '' }]
            this.list_of_videos_background = [{ name: '', url: '' }]
            this.list_of_images = [{ name: '', url: '' }]
            this.list_of_icons = [{ name: '', url: '' }]
            this.list_of_visual_effects = [{ name: '', url: '' }]
            this.list_of_sound_effects = [{ name: '', url: '' }]
            this.script = ``

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
    },
    addOneOfListOfColors() {
      this.list_of_colors.push({ name: '' })
    },
    removeOneOfListOfColors(index) {
      this.list_of_colors.splice(index, 1)
    },
    addOneOfListOfMusics() {
      this.list_of_fonts_urls.push({ name: '', url: '' })
    },
    removeOneOfListOfMusics(index) {
      this.list_of_musics.splice(index, 1)
    },
    addOneOfListOfVideosBackground() {
      this.list_of_videos_background.push({ name: '', url: '' })
    },
    removeOneOfListOfVideosBackground(index) {
      this.list_of_videos_background.splice(index, 1)
    },
    addOneOfListOfImages() {
      this.list_of_images.push({ name: '', url: '' })
    },
    removeOneOfListOfImages(index) {
      this.list_of_images.splice(index, 1)
    },
    addOneOfListOfIcons() {
      this.list_of_icons.push({ name: '', url: '' })
    },
    removeOneOfListOfIcons(index) {
      this.list_of_icons.splice(index, 1)
    },
    addOneOfListOfVisualEffects() {
      this.list_of_visual_effects.push({ name: '', url: '' })
    },
    removeOneOfListOfVisualEffects(index) {
      this.list_of_visual_effects.splice(index, 1)
    },
    addOneOfListOfSoundEffects() {
      this.list_of_sound_effects.push({ name: '', url: '' })
    },
    removeOneOfListOfSoundEffects(index) {
      this.list_of_sound_effects.splice(index, 1)
    }
  }
}
</script>
