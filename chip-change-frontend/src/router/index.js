import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/views/Home.vue';
import UserLogin from '@/views/Login.vue';
import UserDashboard from '@/views/Dashboard.vue';
import CreateAnnouncement from '@/views/CreateAnnouncement.vue';
import UserTransactions from '@/views/Transactions.vue';

const routes = [
  { path: '/', name: 'Home', component: HomePage },
  { path: '/login', name: 'Login', component: UserLogin },
  { path: '/dashboard', name: 'Dashboard', component: UserDashboard },
  { path: '/create-announcement', name: 'CreateAnnouncement', component: CreateAnnouncement },
  { path: '/transactions', name: 'Transactions', component: UserTransactions },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
