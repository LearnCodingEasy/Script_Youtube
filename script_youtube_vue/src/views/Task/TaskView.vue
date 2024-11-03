<template>
  <div class="Component-Name mt-8">
    <div class="container mx-auto">
      <div class="wrapper_form_create_task px-5 py-4">
        <dov class="inner_task">
          <div class="grid">
            <div v-if="boards" class="grid grid_200">
              <!-- Form Add Board -->
              <div class="py-4 px-2 border shadow-lg rounded-2xl h-48">
                <form
                  class="form_login h-full"
                  v-on:submit.prevent="submitAddBoardForm"
                  enctype="multipart/form-data "
                >
                  <div class="flex flex-col items-center justify-evenly h-full">
                    <!-- 1️⃣ title -->
                    <div class="title col-span-1 md:col-span-2">
                      <div class="card">
                        <prime_input_text
                          v-model="board_title"
                          editorStyle="height: 50px"
                          class="w-full"
                        />
                      </div>
                    </div>
                    <div class="w-full">
                      <div class="flex justify-between">
                        <!-- 🎨 Background -->
                        <div class="board_background flex items-center flex-col">
                          <input
                            type="color"
                            name=""
                            id=""
                            v-model="board_background"
                            width="50px"
                            height="50px"
                            class="color-picker"
                          />
                          <div>{{ board_background }}</div>
                        </div>
                        <!-- Send -->
                        <div class="send">
                          <prime_button
                            @click="submitAddBoardForm"
                            severity="success"
                            icon="pi pi-send"
                            iconPos="right"
                            class="flex justify-center items-center"
                          ></prime_button>
                          <div>Send</div>
                        </div>
                      </div>
                    </div>
                  </div>
                </form>
              </div>
              <!-- Board List -->
              <div v-for="board in boards" :key="board">
                <div
                  class="py-4 px-2 border shadow-lg rounded-2xl h-48 flex justify-center items-center"
                  :style="{ backgroundColor: board.background }"
                >
                  <h2
                    class="font-bold text-white capitalize text-4xl cursor-pointer"
                    @click="gatAllLists(board)"
                  >
                    {{ board.title }}
                  </h2>
                </div>
                <!--  -->
                <prime_dialog
                  v-if="visibleBoardInfo"
                  v-model:visible="visibleBoardInfo"
                  maximizable
                  modal
                  :header="board.title"
                  :style="{ width: '50rem' }"
                  :breakpoints="{ '1199px': '75vw', '575px': '90vw' }"
                >
                  <div v-if="lists.length > 0">
                    <ul>
                      <li v-for="list in lists" :key="list.id">{{ list.title }}</li>
                    </ul>
                  </div>
                  <div v-else>
                    <p>No lists available for this board.</p>
                  </div>
                </prime_dialog>
              </div>
            </div>
            <div v-else>
              <div class="grid grid_200">
                <div class="">
                  <prime_skeleton height="8rem"></prime_skeleton>
                </div>
                <div class="py-4 px-2 border shadow-lg rounded-2xl">
                  <form
                    class="form_login"
                    v-on:submit.prevent="submitAddBoardForm"
                    enctype="multipart/form-data "
                  >
                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-7">
                      <!-- 1️⃣ title -->
                      <div class="title px-2 col-span-1 md:col-span-2">
                        <h2 dir="auto" class="mb-5 text-1xl font-bold">العنوان</h2>
                        <div class="card">
                          <prime_input_text
                            v-model="board_title"
                            editorStyle="height: 50px"
                            class="w-full"
                          />
                        </div>
                      </div>

                      <!-- Send -->
                      <div class="send px-2">
                        <prime_button
                          @click="submitAddBoardForm"
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
          </div>
        </dov>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'

