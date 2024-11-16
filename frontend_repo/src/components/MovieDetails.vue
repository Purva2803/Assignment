<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import '../assets/theme.css'
interface Movie {
  Title: string
  Year: string
  Rated: string
  Runtime: string
  Genre: string
  Director: string
  Writer: string
  Actors: string
  Plot: string
  Poster: string
  imdbRating: string
  // New fields
  Budget: string
  Revenue: string
  Status: string
  OriginalLanguage: string
  Keywords: string[]
  Reviews: {
    author: string
    content: string
    rating: number
  }[]
}
const movie = ref<Movie | null>(null)
const loading = ref(true)

onMounted(async () => {
  try {
    const response = await axios.get('http://www.omdbapi.com/?i=tt3896198&apikey=d2132124')
    movie.value = response.data
  } catch (error) {
    console.error('Error fetching movie data:', error)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div v-if="loading" class="loading">Loading...</div>
  <div v-else-if="movie" class="movie-container">
    <div class="hero-section" :style="{ backgroundImage: `url(${movie.Poster})` }">
      <div class="overlay">
        <div class="content-wrapper">
          <!-- Existing poster and basic info -->
          <div class="poster">
            <img :src="movie.Poster" :alt="movie.Title" />
          </div>
          <div class="movie-info">
            <h1 class="movie-title">{{ movie.Title }} ({{ movie.Year }})</h1>
            <div class="meta-info">
              <span class="rating">{{ movie.Rated }}</span>
              <span class="runtime">{{ movie.Runtime }}</span>
              <span class="genre">{{ movie.Genre }}</span>
            </div>
            <div class="score">
              <div class="rating-circle">
                <span class="rating-number">{{ movie.imdbRating }}</span>
                <span class="rating-max">/10</span>
              </div>
              <div class="user-score">
                <div>User</div>
                <div>Score</div>
              </div>
            </div>
            <div class="actions">
              <button class="action-btn">Like</button>
              <button class="action-btn">Add to List</button>
              <button class="action-btn">★ Rate</button>
              <button class="action-btn">▶ Play Trailer</button>
            </div>
            <div class="tagline">Obviously.</div>
            <div class="overview">
              <h3>Overview</h3>
              <p>{{ movie.Plot }}</p>
            </div>
            <div class="crew-list">
              <div class="crew-item">
                <strong>{{ movie.Director }}</strong>
                <span>Director</span>
              </div>
              <div class="crew-item">
                <strong>{{ movie.Writer }}</strong>
                <span>Screenplay</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="content-wrapper main-content">
      <div class="left-column">
        <section class="cast-section">
          <h3 class="section-title">Top Billed Cast</h3>
          <div class="cast-list">
            <div class="cast-item" v-for="actor in movie.Actors.split(',')" :key="actor">
              <div class="cast-avatar">
                <img
                  src="https://www.themoviedb.org/assets/2/v4/glyphicons/basic/glyphicons-basic-4-user-grey-d8fe957375e70239d6abdd549fd7568c89281b2179b5f4470e2e12895792dfa5.svg"
                  :alt="actor"
                />
              </div>
              <div class="cast-info">
                <div class="cast-name">{{ actor.trim() }}</div>
                <div class="cast-character">Character Name</div>
              </div>
            </div>
          </div>
          <div class="full-cast-btn">
            <button class="secondary-btn">Full Cast & Crew</button>
          </div>
        </section>

        <section class="social-section">
          <h3 class="section-title">Social</h3>
          <div class="reviews">
            <div class="review-card">
              <div class="review-header">
                <div class="review-avatar"></div>
                <div class="review-meta">
                  <h4>A review by John Doe</h4>
                  <div class="review-rating">★★★★☆</div>
                </div>
              </div>
              <p class="review-content">
                Written by John Doe on May 5, 2017 Lorem ipsum dolor sit amet, consectetur
                adipiscing elit.
              </p>
            </div>
          </div>
        </section>
      </div>

      <div class="right-column">
        <div class="info-block">
          <h4>Status</h4>
          <p>Released</p>
        </div>
        <div class="info-block">
          <h4>Original Language</h4>
          <p>English</p>
        </div>
        <div class="info-block">
          <h4>Budget</h4>
          <p>$200,000,000.00</p>
        </div>
        <div class="info-block">
          <h4>Revenue</h4>
          <p>$863,756,051.00</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.movie-container {
  min-height: 100vh;
  background-color: var(--bg-primary);
  color: var(--text-primary);
}

.section-title {
  font-size: 1.8rem;
  font-weight: var(--font-weight-bold);
  margin-bottom: 20px;
  color: var(--accent-color);
}

.hero-section {
  position: relative;
  min-height: 600px;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.overlay {
  background: var(--overlay-gradient);
  min-height: 600px;
  padding: 60px 0;
}

.content-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px;
  display: flex;
  gap: 50px;
}

.poster {
  flex-shrink: 0;
  width: 300px;
}

.poster img {
  width: 100%;
  border-radius: 12px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
}

.movie-info {
  flex-grow: 1;
}

.movie-title {
  font-size: 2.5rem;
  font-weight: var(--font-weight-bold);
  margin-bottom: 20px;
}

.meta-info {
  margin: 20px 0;
  display: flex;
  gap: 20px;
  font-size: 1rem;
  opacity: 0.8;
}

.score {
  margin: 30px 0;
  display: flex;
  align-items: center;
  gap: 15px;
}

.rating-circle {
  background: var(--bg-secondary);
  width: 80px;
  height: 80px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: row;
  border: 4px solid var(--accent-color);
}

.rating-number {
  font-size: 1.4rem;
  font-weight: var(--font-weight-bold);
}

.rating-max {
  font-size: 0.9rem;
  opacity: 0.8;
}

.actions {
  display: flex;
  gap: 20px;
  margin: 30px 0;
}

.action-btn {
  padding: 10px 20px;
  border-radius: 6px;
  border: none;
  background: var(--bg-secondary);
  color: var(--text-primary);
  cursor: pointer;
  transition: background 0.3s ease;
  font-size: 1rem;
  font-weight: var(--font-weight-medium);
}

.action-btn:hover {
  background: var(--accent-color);
}

.overview {
  margin: 40px 0;
}

.overview h3 {
  font-size: 1.6rem;
  margin-bottom: 15px;
  font-weight: var(--font-weight-bold);
}

.overview p {
  font-size: 1.1rem;
  line-height: 1.6;
}

.credits {
  margin-top: 30px;
}

.credit-item {
  margin: 15px 0;
  opacity: 0.9;
}

@media (max-width: 768px) {
  .content-wrapper {
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 30px;
  }

  .poster {
    width: 200px;
  }

  .actions {
    justify-content: center;
  }

  .score {
    justify-content: center;
  }

  .meta-info {
    justify-content: center;
    flex-wrap: wrap;
  }
}

.credits h3 {
  font-size: 1.6rem;
  margin-bottom: 25px;
  font-weight: var(--font-weight-bold);
}

.cast-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 25px;
  margin-bottom: 50px;
}

.cast-item {
  display: flex;
  gap: 15px;
  background: var(--card-bg);
  padding: 15px;
  border-radius: 10px;
  transition: transform 0.2s ease;
}

.cast-item:hover {
  transform: translateY(-3px);
}

.cast-avatar {
  width: 70px;
  height: 70px;
  border-radius: 10px;
  overflow: hidden;
  background: var(--bg-secondary);
}

.cast-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.cast-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.cast-name {
  font-weight: var(--font-weight-bold);
  margin-bottom: 6px;
  font-size: 1.1rem;
}

.cast-character {
  font-size: 0.95rem;
  opacity: 0.7;
}

.credits-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 35px;
  margin-top: 40px;
  padding-top: 40px;
  border-top: 1px solid var(--border-color);
}

.credit-column h4 {
  font-size: 1.2rem;
  margin-bottom: 15px;
  color: var(--accent-color);
  font-weight: var(--font-weight-bold);
}

.credit-column p {
  line-height: 1.7;
  opacity: 0.9;
  font-size: 1rem;
}

.main-content {
  display: grid;
  grid-template-columns: 3fr 1fr;
  gap: 50px;
  padding-top: 40px;
  background: var(--bg-primary);
}

.tagline {
  font-style: italic;
  opacity: 0.7;
  margin: 15px 0;
  font-size: 1.1rem;
}

.crew-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 25px;
  margin-top: 30px;
}

