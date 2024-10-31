<template>
  <div class="">
    <div class="container mx-auto">
      <div class="wrapper_script_details mt-10">
        <div class="inner_script_details p-4">
          <div class="header w-fit flex justify-center items-center mb-7">
            <div
              class="script_image w-[25rem]"
              v-if="script.attachments && script.attachments.length > 0"
            >
              <img :src="script.attachments[0].get_image" />
            </div>
            <div class="script_title pl-5">
              <h2 v-html="script.title" class="text-8xl font-bold"></h2>
            </div>
          </div>
          <!-- list_of_sources_urls -->
          <div class="script_list_of_sources_urls shadow-lg mb-7 py-5 px-3">
            <div class="inner">
              <div class="text border-b py-3">
                <h2 class="text-2xl font-bold" dir="auto">قائمة المصادار</h2>
              </div>
              <div class="my-5 flex justify-between">
                <div
                  class="data"
                  v-for="(script, index) in script.list_of_sources_urls"
                  :key="index"
                >
                  <div class="flex justify-center items-center flex-col">
                    <a :href="script.url" target="_blank" class="mb-3">
                      <prime_button :label="script.name" severity="secondary" />
                    </a>
                    <iframe
                      :src="script.url"
                      frameborder="0"
                      height="100%"
                      width="100%"
                      style="border: 1px solid #ccc"
                    ></iframe>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- list_of_shots[ قائمة التصوير ] -->
          <div class="script_list_of_shots mt-5">
            <prime_fieldset :toggleable="true" legend="قائمة التصوير" style="direction: rtl">
              <div
                v-for="(item, index) in script.list_of_shots"
                :key="index"
                class="mb-5"
                style="direction: ltr"
              >
                <ul>
                  <li>
                    <span class="pr-5" v-html="item.text"> </span>
                    <span class="" v-html="item.description"> </span>
                  </li>
                </ul>
              </div>
            </prime_fieldset>
          </div>
          <!-- list_of_examples قائمة الامثلة -->
          <div class="script_list_of_examples mt-5">
            <prime_fieldset :toggleable="true" legend="قائمة الامثلة" style="direction: rtl">
              <div
                v-for="(item, index) in script.list_of_examples"
                :key="index"
                class="mb-5"
                style="direction: ltr"
              >
                <ul>
                  <li>
                    <span class="pr-5" v-html="item.title"> </span>
                    <span class="pr-5" v-html="item.page"> </span>
                    <span class="" v-html="item.lang"> </span>
                  </li>
                </ul>

                <div class="content-code">
                  <div class="code">
                    <prism :language="item.lang">{{ item.code }}</prism>
                  </div>
                  <div class="icon-copy" @click="copyCode(item.code)">
                    <fa :icon="['fas', 'copy']" />
                  </div>
                </div>
              </div>
            </prime_fieldset>
          </div>
          <!-- script -->
          <div class="script_script mt-5">
            <prime_fieldset :toggleable="true" legend="الاسكرابت" style="direction: rtl">
              <div class="mb-5" style="direction: ltr">
                <h2 v-html="script.script" class="text-2xl font-bold" dir="auto"></h2>
              </div>
            </prime_fieldset>
          </div>
          <!-- list_of_shots[ قائمة المؤثرات الصوتية ] -->
          <div class="script_list_of_sound_effects mt-5">
            <prime_fieldset
              :toggleable="true"
              legend="قائمة المؤثرات الصوتية"
              style="direction: rtl"
            >
              <div
                v-for="(item, index) in script.list_of_sound_effects"
                :key="index"
                class="mb-5"
                style="direction: ltr"
              >
                <ul>
                  <li>
                    <span class="pr-5" v-html="item.name"> </span>
                    <span class="" v-html="item.url"> </span>
                  </li>
                </ul>
              </div>
            </prime_fieldset>
          </div>
        </div>
        <prime_toast />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Prism from 'vue-prism-component'
export default {
  name: 'Script_Details',

  data() {
    return {
      code: 'const a = b',
      script: {
        id: null
      }
    }
  },
  components: { Prism },

  mounted() {
    this.getScript()
  },

  methods: {
    getScript() {
      axios
        .get(`/api/scripts/script_list/script_detail/${this.$route.params.id}/`)
        .then((response) => {
          // For Test
          // console.log('data', response.data)
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
    },
    copyCode(e) {
      navigator.clipboard.writeText(e)
      console.log(e)
    }
  }
}
</script>

<style lang="scss">
.wrapper_script_details {
  .inner_script_details {
    .header {
      .script_image {
        img {
        }
      }
      .script_title {
        h2 {
        }
      }
    }
  }
  &.header {
    &.script_image img {
    }
    &.script_title {
    }
    &.text {
    }
    &.text-8xl {
    }
    &.text-2xl {
    }
    &.font-bold {
    }
    &.shadow-lg {
    }
    &.py-5 {
    }
    &.px-3 {
    }
    &.inner {
    }
    &.data {
      li {
        transition: all 0.3s linear;
        overflow: hidden;
        position: relative;
        counter-increment: counter;
        text-transform: capitalize;
        cursor: pointer;
        &::after {
          content: counter(counter);
          position: absolute;
          // color: var(--color-fff);
          font-weight: 700;
          right: 0px;
          top: 0;
          width: 30px;
          height: 30px;
          display: flex;
          justify-content: center;
          align-items: center;
          background-color: #191e32;
          border-radius: 0px 0px 0px 5px;
        }
        a {
          &:hover {
          }
        }
      }
    }
  }
}
</style>

<!--  

-->
