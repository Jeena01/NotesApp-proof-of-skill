<template>
  <div class="form-container">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="Username" />
      <input type="password" v-model="password" placeholder="Password" />
      <button>Login</button>
    </form>
    <p>Don’t have an account? <a href="/register">Register</a></p>
    

  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

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
