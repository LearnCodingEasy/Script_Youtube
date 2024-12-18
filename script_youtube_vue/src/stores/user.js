// Page [ script_youtube/script_youtube_vue/src/stores/user.js ]
import { defineStore } from 'pinia'
import axios from 'axios'
export const useUserStore = defineStore({
    id: 'user',
    state: () => ({
        user: {
            isAuthenticated: false, 
            id: null,
            name: null,
            surname: null,
            email: null,
            date_of_birth: null,
            access: null,
            refresh: null,
            script_count: null,
        }
    }),
    actions: {
        initStore() {
            if (localStorage.getItem('user.access')) {
                console.log('User has access!')
                this.user.isAuthenticated = true
                this.user.id = localStorage.getItem('user.id')
                this.user.name = localStorage.getItem('user.name')
                this.user.surname = localStorage.getItem('user.surname')
                this.user.email = localStorage.getItem('user.email')
                this.user.date_of_birth = localStorage.getItem('user.date_of_birth')
                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                this.refreshToken()
                this.user.script_count = localStorage.getItem('user.script_count')
            }
        },
        setToken(data) {
            console.log('setToken', data)
            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true
            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)

            console.log('user.access: ', localStorage.getItem('user.access'))
        },
        removeToken() {
            console.log('removeToken')
            this.user.refresh = null
            this.user.access = null
            this.user.isAuthenticated = false
            this.user.id = null
            this.user.name = null
            this.user.surname = null
            this.user.email = null
            this.user.date_of_birth = null
            this.user.script_count = null
            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.id', '')
            localStorage.setItem('user.name', '')
            localStorage.setItem('user.surname', '')
            localStorage.setItem('user.email', '')
            localStorage.setItem('user.date_of_birth', '')
            localStorage.setItem('user.script_count', '')
        },
        setUserInfo(user) {
            console.log('setUserInfo', user)
            this.user.id = user.id
            this.user.name = user.name
            this.user.surname = user.surname
            this.user.email = user.email
            this.user.date_of_birth = user.date_of_birth
            this.user.script_count = user.script_count
            localStorage.setItem('user.id', this.user.id)
            localStorage.setItem('user.name', this.user.name)
            localStorage.setItem('user.surname', this.user.surname)
            localStorage.setItem('user.email', this.user.email)
            localStorage.setItem('user.date_of_birth', this.user.date_of_birth)
            localStorage.setItem('user.script_count', this.user.script_count)

        },
        refreshToken() {
            axios.post('/api/refresh/', {
                refresh: this.user.refresh
            })
                .then((response) => {
                    this.user.access = response.data.access
                    localStorage.setItem('user.access', response.data.access)
                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                })
                .catch((error)=>{
                    console.log(error)
                    this.removeToken()
                })
        },
    }
})