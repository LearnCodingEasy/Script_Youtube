<script setup>
import { RouterLink } from 'vue-router'
import axios from 'axios'

// import { ref } from 'vue'
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
  <div class="wrapper_dashboard">
    <div class="container mx-auto">
      <div class="inner">
        <!-- sidebar -->
        <div class="sidebar">
          <!-- sidebar_brand -->
          <div class="sidebar_brand">
            <RouterLink class="flex justify-start items-center">
              <div class="logo">
                <i class="pi pi-video"></i>
              </div>
              <div class="text">
                <span> Script Youtube</span>
              </div>
            </RouterLink>
          </div>
          <!-- sidebar_menu -->
          <div class="sidebar_menu">
            <ul>
              <li>
                <RouterLink to="/" class="active"
                  ><span class="icon"> <i class="pi pi-cog"></i> </span
                  ><span class="text">Dashboard</span></RouterLink
                >
              </li>
              <li>
                <RouterLink to="/"
                  ><span class="icon"> <i class="pi pi-home"></i> </span
                  ><span class="text">Home</span></RouterLink
                >
              </li>
              <li>
                <RouterLink
                  class="flex align-middle"
                  v-if="userStore.user.id"
                  :to="{ name: 'profile', params: { id: userStore.user.id } }"
                  ><span class="icon"> <i class="pi pi-user"></i> </span>
                  <span class="text" v-if="userStore.user.name == null">Profile user</span>
                  <span class="text" v-else>Profile {{ userStore.user.name }}</span>
                </RouterLink>
              </li>
              <li>
                <RouterLink to="/ScriptList"
                  ><span class="icon"> <i class="pi pi-list-check"></i> </span
                  ><span class="text">Script List</span></RouterLink
                >
              </li>
              <li>
                <RouterLink to="/ScriptCreate"
                  ><span class="icon"> <i class="pi pi-file-plus"></i> </span
                  ><span class="text">Add Script</span></RouterLink
                >
              </li>
            </ul>
          </div>
        </div>
        <!-- main_content -->
        <div class="main_content">
          <!-- main_content_header -->
          <div class="main_content_header flex justify-between px-4 py-6 shadow-md">
            <!-- Left -->
            <h2 class="main_content_header_left flex items-center">
              <label for=""><i class="pi pi-bars"></i> </label>Dashboard
            </h2>
            <!-- Center -->
            <div class="input_search">
              <prime_icon_field>
                <prime_input_icon class="pi pi-search" />
                <prime_input_text placeholder="Search Script Youtube" />
              </prime_icon_field>
            </div>
            <!-- Right -->
            <div class="user_wrapper flex justify-center items-center">
              <img src="../../assets/Image/user.png" class="rounded-full mr-4" alt="" />
              <div class="user_data">
                <h4>{{ userStore.user.name }}</h4>
                <small class="text-zinc-500">Supe Admin</small>
              </div>
            </div>
          </div>
          <div class="main_content_main">
            <div class="cards">
              <div class="card_single">
                <div class="text">
                  <h2>{{ scripts.length }}</h2>
                  <span>All Script</span>
                </div>
                <div class="icon">
                  <span class="">
                    <i class="pi pi-folder-open"></i>
                  </span>
                </div>
              </div>
              <div class="card_single">
                <div class="text">
                  <h2>{{ scriptsUser.length }}</h2>
                  <span>Your Scripts</span>
                </div>
                <div class="icon">
                  <span class="">
                    <i class="pi pi-file-check"></i>
                  </span>
                </div>
              </div>
              <div class="card_single">
                <div class="text">
                  <h2>77</h2>
                  <span>Tasks</span>
                </div>
                <div class="icon">
                  <span class="">
                    <i class="pi pi-list-check"></i>
                  </span>
                </div>
              </div>
              <div class="card_single">
                <div class="text">
                  <h2>54</h2>
                  <span>Customers</span>
                </div>
                <div class="icon">
                  <span class="">
                    <i class="pi pi-cog"></i>
                  </span>
                </div>
              </div>
            </div>
          </div>
          <div class="main_content_footer">
            <div class="project">
              <div class="card">
                <div class="card_header flex justify-between item-center px-6">
                  <h2 class="text-3xl bold">Recent Projects</h2>
                  <!-- <button>Sell All <i class="pi pi-arrow-right"></i></button> -->
                  <prime_button
                    label="Sell All"
                    icon="pi pi-arrow-right"
                    iconPos="right"
                    severity="danger"
                  />
                </div>

                <div class="card_body px-6">
                  <prime_data_table
                    v-model:filters="filters"
                    :value="scriptsUser"
                    paginator
                    :rows="5"
                    dataKey="id"
                    filterDisplay="row"
                    :loading="loading"
                    :globalFilterFields="['title', 'name']"
                  >
                    <!-- Header Search -->
                    <template #header>
                      <div class="flex justify-end">
                        <prime_icon_field>
                          <prime_input_icon>
                            <i class="pi pi-search" />
                          </prime_input_icon>
                          <prime_input_text
                            v-model="filters['global'].value"
                            placeholder="Keyword Search"
                          />
                        </prime_icon_field>
                      </div>
                    </template>
                    <template #empty> No scripts found. </template>
                    <template #loading> Loading scripts data. Please wait. </template>
                    <!-- Table Data -->
                    <prime_column
                      v-for="col in columns"
                      :key="col.field"
                      :field="col.field"
                      :header="col.header"
                      style="min-width: 12rem"
                    >
                      <template #body="{ data }">
                        <span class="" v-if="userStore.user.id == data.created_by.id">
                          {{ data[col.field] }}
                        </span>
                      </template>
                    </prime_column>
                    <!-- Delete -->
                    <prime_column header="Delete" style="min-width: 10rem">
                      <template #body="{ data }">
                        <prime_button
                          icon="pi pi-trash"
                          severity="danger"
                          text
                          rounded
                          aria-label="Delete"
                          @click="deleteScript(data.id)"
                          v-if="userStore.user.id == data.created_by.id"
                        />
                      </template>
                    </prime_column>
                    <!-- Edit -->
                    <prime_column header="Edit" style="min-width: 10rem">
                      <template #body="{ data }">
                        <prime_button
                          icon="pi pi-file-edit"
                          severity="success"
                          text
                          rounded
                          aria-label="Edit"
                          @click="$router.push({ name: 'ScriptEdit', params: { id: data.id } })"
                          v-if="userStore.user.id == data.created_by.id"
                        />
                      </template>
                    </prime_column>
                  </prime_data_table>
                </div>
              </div>
            </div>
            <div class="customers"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
