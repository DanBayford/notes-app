/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./templates/**/*.svg",
    "./frontend/inputs.css",
  ],
  // darkMode: "selector",
  // screens: {
  //   sm: "640px", // ≥640px
  //   md: "768px", // ≥768px
  //   lg: "1024px", // ≥1024px
  //   xl: "1280px", // ≥1280px
  //   "2xl": "1536px", // ≥1536px
  // },
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter", "sans-serif"],
        serif: ["NotoSerif", "serif"],
        mono: ["SourceCodePro", "monospace"],
      },
      colors: {
        blue: {
          50: "#ebf1ff",
          500: "#335cff",
          700: "#2547d0",
        },
        green: {
          100: "#d1fbe9",
          500: "#21c16b",
        },
        neutral: {
          0: "#ffffff",
          50: "#f5f7fa",
          100: "#f3f5f8",
          200: "#e0e4ea",
          300: "#cacfd8",
          400: "#99a0ae",
          500: "#717784",
          600: "#525866",
          700: "#2b303b",
          800: "#232530",
          900: "#191b25",
          950: "#0e121b",
        },
        red: {
          100: "#ffd5d8",
          500: "#fb3748",
        },
      },
    },
  },
  plugins: [],
};
