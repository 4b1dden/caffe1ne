import Vuex from 'vuex';
import Vue from 'vue';

Vue.use(Vuex);

import state from './state';
import mutations from './mutations';
import getters from './getters';

export default new Vuex.Store({
    state: state,
    mutations: mutations,
    getters: getters
});