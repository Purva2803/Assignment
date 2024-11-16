import { ref } from 'vue'

export const useThemeStore = () => {
  const isDark = ref(true)

  const toggleTheme = () => {
    isDark.value = !isDark.value
    document.body.classList.toggle('light-mode')
  }

  return {
    isDark,
    toggleTheme,
  }
}
