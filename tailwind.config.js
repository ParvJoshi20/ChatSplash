/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {
      colors: {
        chat_back: { 50: '#78e6e0' },
        chat_dark: { 50: '#040720' },
        chat_sidebar: { 50: '#faf0e6' },
        chat_dark1: { 50: '#342D7E' },
        chat_dark2: { 50: '#483D8B' }, 
        chat_beige: { 50: '#f5f5dc' },
        chat_beige1: { 50: '#EED9C4' },
        chat_box: { 50: '#27d2ca'}
      }
    },
  },
  plugins: [],
}

