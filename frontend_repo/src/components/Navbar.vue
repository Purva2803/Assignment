<script setup lang="ts">
import { ref } from 'vue'
import { useThemeStore } from '../stores/theme'

const showToast = ref(false)
const toastMessage = ref('')
const { isDark, toggleTheme } = useThemeStore()

const handleNavClick = (item: string) => {
  toastMessage.value = `${item} feature is just for demo purposes`
  showToast.value = true
  setTimeout(() => {
    showToast.value = false
  }, 3000)
}
</script>

<template>
  <nav class="navbar">
    <div class="nav-content">
      <div class="nav-brand">TMDB</div>
      <div class="nav-items">
        <div class="nav-item" @click="handleNavClick('Movies')">Movies</div>
        <div class="nav-item" @click="handleNavClick('TV Shows')">TV Shows</div>
        <div class="nav-item" @click="handleNavClick('People')">People</div>
        <div class="nav-item" @click="handleNavClick('More')">More</div>
      </div>
    </div>
    <div v-if="showToast" class="toast">
      {{ toastMessage }}
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  background: #032541;
  padding: 16px 0;
  position: relative;
}

.nav-content {
  max-width: 1300px;
  margin: 0 auto;
  padding: 0 40px;
  display: flex;
  align-items: center;
}

.nav-brand {
  color: #01b4e4;
  font-size: 1.5rem;
  font-weight: bold;
  margin-right: 40px;
}

.nav-items {
  display: flex;
  gap: 24px;
}

.nav-item {
  color: white;
  cursor: pointer;
  font-weight: 600;
  transition: color 0.3s ease;
}

.nav-item:hover {
  color: #01b4e4;
}

.toast {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background: #032541;
  color: white;
  padding: 12px 24px;
  border-radius: 4px;
  z-index: 1000;
  animation: slideIn 0.3s ease;
}

@keyframes slideIn {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@media (max-width: 768px) {
  .nav-content {
    flex-direction: column;
    gap: 16px;
    text-align: center;
  }

  .nav-items {
    flex-wrap: wrap;
    justify-content: center;
  }
}
</style>
