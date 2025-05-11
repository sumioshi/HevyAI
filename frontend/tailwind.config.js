/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'hevy-blue': '#4F46E5',
        'hevy-dark': '#1F2937',
        'hevy-light': '#F9FAFB',
      },
    },
  },
  plugins: [],
}