import { FilterMatchMode } from '@primevue/core/api'
import { useUserStore } from '@/stores/user'

export default {
  name: 'DashboardView',
  data() {
    return {
      // البيانات
      scripts: [],
      scriptsUser: [],

      // T
      columns: [
        { field: 'title', header: 'Title' },
        { field: 'name', header: 'Name' }
      ],
      filters: {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS },
        title: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
        name: { value: null, matchMode: FilterMatchMode.STARTS_WITH }
      },
      loading: true,

      scriptId: 'your-script-uuid-here', // معرف السكريبت المطلوب حذفه
      errors: [] // مصفوفة الأخطاء
    }
  },
  async mounted() {
    await this.getAllScripts()
    await this.getAllScriptsUser()
  },
  methods: {
    /* 
    .get(`/api/posts/profile/${this.$route.params.id}/`)
      .then(response => {
          console.log('data', response.data)
          this.posts = response.data.posts
          this.user = response.data.user
      })
    */
    async getAllScripts() {
      try {
        const response = await axios.get(`/api/scripts/script_list/`)
        console.log('response: ', response)
        this.scripts = response.data
        console.log('response.data: ', response.data)
        console.log('this.scripts: ', this.scripts)
        this.loading = false
      } catch (error) {
        console.error('Error fetching scripts:', error)
        this.$toast.add({
          severity: 'error',
          summary: 'Script List Error',
          detail: `Error: ${error.message}`,
          life: 5000
        })
      }
    },
    async getAllScriptsUser() {
      try {
        // تعريف userStore هنا
        const userStore = useUserStore()

        const response = await axios.get(`/api/scripts/script_list/${userStore.user.id}`)
        console.log('response: ', response)

        console.log('userStore.id: ', userStore.user.id)
        this.scriptsUser = response.data.scripts
        console.log('scriptsUser response.data: ', response.data)
        console.log('this.scriptsUser: ', this.scriptsUser)
        this.loading = false
      } catch (error) {
        console.error('Error fetching scripts:', error)
        this.$toast.add({
          severity: 'error',
          summary: 'Script List Error',
          detail: `Error: ${error.message}`,
          life: 5000
        })
      }
    },
    async deleteScript(scriptId) {
      if (confirm('Are you sure you want to delete this script?')) {
        try {
          const response = await axios.delete(`/api/scripts/script_list/script_delete/${scriptId}/`)
          if (response.data.message === 'script deleted') {
            this.scripts = this.scripts.filter((script) => script.id !== scriptId)
            this.$toast.add({
              severity: 'success',
              summary: 'Script Deleted',
              detail: 'Script successfully deleted.',
              life: 3000
            })
          }
        } catch (error) {
          console.error('Error deleting script:', error)
          this.$toast.add({
            severity: 'error',
            summary: 'Delete Error',
            detail: `Error: ${error.message}`,
            life: 5000
          })
        }
      }
    }
  },
  created() {
    // this.columns = [
    //   { field: 'title', header: 'Title' },
    //   { field: 'name', header: 'Name' },
    //   { field: 'category', header: 'Category' },
    //   { field: 'quantity', header: 'Quantity' }
    // ]
  }
}
</script>

