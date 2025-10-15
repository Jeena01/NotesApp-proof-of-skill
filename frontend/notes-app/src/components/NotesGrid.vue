<template>
  <draggable
    v-model="localNotes"
    item-key="id"
    class="grid gap-4 grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4"
    animation="200"
  >
    <template #item="{ element }">
      <div
        class="bg-white dark:bg-gray-800 p-4 rounded-xl shadow hover:shadow-lg transition-shadow duration-200 relative"
      >
        <p class="text-gray-900 dark:text-gray-100 break-words">{{ element.text }}</p>
        <button
          @click="deleteNote(element.id)"
          class="absolute top-2 right-2 text-gray-400 hover:text-red-500 transition-colors"
        >
          ✕
        </button>
      </div>
    </template>
  </draggable>
</template>

<script setup>
import { ref, watch } from 'vue'
import draggable from 'vuedraggable'

// Props
const props = defineProps({
  modelValue: Array,      // receive notes
  deleteNote: Function
})

// Emits
const emit = defineEmits(['update:modelValue'])

// Local reactive copy
const localNotes = ref([...props.modelValue])

// Sync parent → child
watch(
  () => props.modelValue,
  (newVal) => (localNotes.value = [...newVal])
)

// Sync child → parent
watch(localNotes, (newVal) => emit('update:modelValue', newVal), { deep: true })
</script>
