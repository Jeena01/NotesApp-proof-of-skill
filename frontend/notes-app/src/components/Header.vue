<template>
  <header class="bg-white dark:bg-gray-800 shadow-md sticky top-0 z-50">
    <div class="max-w-6xl mx-auto flex items-center justify-between px-6 py-4">
      
      <!-- Logo -->
      <h1
        @click="$router.push('/notes')"
        class="text-2xl font-bold text-emerald-600 dark:text-red-400 cursor-pointer select-none hover:scale-105 transition-transform"
      >
        📝 Notes App
      </h1>

      <!-- Controls -->
      <nav class="flex items-center gap-3">
        <label class="flex items-center cursor-pointer">
          <input
            type="checkbox"
            class="sr-only"
            v-model="isDark"
          />
          <div
            class="w-12 h-6 bg-gray-300 dark:bg-gray-600 rounded-full p-1 transition-all"
          >
            <div
              class="w-4 h-4 bg-white rounded-full shadow transform transition-transform duration-300"
              :class="isDark ? 'translate-x-6' : 'translate-x-0'"
            ></div>
          </div>
          <span class="ml-2 text-sm text-gray-700 dark:text-gray-300 select-none">
            {{ isDark ? 'Dark' : 'Light' }}
          </span>
        </label>

        <!-- Refresh -->
        <button
          v-if="token"
          @click="$emit('refresh')"
          class="bg-emerald-500 hover:bg-emerald-600 text-white px-4 py-2 rounded-lg shadow transition-colors duration-200"
        >
          Refresh
        </button>

        <!-- Logout -->
        <button
          v-if="token"
          @click="logout"
          class="bg-emerald-500 hover:bg-emerald-600 text-white px-4 py-2 rounded-lg shadow transition-colors duration-200"
        >
          Logout
        </button>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'

const token = localStorage.getItem('token')
const isDark = ref(false)

// Load theme from localStorage
onMounted(() => {
  const savedTheme = localStorage.getItem('theme')
  isDark.value = savedTheme === 'dark'
  applyTheme()
})

// Watch for changes
watch(isDark, (val) => {
  console.log(isDark)
  localStorage.setItem('theme', val ? 'dark' : 'light')
  applyTheme()
})

// Apply theme by toggling the `dark` class
const applyTheme = () => {
  if (isDark.value) {
    document.documentElement.classList.add('dark')
  } else {
    document.documentElement.classList.remove('dark')
  }
}


const logout = () => {
  localStorage.removeItem('token')
  window.location.href = '/login'
}
</script>
