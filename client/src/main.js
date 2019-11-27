import Vue from 'vue';
import App from './App';
import VueRouter from 'vue-router';
import OAuthHandler from './components/OAuthHandler';
import Login from './components/Login';
import Home from './components/Home';
import Register from './components/Register';
import store from './store/index';

Vue.use(VueRouter);
Vue.config.productionTip = false

const router = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: "/", component: Home
        },
        {
            path: '/login', component: Login
        },
        {
            path: '/register', component: Register
        },
        {
            path: '/oauth2/cb', component: OAuthHandler
        }
    ]
});

new Vue({
    store,
    router,
    render: h => h(App),
}).$mount('#app')
