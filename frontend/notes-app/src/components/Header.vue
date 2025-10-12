<template>
  <header class="header">
    <h1 @click="$router.push('/notes')">📝 NotesApp</h1>
    <nav>
      <button v-if="token" @click="logout">Logout</button>
    </nav>
  </header>
</template>

<script setup>
const token = localStorage.getItem('token')
const logout = () => {
  localStorage.removeItem('token')
  window.location.href = '/login'
}
</script>