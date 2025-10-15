<template>
  <div class="min-h-screen bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100 transition-colors duration-300">
    <Header />
    <main class="max-w-6xl mx-auto p-4">
      <RouterView />
    </main>
  </div>
</template>

<script setup>
import Header from './components/Header.vue'
</script>
