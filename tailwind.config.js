/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html"],
  theme: {
    extend: {
      colors: {
        cream: {
          DEFAULT: "#F4EEE3",
          soft: "#FBF8F2",
        },
        ink: {
          DEFAULT: "#181A17",
          soft: "#24261F",
        },
        pine: {
          DEFAULT: "#2E5951",
          dark: "#20403A",
          light: "#3E7269",
        },
        sand: {
          DEFAULT: "#B08A5A",
        },
        stone: {
          DEFAULT: "#5B5F55",
          light: "#8C8F82",
        },
      },
      fontFamily: {
        display: ["Fraunces", "serif"],
        sans: ["Manrope", "sans-serif"],
        tifinagh: ["'Noto Sans Tifinagh'", "sans-serif"],
        wordmark: ["'Cormorant Garamond'", "ui-serif", "Georgia", "serif"],
      },
      letterSpacing: {
        widest2: "0.28em",
      },
    },
  },
  future: {
    hoverOnlyWhenSupported: true,
  },
  plugins: [],
};
