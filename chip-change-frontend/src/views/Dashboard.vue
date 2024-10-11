<template>
  <div class="dashboard">
    <h2>User Dashboard</h2>
    <p>Welcome, {{ user.email }}</p>
  </div>
</template>

<script>
export default {
  name: 'UserDashboard',
  data() {
    return {
      user: {
        email: 'user@example.com',
      },
    };
  },
};
</script>

<style scoped>
.dashboard {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h2 {
  color: #333;
}

p {
  color: #666;
}
</style>
