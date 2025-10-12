<template>
  <div class="app">
    <h1>📝 Sleek Notes</h1>

    <!-- Login/Register Section -->
    <div v-if="!token" class="auth">
      <input v-model="username" placeholder="Username" />
      <input v-model="password" type="password" placeholder="Password" />
      <button @click="login">Login</button>
      <button @click="register">Register</button>
      <p>{{ message }}</p>
    </div>

    <!-- Notes Section -->
    <div v-else>
      <div class="input-row">
        <input v-model="newNote" @keyup.enter="addNote" placeholder="Add a note" />
        <button @click="addNote">Add</button>
      </div>

      <draggable v-model="notes" item-key="id" class="grid" @end="onReorder">
        <template #item="{ element }">
          <div class="note-card">
            <p>{{ element.text }}</p>
            <button @click="deleteNote(element.id)">🗑️</button>
          </div>
        </template>
      </draggable>

      <button class="logout" @click="logout">Logout</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import draggable from 'vuedraggable'

const username = ref('')
const password = ref('')
const token = ref(localStorage.getItem('token') || '')
const newNote = ref('')
const notes = ref([])
const message = ref('')

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000',
})
api.interceptors.request.use(config => {
  if (token.value) config.headers.Authorization = `Bearer ${token.value}`
  return config
})

const fetchNotes = async () => {
  const res = await api.get('/notes')
  notes.value = res.data
}

const login = async () => {
  try {
    const res = await api.post('/login', { username: username.value, password: password.value })
    token.value = res.data.token
    localStorage.setItem('token', token.value)
    fetchNotes()
  } catch {
    message.value = 'Login failed'
  }
}

const register = async () => {
  try {
    await api.post('/register', { username: username.value, password: password.value })
    message.value = 'User registered! Now login.'
  } catch {
    message.value = 'Registration failed'
  }
}

const addNote = async () => {
  if (!newNote.value) return
  const res = await api.post('/notes', { text: newNote.value })
  notes.value.push(res.data)
  newNote.value = ''
}

const deleteNote = async (id) => {
  await api.delete(`/notes/${id}`)
  notes.value = notes.value.filter(n => n.id !== id)
}

const logout = () => {
  token.value = ''
  localStorage.removeItem('token')
  notes.value = []
}

const onReorder = () => {
  // You can optionally send the new order to backend
  console.log('New order:', notes.value)
}

onMounted(() => {
  if (token.value) fetchNotes()
})
</script>

<style scoped>
.app {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: "Inter", sans-serif;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
}

.auth input {
  display: block;
  width: 100%;
  margin-bottom: 10px;
  padding: 8px;
}

.auth button {
  margin-right: 10px;
}

.input-row {
  display: flex;
  margin-bottom: 20px;
}

.input-row input {
  flex: 1;
  padding: 10px;
}

.input-row button {
  padding: 10px 15px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 15px;
}

.note-card {
  background: #f5f5f5;
  padding: 15px;
  border-radius: 10px;
  min-height: 100px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  cursor: grab;
  transition: transform 0.15s ease;
}

.note-card:hover {
  transform: scale(1.03);
}

.note-card p {
  margin: 0;
  word-wrap: break-word;
}

.note-card button {
  align-self: flex-end;
  background: none;
  border: none;
  cursor: pointer;
}

.logout {
  margin-top: 20px;
}
</style>
