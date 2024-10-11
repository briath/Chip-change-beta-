import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
// import './assets/styles.css'; // Если у вас есть глобальные стили

createApp(App).use(router).mount('#app');
