<template>
  <div class="flex flex-col items-center justify-center min-h-[80vh]">
    <div class="bg-white  dark:bg-gray-800 p-8 rounded-2xl shadow-lg w-full max-w-md">



    <h2 class="text-2xl font-bold text-center mb-6 text-emerald-500">Login</h2>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="Username" class="w-full mb-2 px-3 py-2 border rounded-lg bg-gray-50 dark:bg-gray-900 dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-emerald-500"
        />
      <input type="password" v-model="password" placeholder="Password" class="w-full mb-2 px-3 py-2 border rounded-lg bg-gray-50 dark:bg-gray-900 dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-emerald-500"
         />
      <button
      :disabled="!username.trim() || !password.trim()"
       class="w-full bg-emerald-500 hover:bg-emerald-600 text-white font-semibold py-2 rounded-lg transition disabled:opacity-50"
      >Login</button>
    </form>
    <p class="mt-4 text-sm text-center text-gray-600 dark:text-gray-400">Don’t have an account? <a href="/register" class="text-emerald-500 hover:underline">Register</a></p>
    
</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

import useVuelidate from '@vuelidate/core'

const username = ref('')
const password = ref('')

const login = async () => {
  try {
    const res = await axios.post('http://127.0.0.1:5000/login', {
      username: username.value,
      password: password.value
    })
    localStorage.setItem('token', res.data.token)
    window.location.href = '/notes'
  } catch {
    alert('Invalid credentials!')
  }
}
</script>
