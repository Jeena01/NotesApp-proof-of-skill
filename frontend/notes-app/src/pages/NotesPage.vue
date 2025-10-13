<template>
  <div>
    <Header />
    <div class="container">
      <NotesGrid :notes="notes" :deleteNote="deleteNote" />
      <AddNoteModal @add="addNote" />
    </div>
  </div>
</template>

<script setup>
import Header from '../components/Header.vue'
import NotesGrid from '../components/NotesGrid.vue'
import AddNoteModal from '../components/AddNoteModal.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const notes = ref([])
const api = axios.create({ baseURL: 'http://127.0.0.1:5000' })
api.interceptors.request.use(config => {
  const token = localStorage.getItem('token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

const fetchNotes = async () => {
  const res = await api.get('/notes')
  notes.value = res.data
}

const addNote = async (text) => {
  const res = await api.post('/notes', { text })
  notes.value.push(res.data)
}

const deleteNote = async (id) => {
  await api.delete(`/notes/${id}`)
  notes.value = notes.value.filter(n => n.id !== id)
}

onMounted(fetchNotes)
</script>