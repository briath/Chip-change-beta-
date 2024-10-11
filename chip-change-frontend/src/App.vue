<template>
  <div id="app">
    <header>
      <nav>
        <ul>
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/login">Login</router-link></li>
          <li><router-link to="/dashboard">Dashboard</router-link></li>
          <li><router-link to="/create-announcement">Create Announcement</router-link></li>
          <li><router-link to="/transactions">Transactions</router-link></li>
        </ul>
      </nav>
    </header>
    <main>
      <router-view></router-view>
    </main>
    <footer>
      <p>© 2024 Chip-Change. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style scoped>
/* Основные стили для приложения */
#app {
  font-family: 'Arial', sans-serif;
  color: #333;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

/* Стили для заголовка и навигации */
header {
  background-color: #004d99;
  padding: 10px 0;
}

nav {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

nav ul {
  list-style: none;
  display: flex;
  justify-content: space-around;
  padding: 0;
  margin: 0;
}

nav li {
  margin: 0 10px;
}

nav a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

nav a:hover {
  text-decoration: underline;
}

/* Стили для основного контента */
main {
  flex: 1;
  max-width: 1200px;
  margin: 20px auto;
  padding: 20px;
  background-color: #f0f8ff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* Стили для футера */
footer {
  background-color: #004d99;
  color: white;
  text-align: center;
  padding: 10px 0;
}

footer p {
  margin: 0;
  font-size: 0.9rem;
}
</style>
