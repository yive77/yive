import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router';
import OAuthHandler from './components/OAuthHandler'
import Login from './components/Login'

Vue.use(VueRouter);
Vue.config.productionTip = false

const router = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/login', component: Login,
        },
        {
            path: '/oauth2/cb', component: OAuthHandler
        }
    ]
});

new Vue({
    router,
    render: h => h(App),
}).$mount('#app')
