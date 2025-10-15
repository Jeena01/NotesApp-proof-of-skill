<template>
  <div
    class="min-h-screen bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100 transition-colors duration-300"
  >
    <Header />

    <main class="px-4 sm:px-8 md:px-12 py-8 max-w-6xl mx-auto">
      <RouterView />
    </main>
  </div>
</template>

<script setup>
import Header from './components/Header.vue'
</script>

<style>
/* Optional: smooth fade transitions for page changes */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
