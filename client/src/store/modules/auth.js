/* eslint-disable no-alert, no-console, no-unused-vars*/


import axios from 'axios'; 
import qs from 'querystring';
const login_url = "http://localhost:8081/api/login";

const state = {
    authenticated: false,
    user: {}
}

const getters = {
    isAuthorized: (state) => {
        return state.authenticated;
    },
    getUser: (state) => {
        return state.user;
    }
}

const actions = {
    login: ({commit}, form) => {
        if (form.email.length > 0 && form.password.length > 0) {
            return new Promise((resolve, reject) => {
                axios.post(login_url, qs.stringify(form)).then(response => {
                    if (response.data.success) {
                        commit('updateAuthenticated', {authenticated: true, user: response.data.user})
                    }
                    resolve(response)
                }).catch(error => {
                    reject(error);
                })
            })
        }
    },
    logout: ({commit}) => {
        commit('logout');
    }
}

const mutations = {
    updateAuthenticated: (state, obj) => {
        state.authenticated = obj.authenticated;
        state.user = obj.user;
    },
    logout: (state) => {
        state.authenticated = false;
        state.user = {};
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
