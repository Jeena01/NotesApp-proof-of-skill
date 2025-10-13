<template>
  <div class="flex flex-col items-center justify-center min-h-[80vh]">
    <div class="bg-white dark:bg-gray-800 p-8 rounded-2xl shadow-lg w-full max-w-md">
      <h2 class="text-2xl font-bold text-center mb-6 text-emerald-500">
        Create an Account
      </h2>

      <form @submit.prevent="register">
        <!-- Username -->
        <input
          v-model="username"
          placeholder="Username"
          class="w-full mb-2 px-3 py-2 border rounded-lg bg-gray-50 dark:bg-gray-900 dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-emerald-500"
        />
        <div v-if="v$.username.$error" class="text-red-500 text-sm mb-2">
          Username required
        </div>

        <!-- Password -->
        <input
          type="password"
          v-model="password"
          placeholder="Password"
          class="w-full mb-2 px-3 py-2 border rounded-lg bg-gray-50 dark:bg-gray-900 dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-emerald-500"
        />
        <div v-if="v$.password.$error" class="text-red-500 text-sm mb-2">
          Min 6 characters
        </div>

        <!-- Confirm Password -->
        <input
          type="password"
          v-model="confirm"
          placeholder="Confirm Password"
          class="w-full mb-2 px-3 py-2 border rounded-lg bg-gray-50 dark:bg-gray-900 dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-emerald-500"
        />
        <div v-if="password !== confirm" class="text-red-500 text-sm mb-4">
          Passwords don’t match
        </div>

        <button
          type="submit"
          :disabled="v$.$invalid || password !== confirm"
          class="w-full bg-emerald-500 hover:bg-emerald-600 text-white font-semibold py-2 rounded-lg transition disabled:opacity-50"
        >
          Register
        </button>
      </form>

      <p class="mt-4 text-sm text-center text-gray-600 dark:text-gray-400">
        Already have an account?
        <router-link to="/login" class="text-emerald-500 hover:underline">
          Login
        </router-link>
      </p>
    </div>
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
  v$.value.$touch() // Mark all as touched so validation errors show

  if (v$.value.$invalid || password.value !== confirm.value) return

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
