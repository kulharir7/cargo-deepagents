---
name: frontend-agent
description: "INVOKE THIS SKILL for frontend tasks. Triggers: 'UI', 'React', 'Vue', 'component', 'CSS', 'Tailwind'."
---

<oneliner>
Frontend developer for React, Vue, Tailwind with modern best practices.
</oneliner>

<setup>
## Frameworks
- React 18+ with Hooks
- Vue 3 with Composition API
- Tailwind CSS
- TypeScript

## Project Setup
`ash
# React
npm create vite@latest my-app -- --template react-ts

# Vue
npm create vue@latest my-app

# Tailwind
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
`
</setup>

<react>
`	sx
import { useState, useEffect } from "react";

interface Props {
  initialCount?: number;
  onCountChange?: (count: number) => void;
}

export function Counter({ initialCount = 0, onCountChange }: Props) {
  const [count, setCount] = useState(initialCount);
  
  useEffect(() => {
    onCountChange?.(count);
  }, [count, onCountChange]);
  
  return (
    <div className="flex flex-col items-center gap-4 p-6 bg-white rounded-lg shadow-md">
      <span className="text-3xl font-bold text-gray-800">{count}</span>
      <div className="flex gap-2">
        <button
          onClick={() => setCount(c => c - 1)}
          className="px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600"
        >
          Decrement
        </button>
        <button
          onClick={() => setCount(c => c + 1)}
          className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600"
        >
          Increment
        </button>
      </div>
    </div>
  );
}
`
</react>

<vue>
`ue
<script setup lang="ts">
import { ref, watch } from 'vue';

const props = defineProps<{
  initialCount?: number;
}>();

const count = ref(props.initialCount ?? 0);

watch(count, (newCount) => {
  emit('count-change', newCount);
});

const emit = defineEmits<{
  'count-change': [count: number];
}>();
</script>

<template>
  <div class="flex flex-col items-center gap-4 p-6 bg-white rounded-lg shadow-md">
    <span class="text-3xl font-bold text-gray-800">{{ count }}</span>
    <div class="flex gap-2">
      <button @click="count--" class="px-4 py-2 bg-red-500 text-white rounded">
        Decrement
      </button>
      <button @click="count++" class="px-4 py-2 bg-green-500 text-white rounded">
        Increment
      </button>
    </div>
  </div>
</template>
`
</vue>

<tailwind>
`html
<!-- Common Tailwind patterns -->
<!-- Card -->
<div className="p-6 max-w-sm mx-auto bg-white rounded-xl shadow-md">
  <h2 className="text-xl font-bold">Title</h2>
  <p className="text-gray-600">Description text</p>
</div>

<!-- Button -->
<button className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 focus:ring-2">
  Click me
</button>

<!-- Form -->
<input 
  className="border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
  placeholder="Enter text"
/>
`
</tailwind>

<tips>
1. Use functional components with hooks
2. Implement proper state management (Redux/Pinia)
3. Handle loading and error states
4. Optimize bundle size (lazy loading)
5. Add accessibility (aria-*)
6. Use TypeScript for type safety
</tips>

<triggers>
- 'frontend', 'React', 'Vue', 'component'
- 'CSS', 'Tailwind', 'UI', 'button'
- 'state', 'hooks', 'props', 'jsx', 'tsx'
</triggers>
