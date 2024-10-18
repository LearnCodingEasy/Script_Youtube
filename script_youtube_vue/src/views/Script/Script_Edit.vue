<template>
  <div class="">
    <div class="container mx-auto">
      <div class="wrapper_form_create_script px-5">
        <form
          class="form_login"
          v-on:submit.prevent="submitEditScriptForm"
          enctype="multipart/form-data"
        >
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-7">
            <!-- 1️⃣ title -->
            <div class="title border p-5 rounded shadow-lg">
              <h2 dir="auto" class="mb-5 text-1xl font-bold">موضوع الفيديو [ العنوان ]</h2>
              <div class="card">
                <h2 v-html="script.title"></h2>
                <prime_editor
                  v-if="script.title"
                  v-model="script.title"
                  editorStyle="height: 100px"
                />
              </div>
            </div>
            <!-- 2️⃣ list of sources urls -->
            <div class="list_of_sources">
              <h2 dir="auto" class="mb-5 text-1xl font-bold">قائمة المصادار</h2>
              <div v-for="(item, index) in script.list_of_sources_urls" :key="index">
                <prime_input_text type="text" v-model="item.name" placeholder="Enter Name" />
                <prime_input_text type="url" v-model="item.url" placeholder="Enter URL" />

                <prime_button
                  @click="removeOneOfListOfSourcesUrls(index)"
                  severity="danger"
                  icon="pi pi-trash"
                  iconPos="right"
                  class="mx-3"
                >
                </prime_button>
                <prime_button
                  @click="addOneOfListOfSourcesUrls"
                  severity="success"
                  icon="pi pi-folder-plus"
                  iconPos="right"
                >
                </prime_button>
              </div>
            </div>
            <!-- 3️⃣ list of shots -->
            <div class="list_of_sources shadow-lg py-7 px-3">
              <div class="flex justify-between items-center">
                <h2 dir="auto" class="mb-5 text-1xl font-bold">قائمة التصوير</h2>
                <prime_button
                  icon="pi pi-arrow-left"
                  @click="list_of_shots_info_visible = true"
                  class="mx-3"
                />
                <prime_drawer
                  v-model:visible="list_of_shots_info_visible"
                  :header="list_of_shots_info[0].text"
                  :key="list_of_shots_info.id"
                >
                  <p dir="auto" class="text-lg">
                    {{ list_of_shots_info[0].description }}
                  </p>
                </prime_drawer>
              </div>
              <!-- Data -->
              <div class="mb-4">
                <prime_fieldset :toggleable="true" legend="قائمة التصوير">
                  <div class="mb-5">
                    <ul>
                      <li
                        v-for="(item, index) in script.list_of_shots"
                        :key="index"
                        class="pb-3 flex font-bold"
                      >
                        <span class="pr-5" v-html="item.text"></span>
                        <span class="" v-html="item.description"> </span>
                      </li>
                    </ul>
                  </div>
                </prime_fieldset>
              </div>
              <!-- Input Edit -->
              <div v-for="(item, index) in script.list_of_shots" :key="index" class="mb-5">
                <prime_input_text
                  type="text"
                  v-model="item.text"
                  placeholder="Shots Name"
                  class="mb-5"
                >
                </prime_input_text>
                <prime_textarea v-model="item.description" rows="5" cols="30"></prime_textarea>
                <prime_editor editorStyle="height: 100px" v-model="item.description" />
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
            <!-- list_of_examples -->
            <!-- 4️⃣ list of examples -->
            <div class="list_of_examples shadow-lg py-7 px-3">
              <h2 dir="auto">قائمة الامثلة</h2>
              <!-- Data -->
              <div class="mb-4">
                <prime_fieldset :toggleable="true" legend="قائمة الامثلة" style="direction: rtl">
                  <div class="mb-5" style="direction: ltr">
                    <ul>
                      <li
                        v-for="(item, index) in script.list_of_examples"
                        :key="index"
                        class="pb-3 flex font-bold"
                      >
                        <span class="pr-5" v-html="item.title"></span>
                        <span class="" v-html="item.page"> </span>
                        <span class="mr-5" v-html="item.lang"> </span>
                        <div class="block" v-html="item.code"></div>
                      </li>
                    </ul>
                  </div>
                </prime_fieldset>
              </div>
              <!-- Input Edit -->
              <div v-for="(item, index) in script.list_of_examples" :key="index" class="mb-5">
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
            <!-- list_of_paragraphs -->
            <!-- 5️⃣ list of Paragraphs -->
            <div class="list_of_sources shadow-lg py-7 px-3">
              <h2 dir="auto" class="mb-5 text-1xl font-bold">قائمة الفقرات</h2>
              <!-- Data -->
              <div class="mb-4">
                <prime_fieldset :toggleable="true" legend="قائمة التصوير">
                  <div class="mb-5">
                    <ul>
                      <li
                        v-for="(item, index) in script.list_of_paragraphs"
                        :key="index"
                        class="pb-3 flex font-bold"
                      >
                        <span class="pr-5" v-html="item.text"></span>
                        <span class="" v-html="item.description"> </span>
                        <span class="" v-html="item.start"> </span>
                        <span class="" v-html="item.end"> </span>
                      </li>
                    </ul>
                  </div>
                </prime_fieldset>
              </div>
              <!-- Input Edit -->
              <div v-for="(item, index) in script.list_of_paragraphs" :key="index" class="mb-5">
                <prime_input_text
                  type="text"
                  v-model="item.text"
                  placeholder="Paragraphs Name"
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
                  v-model="item.start"
                  placeholder="00.00"
                  class="mb-5 mr-3"
                >
                </prime_input_text>
                <prime_input_text type="number" v-model="item.end" placeholder="00.01" class="mb-5">
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
              <div v-for="(item, index) in script.list_of_fonts_urls" :key="index">
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
              <div v-for="(item, index) in script.list_of_colors" :key="index">
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
              <div v-for="(item, index) in script.list_of_musics" :key="index">
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
              <div v-for="(item, index) in script.list_of_videos_background" :key="index">
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
              <div v-for="(item, index) in script.list_of_images" :key="index">
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
              <div v-for="(item, index) in script.list_of_icons" :key="index">
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
              <div v-for="(item, index) in script.list_of_visual_effects" :key="index">
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
              <div v-for="(item, index) in script.list_of_sound_effects" :key="index">
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
            <!-- 📝 Script -->
            <div class="script border p-5 rounded shadow-lg">
              <h2 dir="auto" class="mb-5 text-1xl font-bold">السيناريو</h2>
              <div class="" v-html="script.script" dir="auto"></div>
              <div class="card">
                <prime_editor v-model="script.script" editorStyle="height: 350px" />
              </div>
            </div>

            <!-- 🖼️ Image -->
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
                  <div id="preview" v-else>
                    <div class="" v-for="image in script.attachments" :key="image.id">
                      <img :src="image.get_image" class="img-thumbnail" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- Send -->
            <div class="send">
              <prime_button
                @click="submitEditScriptForm"
                label="Updated"
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

