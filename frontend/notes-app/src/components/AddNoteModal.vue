<template>
  <div>
    <div
      class="floating-btn"
      v-draggable
      @click="toggleModal"
    >+</div>

    <div v-if="showModal" class="modal-backdrop" @click.self="toggleModal">
      <div class="modal">
        <textarea v-model="noteText" placeholder="Write your note..." />
        <button @click="submitNote">Add Note</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const emit = defineEmits(['add'])
const showModal = ref(false)
const noteText = ref('')

const toggleModal = () => showModal.value = !showModal.value
const submitNote = () => {
  if (!noteText.value.trim()) return
  emit('add', noteText.value)
  noteText.value = ''
  showModal.value = false
}
</script>