<style lang="scss" scoped>
.sidebar {
  width: 345px;
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
  z-index: 100;
  // For Test
  background-color: #ff4444;
  .sidebar_brand {
    height: 90px;
    padding: 2rem 0rem 1rem 2rem;
    a {
      color: white;
      .logo {
        padding-right: 1rem;
        i {
        }
      }
      .text {
        span {
          display: inline-block;
          padding-right: 1rem;
        }
      }
    }
  }
  .sidebar_menu {
    margin-top: 1rem;
    ul {
      li {
        width: 100%;
        margin-bottom: 1.7rem;
        padding-left: 1rem;
        a {
          display: block;
          font-size: 1.1rem;
          padding-left: 1rem;
          span:first-child {
            font-size: 1.5rem;
            padding-right: 1rem;
          }
          .icon {
            i {
              color: white;
            }
          }
          .text {
            color: white;
          }
          &.active {
            padding-top: 1rem;
            padding-bottom: 1rem;
            border-radius: 30px 0 0 30px;
            // For Test
            background-color: #fff;
            .icon {
              i {
                color: #000;
              }
            }
            .text {
              color: #000;
            }
          }
        }
      }
    }
  }
}
.main_content {
  margin-left: 345px;
  min-height: calc(100vh - 90px);

  .main_content_header {
    position: fixed;
    top: 0;
    left: 345px;
    width: calc(100% - 345px);
    z-index: 100;
    .main_content_header_left {
      label {
        i {
          font-size: 1.7rem;
          padding-right: 1rem;
        }
      }
    }
    .input_search {
    }
    .user_wrapper {
      img {
      }
      .user_data {
        h4 {
        }
      }
    }
  }
  .main_content_main {
    margin-top: 85px;
    padding: 2rem 1.5rem;
    .cards {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      grid-gap: 2rem;
      margin-top: 1rem;
      .card_single {
        display: flex;
        justify-content: space-between;
        padding: 2rem;
        border-radius: 5px;
        border: 0.1rem solid #999;
        .text {
          span {
            color: #999;
          }
        }
        .icon {
          i {
            font-size: 3rem;
            color: #ff4444;
          }
        }
        &:first-child {
          background-color: #ff4444;
          .text {
            color: #fff;

            span {
              color: #fff;
            }
          }
          .icon {
            i {
              font-size: 3rem;
              color: #fff;
            }
          }
        }
      }
    }
  }
}
body {
  border: 0.5rem solid #f00;
  #app {
    border: 0.5rem solid #f00;
    > div {
      border: 0.5rem solid #f00;
      .wrapper_header {
        display: none;
      }
    }
  }
}
</style>
