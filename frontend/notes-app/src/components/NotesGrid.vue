<template>
  <draggable v-model="notes" item-key="id" class="note-grid" animation="200">
    <template #item="{ element }">
      <div class="note-card">
        <p>{{ element.text }}</p>
        <button @click="deleteNote(element.id)">✕</button>
      </div>
    </template>
  </draggable>
</template>

<script setup>
import { defineProps } from 'vue'
import draggable from 'vuedraggable'

defineProps({
  notes: Array,
  deleteNote: Function
})
</script>