export default {
  name: 'Script_Edit',

  data() {
    return {
      script: {
        id: null,
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
        attachments: []
      },
      selectedImageFile: null,
      imageFileUrl: null,
      errors: [],
      list_of_shots_info: [
        {
          text: 'قائمة التصوير',
          description:
            '🎥: قائمة تحتوي على جميع المشاهد أو العناصر التي تحتاج إلى تصويرها أو تسجيلها أثناء إعداد الفيديو التعليمي.'
        }
      ],
      list_of_shots_info_visible: false
    }
  },

  mounted() {
    this.getScript()
    console.log('script.list_of_sources_urls: ', this.script.list_of_sources_urls)
  },

  methods: {
    getScript() {
      axios
        .get(`/api/scripts/script_list/script_edit/${this.$route.params.id}/`)
        .then((response) => {
          console.log('data', response.data)
          this.script = response.data
          // تحقق من كل قائمة إذا كانت فارغة، أضف عناصر افتراضية
          if (!this.script.list_of_sources_urls || this.script.list_of_sources_urls.length === 0) {
            this.script.list_of_sources_urls = [{ name: '', url: '' }]
          }
          if (!this.script.list_of_shots || this.script.list_of_shots.length === 0) {
            this.script.list_of_shots = [{ text: '', description: '' }]
          }
          if (!this.script.list_of_examples || this.script.list_of_examples.length === 0) {
            this.script.list_of_examples = [{ title: '', page: '', lang: '', code: '' }]
          }
          if (!this.script.list_of_paragraphs || this.script.list_of_paragraphs.length === 0) {
            this.script.list_of_paragraphs = [{ text: '', description: '', start: '', end: '' }]
          }
          if (!this.script.list_of_fonts_urls || this.script.list_of_fonts_urls.length === 0) {
            this.script.list_of_fonts_urls = [{ name: '', url: '' }]
          }
          if (!this.script.list_of_colors || this.script.list_of_colors.length === 0) {
            this.script.list_of_colors = [{ name: '' }]
          }
          if (!this.script.list_of_musics || this.script.list_of_musics.length === 0) {
            this.script.list_of_musics = [{ name: '', url: '' }]
          }
          if (
            !this.script.list_of_videos_background ||
            this.script.list_of_videos_background.length === 0
          ) {
            this.script.list_of_videos_background = [{ name: '', url: '' }]
          }
          if (!this.script.list_of_images || this.script.list_of_images.length === 0) {
            this.script.list_of_images = [{ name: '', url: '' }]
          }
          if (!this.script.list_of_icons || this.script.list_of_icons.length === 0) {
            this.script.list_of_icons = [{ name: '', url: '' }]
          }
          if (
            !this.script.list_of_visual_effects ||
            this.script.list_of_visual_effects.length === 0
          ) {
            this.script.list_of_visual_effects = [{ name: '', url: '' }]
          }
          if (
            !this.script.list_of_sound_effects ||
            this.script.list_of_sound_effects.length === 0
          ) {
            this.script.list_of_sound_effects = [{ name: '', url: '' }]
          }
        })
        .catch((error) => {
          console.log('error', error)
          this.$toast.add({
            severity: 'error',
            summary: 'Script List Error',
            detail: `Your Error ${error}`,
            life: 10000
          })
        })
    },
    // For Upload Image to Post Store and for Post
    handleImageFileUpload(event) {
      let file = event.target.files[0]
      if (file) {
        this.selectedImageFile = file
        this.script.image = file
        console.log('file: ', file)
        console.log('this.script.image: ', this.script.image)
        // توليد URL للصورة للعرض
        this.imageFileUrl = URL.createObjectURL(file)
      } else {
        // في حالة عدم اختيار ملف، تفريغ الصورة
        this.imageFileUrl = null
      }
      // this.imageFileUrl = URL.createObjectURL(file)
      // this.selectedImageFile = event.target.files[0]
    },
    submitEditScriptForm() {
      let formData = new FormData()
      // Title
      if (this.script.title == '') {
        this.$toast.add({
          severity: 'error',
          summary: 'Type Script Title',
          detail: 'Your Script Title is missing',
          life: 3000
        })
        this.errors.push('Type Script Title')
      } else if (this.script.title !== '') {
        formData.append('title', this.script.title)
      }
      // JSON أضف قائمة المصادر كـ
      const sources = this.script.list_of_sources_urls.map((item) => ({
        name: item.name,
        url: item.url
      }))
      formData.append('list_of_sources_urls', JSON.stringify(sources))
      // JSON أضف قائمة التصوير كـ
      const shots = this.script.list_of_shots.map((item) => ({
        text: item.text,
        description: item.description
      }))
      formData.append('list_of_shots', JSON.stringify(shots))
      // JSON أضف قائمة التصوير كـ
      const examples = this.script.list_of_examples.map((item) => ({
        title: item.title,
        lang: item.lang,
        page: item.page,
        code: item.code
      }))
      formData.append('list_of_examples', JSON.stringify(examples))
      // JSON أضف قائمة الفقرات كـ
      const paragraphs = this.script.list_of_paragraphs.map((item) => ({
        text: item.text,
        description: item.description,
        start: item.start,
        end: item.end
      }))
      formData.append('list_of_paragraphs', JSON.stringify(paragraphs))
      // JSON أضف قائمة الخطوط كـ
      const fonts = this.script.list_of_fonts_urls.map((item) => ({
        name: item.name,
        url: item.url
      }))
      formData.append('list_of_fonts_urls', JSON.stringify(fonts))
      // JSON أضف قائمة الألوان كـ
      const colors = this.script.list_of_colors.map((item) => ({
        name: item.name
      }))
      formData.append('list_of_colors', JSON.stringify(colors))
      // JSON أضف قائمة الموسيقى كـ
      const musics = this.script.list_of_musics.map((item) => ({
        name: item.name,
        url: item.url
      }))
      formData.append('list_of_musics', JSON.stringify(musics))
      // JSON أضف قائمة الفيديوهات كـ
      const videos = this.script.list_of_videos_background.map((item) => ({
        name: item.name,
        url: item.url
      }))
      formData.append('list_of_videos_background', JSON.stringify(videos))
      // JSON أضف قائمة الصور كـ
      const images = this.script.list_of_images.map((item) => ({
        name: item.name,
        url: item.url
      }))
      formData.append('list_of_images', JSON.stringify(images))
      // JSON أضف قائمة الأيقونات كـ
      const icons = this.script.list_of_icons.map((item) => ({
        name: item.name,
        url: item.url
      }))
      formData.append('list_of_icons', JSON.stringify(icons))
      // JSON أضف قائمة التأثيرات البصرية كـ
      const visualEffects = this.script.list_of_visual_effects.map((item) => ({
        name: item.name,
        url: item.url
      }))
      formData.append('list_of_visual_effects', JSON.stringify(visualEffects))
      // JSON أضف قائمة المؤثرات الصوتية كـ
      const soundEffects = this.script.list_of_sound_effects.map((item) => ({
        name: item.name,
        url: item.url
      }))
      formData.append('list_of_sound_effects', JSON.stringify(soundEffects))
      // Script
      if (this.script.script == '') {
        this.$toast.add({
          severity: 'error',
          summary: 'Type Script script',
          detail: 'Your Script script is missing',
          life: 3000
        })
        this.errors.push('Type Script script')
      } else if (this.script.script !== '') {
        formData.append('script', this.script.script)
      }
      // أضف الصورة إذا كانت موجودة
      if (this.selectedImageFile) {
        formData.append('image', this.selectedImageFile)
      }

      // دالة لتحديث البيانات وإرسال الطلب
      // All Is Good
      if (this.errors.length === 0) {
        axios
          .put(`/api/scripts/script_list/script_edit/${this.script.id}/`, formData)
          .then((response) => {
            console.log('Data updated successfully:', response.data)
            this.$router.push({ name: 'ScriptDetails', params: { id: this.script.id } })

            // معالجة الاستجابة الناجحة
          })
          .catch((error) => {
            console.error('Error updating data:', error)
            this.$toast.add({
              severity: 'error',
              summary: `Script Error`,
              detail: `Your Error ${error}`,
              life: 3000
            })
            // معالجة الخطأ
          })
      }
    },
    addOneOfListOfSourcesUrls() {
      this.script.list_of_sources_urls.push({ name: '', url: '' })
    },
    removeOneOfListOfSourcesUrls(index) {
      this.script.list_of_sources_urls.splice(index, 1)
    },
    addOneOfListOfShots() {
      this.script.list_of_shots.push({ text: '', description: '' })
    },
    removeOneOfListOfShots(index) {
      this.script.list_of_shots.splice(index, 1)
    },
    addOneOfListOfExamples() {
      this.script.list_of_examples.push({ title: '', page: '', lang: '', code: '' })
    },
    removeOneOfListOfExamples(index) {
      this.script.list_of_shots.splice(index, 1)
    },
    addOneOfListOfParagraphs() {
      this.script.list_of_paragraphs.push({ text: '', description: '', start: '', end: '' })
    },
    removeOneOfListOfParagraphs(index) {
      this.script.list_of_shots.splice(index, 1)
    },
    addOneOfListOfFontsUrls() {
      this.script.list_of_fonts_urls.push({ name: '', url: '' })
    },
    removeOneOfListOfFontsUrls(index) {
      this.script.list_of_fonts_urls.splice(index, 1)
    },
    addOneOfListOfColors() {
      this.script.list_of_colors.push({ name: '' })
    },
    removeOneOfListOfColors(index) {
      this.script.list_of_colors.splice(index, 1)
    },
    addOneOfListOfMusics() {
      this.script.list_of_fonts_urls.push({ name: '', url: '' })
    },
    removeOneOfListOfMusics(index) {
      this.script.list_of_musics.splice(index, 1)
    },
    addOneOfListOfVideosBackground() {
      this.script.list_of_videos_background.push({ name: '', url: '' })
    },
    removeOneOfListOfVideosBackground(index) {
      this.script.list_of_videos_background.splice(index, 1)
    },
    addOneOfListOfImages() {
      this.script.list_of_images.push({ name: '', url: '' })
    },
    removeOneOfListOfImages(index) {
      this.script.list_of_images.splice(index, 1)
    },
    addOneOfListOfIcons() {
      this.script.list_of_icons.push({ name: '', url: '' })
    },
    removeOneOfListOfIcons(index) {
      this.script.list_of_icons.splice(index, 1)
    },
    addOneOfListOfVisualEffects() {
      this.script.list_of_visual_effects.push({ name: '', url: '' })
    },
    removeOneOfListOfVisualEffects(index) {
      this.script.list_of_visual_effects.splice(index, 1)
    },
    addOneOfListOfSoundEffects() {
      this.script.list_of_sound_effects.push({ name: '', url: '' })
    },
    removeOneOfListOfSoundEffects(index) {
      this.script.list_of_sound_effects.splice(index, 1)
    }
  }
}
</script>
