<template>
  <footer class="site-footer">
    <div class="footer-content">
      <div class="footer-section">
        <h4>THE BASICS</h4>
        <ul>
          <li><a href="#">About TMDB</a></li>
          <li><a href="#">Contact Us</a></li>
          <li><a href="#">Support Forums</a></li>
          <li><a href="#">API</a></li>
        </ul>
      </div>
      <div class="footer-section">
        <h4>GET INVOLVED</h4>
        <ul>
          <li><a href="#">Contribution Bible</a></li>
          <li><a href="#">Add New Movie</a></li>
          <li><a href="#">Add New TV Show</a></li>
        </ul>
      </div>
      <div class="footer-section">
        <h4>COMMUNITY</h4>
        <ul>
          <li><a href="#">Guidelines</a></li>
          <li><a href="#">Discussions</a></li>
          <li><a href="#">Leaderboard</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2023 TMDB. All rights reserved.</p>
      <div class="social-icons">
        <a href="#" aria-label="Facebook"><i class="fab fa-facebook"></i></a>
        <a href="#" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
        <a href="#" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.site-footer {
  background-color: #032541;
  color: #ffffff;
  padding: 40px 0 20px;
  font-weight: var(--font-weight-normal);
}

.footer-content {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  max-width: 1200px;
  margin: 0 auto;
}

.footer-section {
  margin-bottom: 20px;
}

h4 {
  font-size: 1.2em;
  margin-bottom: 15px;
  color: #01b4e4;
  font-weight: var(--font-weight-bold);
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
}

a {
  color: #ffffff;
  text-decoration: none;
  transition: color 0.3s ease;
  font-weight: var(--font-weight-medium);
}

a:hover {
  color: #01b4e4;
}

.footer-bottom {
  text-align: center;
  margin-top: 30px;
  padding-top: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.social-icons {
  margin-top: 15px;
}

.social-icons a {
  font-size: 1.5em;
  margin: 0 10px;
}

@media (max-width: 768px) {
  .footer-content {
    flex-direction: column;
    align-items: center;
  }

  .footer-section {
    text-align: center;
    margin-bottom: 30px;
  }
}
</style>
