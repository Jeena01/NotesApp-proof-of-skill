import colors from "tailwindcss/dist/colors.mjs"
/** @type {import('tailwindcss').Config} */

export default {
  darkMode: 'class',
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors:{
        ...colors
      }
    },
  },
  plugins: [],
  safelist: [
  'dark:bg-gray-800',
  'dark:text-white',],
}
