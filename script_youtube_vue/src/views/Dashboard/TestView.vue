<template><div class="Component-Name"></div></template>

<script>
export default { name: 'TestView' }
// deleteScript(scriptId) {
//   // تأكيد عملية الحذف من المستخدم
//   if (confirm('Are you sure you want to delete this script?')) {
//     axios
//       .delete(`/api/scripts/script_list/script_delete/${scriptId}/`)
//       .then((response) => {
//         if (response.data.message == `script deleted`) {
//           console.log(response.data)
//           console.log('scriptId: ', scriptId)
//           this.$toast.add({
//             severity: 'error',
//             summary: 'Script Deleted',
//             detail: 'Script Youtube Deleted.',
//             life: 3000
//           })
//           this.scripts = this.scripts.filter((script) => script.id !== scriptId)
//         }
//       })
//       .catch((error) => {
//         console.error('Error deleting script:', error)

//         this.$toast.add({
//           severity: 'error',
//           summary: 'Script List Error',
//           detail: `Your Error ${error}`,
//           life: 3000
//         })
//       })
//   }
// }
</script>

<style lang="scss" scoped></style>

<!--  
<form
            class="form_login w-3/12"
            v-on:submit.prevent="submitAddTaskForm"
            enctype="multipart/form-data "
          >
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-7 shadow-lg">
              <div class="title border p-5 col-span-1 md:col-span-2 rounded">
                <h2 dir="auto" class="mb-5 text-1xl font-bold">[ العنوان ]</h2>
                <div class="card">
                  <prime_input_text v-model="title" editorStyle="height: 50px" class="w-full" />
                </div>
              </div>
              

              <div class="card flex justify-center">
                <prime_toggle_button
                  v-model="is_private"
                  onLabel="Locked"
                  offLabel="Unlocked"
                  onIcon="pi pi-lock"
                  offIcon="pi pi-lock-open"
                  class="w-36"
                  aria-label="Do you confirm"
                />
              </div>
              <div class="card flex justify-center">
                <prime_list_box
                  v-model="task_status"
                  :options="statusOptions"
                  optionLabel="name"
                  checkmark
                  :highlightOnSelect="false"
                  class="w-full md:w-56"
                />
              </div>

              <div class="send">
                <prime_button
                  @click="submitAddTaskForm"
                  label="Submit"
                  severity="success"
                  icon="pi pi-send"
                  iconPos="right"
                ></prime_button>
              </div>
            </div>
          </form>
-->
