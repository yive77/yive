/* eslint-disable no-alert, no-console */

import homeAuthApi from '../../api/homeAuth';

const state = {
    accessToken: null
}

const getters = {
    isAuthorized: currentState => !!currentState.accessToken
}

const actions = {
    login: (currentState, email, password) => {
        console.log(currentState);
        console.log(email, password)
        homeAuthApi.login();
    },
    logout: () => {

    }
}

const mutations = {
    updateToken: (currentState, accessToken) => {
        currentState.accessToken = accessToken;
    },
    
}

export default {
    state,
    getters,
    actions,
    mutations
}
