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
              <h2 dir="auto">قائمة المصادار</h2>
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
        attachments: [{ get_image: ``, id: `` }]
      },
      selectedImageFile: null,
      imageFileUrl: null,
      errors: []
    }
  },

  mounted() {
    this.getScript()
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
      // دالة لتحديث البيانات وإرسال الطلب
      axios
        .put(`/api/scripts/script_list/script_edit/${this.script.id}/`, this.script)
        .then((response) => {
          console.log('Data updated successfully:', response.data)
          this.$router.push({ name: 'ScriptDetails', params: { id: this.script.id } })

          // معالجة الاستجابة الناجحة
        })
        .catch((error) => {
          console.error('Error updating data:', error)
          // معالجة الخطأ
        })
    }
  }
}
</script>
