<template>
  <div class="create-announcement">
    <h2>Create Announcement</h2>
    <form @submit.prevent="createAnnouncement">
      <input type="number" v-model="chipsAmount" placeholder="Chips Amount" required />
      <input type="number" v-model="rate" placeholder="Exchange Rate" required />
      <input type="number" v-model="minVolume" placeholder="Minimum Volume" required />
      <input type="text" v-model="paymentMethod" placeholder="Payment Method" required />
      <button type="submit">Create</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CreateAnnouncement',
  data() {
    return {
      chipsAmount: 0,
      rate: 0,
      minVolume: 0,
      paymentMethod: '',
    };
  },
  methods: {
    async createAnnouncement() {
      try {
        const response = await axios.post('http://localhost:8000/api/announcements', {
          chipsAmount: this.chipsAmount,
          rate: this.rate,
          minVolume: this.minVolume,
          paymentMethod: this.paymentMethod,
        });
        console.log(response.data);
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

<style scoped>
.create-announcement {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  color: #333;
  margin-bottom: 20px;
}

input {
  display: block;
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border-radius: 4px;
  border: 1px solid #ccc;
  font-size: 1rem;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #28a745;
  border: none;
  border-radius: 4px;
  color: white;
  font-size: 1rem;
  cursor: pointer;
}

button:hover {
  background-color: #218838;
}
</style>
