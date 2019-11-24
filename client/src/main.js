import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router';
import OAuthHandler from './components/OAuthHandler'

Vue.use(VueRouter);
Vue.config.productionTip = false

const router = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/oauth2/cb', component: OAuthHandler
        }
    ]
});

new Vue({
    router,
    render: h => h(App),
}).$mount('#app')
