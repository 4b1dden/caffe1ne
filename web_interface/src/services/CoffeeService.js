import api from './api';
import constants from '../constants';
import store from '../store/store';

export default {
    getCoffeeStats: function() {
        return new Promise (
            async function (resolve, reject) {
                const response = await api.get(constants.API.ENDPOINTS.STATS.ENTRY);
                if (response.ok) resolve(response.data);
                else reject(response);
            }
        )
    },
    requestCoffee: function (obj) {
        return new Promise (
            async function (resolve, reject) {
                const response = await api.post(constants.API.ENDPOINTS.COFFEE.ENTRY, obj)
                if (response.ok) resolve(response.data);
                else reject(response);
            }
        )
    }
}