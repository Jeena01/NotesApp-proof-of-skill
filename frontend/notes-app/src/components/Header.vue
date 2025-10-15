<template>
  <header class="bg-white dark:bg-gray-800 shadow-md sticky top-0 z-50">
    <div class="max-w-6xl mx-auto flex items-center justify-between px-6 py-4">
      
      <h1
        @click="$router.push('/notes')"
        class="text-2xl font-bold text-emerald-600 dark:text-emerald-400 cursor-pointer select-none hover:scale-105 transition-transform"
      >
        📝 Notes App
      </h1>

      <nav>
        <button
          v-if="token"
          @click="$emit('refresh')"
          class="m-2 bg-emerald-500 hover:bg-emerald-600 text-white px-4 py-2 rounded-lg shadow transition-colors duration-200"
        >
          Refresh
        </button>
        <button
          v-if="token"
          @click="logout"
          class="m-2 bg-emerald-500 hover:bg-emerald-600 text-white px-4 py-2 rounded-lg shadow transition-colors duration-200"
        >
          Logout
        </button>
      </nav>
    </div>
  </header>
</template>

<script setup>
const token = localStorage.getItem('token')

const logout = () => {
  localStorage.removeItem('token')
  window.location.href = '/login'
}
</script>
