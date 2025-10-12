<template>
  <div class="form-container">
    <h2>Create an Account</h2>
    <form @submit.prevent="register">
      <input v-model="username" placeholder="Username" />
      <div v-if="$v.username.$error" class="error">Username required</div>

      <input type="password" v-model="password" placeholder="Password" />
      <div v-if="$v.password.$error" class="error">Min 6 characters</div>

      <input type="password" v-model="confirm" placeholder="Confirm Password" />
      <div v-if="password !== confirm" class="error">Passwords don’t match</div>

      <button :disabled="$v.$invalid || password !== confirm">Register</button>
    </form>
    <p>Already have an account? <a href="/login">Login</a></p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import useVuelidate from '@vuelidate/core'
import { required, minLength } from '@vuelidate/validators'

const username = ref('')
const password = ref('')
const confirm = ref('')

const rules = {
  username: { required },
  password: { required, minLength: minLength(6) },
  confirm: { required }
}

const v$ = useVuelidate(rules, { username, password, confirm })

const register = async () => {
  if (v$.$invalid || password.value !== confirm.value) return
  try {
    await axios.post('http://127.0.0.1:5000/register', {
      username: username.value,
      password: password.value
    })
    window.location.href = '/login'
  } catch {
    alert('Registration failed!')
  }
}
</script>