.crew-item {
  display: flex;
  flex-direction: column;
}

.crew-item strong {
  margin-bottom: 6px;
  font-size: 1.1rem;
  font-weight: var(--font-weight-bold);
}

.crew-item span {
  opacity: 0.7;
  font-size: 0.95rem;
}

.social-section {
  margin-top: 50px;
}

.review-card {
  background: var(--card-bg);
  border-radius: 12px;
  padding: 25px;
  margin: 25px 0;
}

.review-header {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}

.review-avatar {
  width: 50px;
  height: 50px;
  border-radius: 25px;
  background: var(--bg-secondary);
}

.review-meta h4 {
  margin: 0 0 8px 0;
  font-size: 1.2rem;
  font-weight: var(--font-weight-bold);
}

.right-column .info-block {
  margin-bottom: 30px;
}

.info-block h4 {
  color: var(--accent-color);
  margin-bottom: 10px;
  font-size: 1.1rem;
  font-weight: var(--font-weight-bold);
}

.info-block p {
  font-size: 1rem;
  line-height: 1.6;
}

.secondary-btn {
  background: transparent;
  border: 2px solid var(--accent-color);
  color: var(--accent-color);
  padding: 10px 20px;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 1rem;
  font-weight: var(--font-weight-medium);
}

.secondary-btn:hover {
  background: var(--accent-color);
  color: var(--text-primary);
}

@media (max-width: 768px) {
  .main-content {
    grid-template-columns: 1fr;
    gap: 40px;
  }

  .right-column {
    order: -1;
  }
}
</style>
