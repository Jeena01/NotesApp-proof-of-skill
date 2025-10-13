<template>
  <div>
    <!-- Floating draggable add button -->
    <div
      ref="buttonRef"
      class="fixed bottom-6 right-6 bg-emerald-500 text-white w-14 h-14 rounded-full flex items-center justify-center text-4xl cursor-pointer shadow-lg hover:bg-emerald-600 active:scale-95 transition-all select-none"
      @mousedown="startDrag"
      @touchstart.prevent="startDrag"
      @click="toggleModal"
    >
      +
    </div>

    <!-- Modal -->
    <div
      v-if="showModal"
      class="fixed inset-0 bg-black/40 flex items-center justify-center z-50"
      @click.self="toggleModal"
    >
      <div
        class="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-xl w-[90%] max-w-md"
      >
        <h3 class="text-lg font-semibold mb-4 text-emerald-600 dark:text-emerald-400">
          Add a Note
        </h3>
        <textarea
          v-model="noteText"
          placeholder="Write your note..."
          class="w-full h-32 border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-emerald-500 bg-gray-50 dark:bg-gray-900 dark:text-gray-100 resize-none"
        />
        <div class="flex justify-end mt-4 gap-3">
          <button
            @click="toggleModal"
            class="px-4 py-2 bg-gray-200 dark:bg-gray-700 rounded-lg hover:bg-gray-300 dark:hover:bg-gray-600 transition"
          >
            Cancel
          </button>
          <button
            @click="submitNote"
            class="px-4 py-2 bg-emerald-500 text-white rounded-lg hover:bg-emerald-600 transition"
          >
            Add
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const emit = defineEmits(['add'])
const showModal = ref(false)
const noteText = ref('')

const toggleModal = () => (showModal.value = !showModal.value)
const submitNote = () => {
  if (!noteText.value.trim()) return
  emit('add', noteText.value)
  noteText.value = ''
  showModal.value = false
}

/* ---- Simple draggable logic ---- */
const buttonRef = ref(null)
let isDragging = false
let offsetX = 0
let offsetY = 0

const startDrag = (e) => {
  e.stopPropagation()
  isDragging = true
  const button = buttonRef.value
  const rect = button.getBoundingClientRect()
  const event = e.touches ? e.touches[0] : e
  offsetX = event.clientX - rect.left
  offsetY = event.clientY - rect.top
  document.addEventListener('mousemove', onDrag)
  document.addEventListener('mouseup', stopDrag)
  document.addEventListener('touchmove', onDrag)
  document.addEventListener('touchend', stopDrag)
}

const onDrag = (e) => {
  if (!isDragging) return
  const event = e.touches ? e.touches[0] : e
  const button = buttonRef.value
  const x = event.clientX - offsetX
  const y = event.clientY - offsetY
  button.style.left = `${x}px`
  button.style.top = `${y}px`
  button.style.bottom = 'auto'
  button.style.right = 'auto'
}

const stopDrag = () => {
  isDragging = false
  document.removeEventListener('mousemove', onDrag)
  document.removeEventListener('mouseup', stopDrag)
  document.removeEventListener('touchmove', onDrag)
  document.removeEventListener('touchend', stopDrag)
}

onMounted(() => {
  const button = buttonRef.value
  button.style.position = 'fixed'
  button.style.bottom = '1.5rem'
  button.style.right = '1.5rem'
})
</script>