export default {
  name: 'TaskView',
  props: [],
  computed: {},
  watch: {},
  async created() {},
  setup() {
    return {}
  },
  data() {
    return {
      // Board
      board_title: ``,
      board_background: `#333333`,
      board_errors: [],
      boards: [],
      // List
      visibleBoardInfo: false,
      selectedBoard: null,
      list_title: '',
      list_errors: [],
      lists: [],

      statusOptions: [
        { name: 'TASKS', code: 'Tasks' },
        { name: 'DONE', code: 'Done' },
        { name: 'IN_MAKING', code: 'In Making' }
      ],
      // قيمة افتراضية
      task_status: 'TASKS',
      is_private: false,
      title: '',
      list_of_item_number: 0,
      // Tasks List
      tasks: [],

      errors: []
    }
  },
  async mounted() {
    await this.gatAllBoards()
    // await this.gatAllLists(`2aafced5-bdef-4705-b4a5-7263a334d50d`)
  },
  methods: {
    // Add Board
    submitAddBoardForm() {
      this.board_errors = []

      let formData = new FormData()

      // Title
      if (this.board_title == '') {
        this.$toast.add({
          severity: 'error',
          summary: 'Type Board Title',
          detail: 'Your Board Title is missing',
          life: 3000
        })
        this.board_errors.push('Type Board Title')
      } else if (this.board_title !== '') {
        formData.append('title', this.board_title)
      }
      // Background
      if (this.board_background == '') {
        this.$toast.add({
          severity: 'error',
          summary: 'Type Board Background',
          detail: 'Your Board Background is missing',
          life: 3000
        })
        this.board_errors.push('Type Board Background')
      } else if (this.board_background !== '') {
        formData.append('background', this.board_background)
      }

      // All Is Good
      if (this.board_errors.length === 0) {
        axios
          .post('/api/tasks/board_create/', formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          })
          .then((response) => {
            this.board_title = ''
            this.board_background = '#333333'
            console.log('Data Is Send To Django: ', response.data)
            this.$toast.add({
              severity: 'success',
              summary: 'Board Done',
              detail: 'Good Board Youtube Adding.',
              life: 3000
            })
            // this.boards.unshift(response.data), (this.board_title = '')

            // this.$router.push({ name: 'TaskDetails', params: { id: this.task.id } })
            if (this.user) {
              console.log('this.user: ', this.user)
              // this.user.posts_count += 1
            }
          })
          .catch((error) => {
            console.log('error', error)
            console.log('error.response.data', error.response.data)
            this.$toast.add({
              severity: 'error',
              summary: `Type Board Error`,
              detail: `Error = ${error.response.data}`,
              life: 3000
            })
          })
      }
    },
    // All Board
    gatAllBoards() {
      let line = '📌'.repeat(30)
      console.log(` %c${line} `, 'color: #1cd07c; font-size: 16px')
      console.log(` %c All Board`, 'color: #1cd07c; font-size: 16px')
      // تعريف userStore هنا
      const userStore = useUserStore()
      console.log('userStore.user.id: ', userStore.user.id)
      if (!userStore.user || !userStore.user.id) {
        this.$toast.add({
          severity: 'error',
          summary: 'User Error',
          detail: 'User ID is missing',
          life: 10000
        })
        return
      }
      axios
        .get(`/api/tasks/board_list/${userStore.user.id}`)
        .then((response) => {
          this.boards = response.data.boards
          console.log('Boards: ', response.data.boards)
          console.log('User', response.data.user)
          console.log('This Boards: ', this.boards)
          console.log(` %c${line} `, 'color: #1cd07c; font-size: 16px')
        })
        .catch((error) => {
          console.log('error', error)
          this.$toast.add({
            severity: 'error',
            summary: 'tasks List Error',
            detail: `Your Error Message Is${error.message}`,
            life: 10000
          })
          console.log(` %c${line} `, 'color: #1cd07c; font-size: 16px')
        })
    },
    /*
    // Add List
    submitAddListForm() {
      this.list_errors = []

      let formData = new FormData()

      // Title
      if (this.list_title == '') {
        this.$toast.add({
          severity: 'error',
          summary: 'Type List Title',
          detail: 'Your List Title is missing',
          life: 3000
        })
        this.list_errors.push('Type List Title')
      } else if (this.list_title !== '') {
        formData.append('title', this.list_title)
      }

      // All Is Good
      if (this.board_errors.length === 0) {
        axios
          .post('/api/tasks/list_create/', formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          })
          .then((response) => {
            console.log('Data Is Send To Django: ', response.data)
            this.$toast.add({
              severity: 'success',
              summary: 'List Done',
              detail: 'Good List Youtube Adding.',
              life: 3000
            })
            // this.boards.unshift(response.data), (this.board_title = '')

            // this.$router.push({ name: 'TaskDetails', params: { id: this.task.id } })
            if (this.user) {
              console.log('this.user: ', this.user)
              // this.user.posts_count += 1
            }
          })
          .catch((error) => {
            console.log('error', error)
            console.log('error.response.data', error.response.data)
            this.$toast.add({
              severity: 'error',
              summary: `Type List Error`,
              detail: `Error = ${error.response.data}`,
              life: 3000
            })
          })
      }
    },
    */
    // All List
    gatAllLists(board) {
      if (!board || !board.id) {
        this.$toast.add({
          severity: 'error',
          summary: 'Board Error',
          detail: 'Board ID is missing',
          life: 3000
        })
        return
      }
      let line = '📌'.repeat(30)
      console.log(` %c${line} `, 'color: #1cd07c; font-size: 16px')
      console.log(` %c Single Board`, 'color: #1cd07c; font-size: 16px')
      console.log('board: ', board)
      console.log('board.id: ', board.id)
      axios
        .get(`/api/tasks/list_list/${board.id}`)
        .then((response) => {
          this.selectedBoard = board
          this.lists = response.data.lists
          this.visibleBoardInfo = true
          console.log('Fetched lists: ', this.lists)
        })
        .catch((error) => {
          console.log('error', error)
          this.$toast.add({
            severity: 'error',
            summary: 'tasks List Error',
            detail: `Your Error Message Is${error.message}`,
            life: 10000
          })
        })
    }
    /*
    // Add Task
    submitAddTaskForm() {
      this.errors = []

      let formData = new FormData()
      // إضافة حالة السكربت (Task Status)
      if (this.task_status) {
        // استخدام الاسم النصي فقط لقائمة الحالة
        formData.append('task_status', this.task_status ? this.task_status.name : '')
      }
      // is_private
      formData.append('is_private', this.is_private ? 'true' : 'false')
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
      // إضافة عدد العناصر
      const list_of_item_number_num = this.list_of_item_number + 1
      formData.append('list_of_item_number', list_of_item_number_num)

      // All Is Good
      if (this.errors.length === 0) {
        axios
          .post('/api/tasks/task_create/', formData, {
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

            // this.$router.push({ name: 'TaskDetails', params: { id: this.task.id } })
            if (this.user) {
              console.log('this.user: ', this.user)
              // this.user.posts_count += 1
            }
          })
          .catch((error) => {
            console.log('error', error)
            console.log('error.response.data', error.response.data)
            this.$toast.add({
              severity: 'error',
              summary: `Type Script Error`,
              detail: `Error = ${error.response.data}`,
              life: 3000
            })
          })
      }
    },
    // All Tasks
    gatAllTasks() {
      axios
        .get('/api/tasks/task_list')
        .then((response) => {
          this.tasks = response.data
          console.log('response.data: ', response.data)
          console.log('this.tasks: ', this.tasks)
        })
        .catch((error) => {
          console.log('error', error)
          this.$toast.add({
            severity: 'error',
            summary: 'tasks List Error',
            detail: `Your Error Message Is${error.message}`,
            life: 10000
          })
        })
    }*/
  }
}
</script>

<style lang="scss">
.gg,
.grid_200 {
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-gap: 2rem;
}
.color-picker {
  width: 40px;
  height: 45px;
  padding: 0;
  border: none;
  outline: none;
  border-radius: 1rem;
  background: transparent;
}
</style>

<!--  
🎨 Design
💻 Code
✅ Done
🚧 Doing

📋 To_Do
📥 Archive
📋 Checklist
🏷️ Label

🗒️ Notes
📌 Subtask
📈 Progress
📅 Date
-->
