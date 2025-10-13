<template>
  <draggable
    v-model="localNotes"
    item-key="id"
    class="note-grid"
    animation="200"
  >
    <template #item="{ element }">
      <div class="note-card">
        <p>{{ element.text }}</p>
        <button @click="deleteNote(element.id)">✕</button>
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
