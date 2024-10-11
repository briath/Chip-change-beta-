<template>
  <div class="transactions">
    <h2>Transactions</h2>
    <ul>
      <li v-for="transaction in transactions" :key="transaction.id">
        Transaction ID: {{ transaction.id }} - {{ transaction.amount }} chips
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'UserTransactions',
  data() {
    return {
      transactions: [],
    };
  },
  async created() {
    try {
      const response = await axios.get('http://localhost:8000/api/transactions');
      this.transactions = response.data;
    } catch (error) {
      console.error(error);
    }
  },
};
</script>

<style scoped>
.transactions {
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
  margin-bottom: 20px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  padding: 10px;
  border-bottom: 1px solid #ddd;
}

li:last-child {
  border-bottom: none;
}
</style>
